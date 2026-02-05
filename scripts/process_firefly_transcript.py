#!/usr/bin/env python3
import argparse
import subprocess
import os
import sys

def run_command(command):
    """Runs a shell command and exits on failure."""
    print(f"Executing: {' '.join(command)}")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        sys.exit(1)

def post_process(file_path):
    """Performs final structural cleanup on the markdown file."""
    import re
    print(f"Post-processing: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Add # Info at the start (avoid double adding if re-run)
        if not content.startswith("# Info"):
            content = "# Info\n\n" + content
        
        # 2. Replace General\nSummary with # General Summary
        content = re.sub(r'(?m)^General\nSummary', '# General Summary', content)
        
        # 3. Replace Transcript with # Transcript
        content = re.sub(r'(?m)^Transcript$', '# Transcript', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        print(f"Error during post-processing: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Master script to process Fireflies.ai transcripts: converts HTML, removes images, and fixes double caps typos."
    )
    parser.add_argument("input_html", help="Path to the input HTML file")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_html):
        print(f"Error: Input file '{args.input_html}' not found.")
        sys.exit(1)
        
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Convert HTML to Markdown (and clean HTML tags)
    # This creates a .md file with the same base name.
    convert_script = os.path.join(script_dir, "convert_html.py")
    run_command([sys.executable, convert_script, args.input_html, "--clean"])
    
    # Get the resulting markdown file path
    base_name = os.path.splitext(args.input_html)[0]
    markdown_file = base_name + ".md"
    
    if not os.path.exists(markdown_file):
        print(f"Error: Expected markdown file '{markdown_file}' was not created.")
        sys.exit(1)
        
    # 2. Remove images and emojis
    remove_images_script = os.path.join(script_dir, "remove-images.py")
    # By default remove-images.py removes emojis and data:image tags. 
    # The user asked to run it, implying default cleaning behavior.
    run_command([sys.executable, remove_images_script, markdown_file])
    
    # 3. Fix double uppercase letters at sentence starts
    fix_caps_script = os.path.join(script_dir, "fix_double_caps.py")
    run_command([sys.executable, fix_caps_script, markdown_file, "--in-place"])
    
    # 4. Final structural cleanup
    post_process(markdown_file)
    
    print(f"\nSuccess! Processed transcript saved to: {markdown_file}")

if __name__ == "__main__":
    main()
