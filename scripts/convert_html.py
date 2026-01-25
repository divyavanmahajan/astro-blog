#!/usr/bin/env python3
import sys
import subprocess
import os
import argparse

# This script requires pandoc to be installed: brew install pandoc

def convert(input_file, output_file=None, clean=False):
    if not output_file:
        base, _ = os.path.splitext(input_file)
        output_file = base + ".md"
    
    # Check if pandoc is installed
    try:
        subprocess.run(["pandoc", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("Error: pandoc is not installed or not in PATH.")
        print("Please install pandoc (e.g., 'brew install pandoc' on macOS) before running this script.")
        sys.exit(1)

    print(f"Converting '{input_file}' to '{output_file}'...")
    
    target_format = "gfm-raw_html" if clean else "gfm"
    if clean:
        print("Note: HTML tags will be stripped (-t gfm-raw_html)")

    try:
        # Using markdown_strict or just markdown. Common Mark or GFM are also options.
        # -t gfm (GitHub Flavored Markdown) is usually best for blogs.
        # -raw_html extension disables raw HTML blocks and inline HTML
        subprocess.run(["pandoc", input_file, "-f", "html", "-t", target_format, "-o", output_file], check=True)
        print(f"Success! Output saved to: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HTML to Markdown using pandoc.")
    parser.add_argument("input_file", help="Path to the input HTML file")
    parser.add_argument("output_file", nargs="?", help="Path to the output Markdown file (optional)")
    parser.add_argument("--clean", action="store_true", help="Strip all HTML tags from the output")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' not found.")
        sys.exit(1)
        
    convert(args.input_file, args.output_file, args.clean)
