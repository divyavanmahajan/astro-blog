#!/usr/bin/env python3
import re
import argparse
import os
import shutil
import sys

def clean_document(file_path, remove_emojis=True, all_images=False, backup=True, dry_run=False, verbose=False):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex patterns
    
    # 1. data:image (Markdown and HTML)
    data_img_md = re.compile(r'!\[[^\]]*\]\(data:image/[^)]+\)')
    data_img_html = re.compile(r'<img\s+[^>]*src=["\']data:image/[^"\']+["\'][^>]*>')
    
    # 2. All images (Markdown and HTML)
    all_img_md = re.compile(r'!\[[^\]]*\]\([^)]+\)')
    all_img_html = re.compile(r'<img\s+[^>]*src=["\'][^"\']+["\'][^>]*>')
    
    # 3. Emojis (Unicode range for most emojis and supplementary symbols)
    # This range \U00010000-\U0010ffff covers the high plane where emojis reside
    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)

    # Counting matches for reporting
    data_md_matches = data_img_md.findall(content)
    data_html_matches = data_img_html.findall(content)
    
    total_img_md_matches = all_img_md.findall(content)
    total_img_html_matches = all_img_html.findall(content)
    
    emoji_matches = emoji_pattern.findall(content)

    if verbose or dry_run:
        print(f"Document analysis for '{file_path}':")
        print(f"  - data:image occurrences (MD/HTML): {len(data_md_matches)} / {len(data_html_matches)}")
        print(f"  - Total image tag occurrences (MD/HTML): {len(total_img_md_matches)} / {len(total_img_html_matches)}")
        print(f"  - Emoji occurrences: {len(emoji_matches)}")

    if dry_run:
        print("Dry run: No changes made.")
        return

    # Transformations
    new_content = content
    
    # Image removal
    if all_images:
        if verbose: print("  Removing all images...")
        new_content = all_img_md.sub('', new_content)
        new_content = all_img_html.sub('', new_content)
    else:
        if verbose: print("  Removing data:image tags...")
        new_content = data_img_md.sub('', new_content)
        new_content = data_img_html.sub('', new_content)
        
    # Emoji removal
    if remove_emojis:
        if verbose: print("  Removing emojis...")
        new_content = emoji_pattern.sub('', new_content)

    # Clean up whitespace (triple newlines or more)
    new_content = re.sub(r'\n{3,}', '\n\n', new_content)

    if new_content == content:
        print("No changes needed. Document is already clean.")
        return

    # Create backup
    if backup:
        bak_path = file_path + ".bak"
        if verbose:
            print(f"Creating backup at '{bak_path}'")
        shutil.copy2(file_path, bak_path)

    # Save
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Successfully processed '{file_path}'.")
    if backup:
        print(f"Original file backed up to '{file_path}.bak'.")

def main():
    parser = argparse.ArgumentParser(description="Clean documents by removing data:image URIs, emojis, and optionally all images.")
    parser.add_argument("file", help="Path to the file to process")
    
    # Emoji options
    parser.add_argument("--no-emojis", action="store_true", default=True, help="Remove emojis (default: True)")
    parser.add_argument("--keep-emojis", action="store_false", dest="no_emojis", help="Keep emojis in the document")
    
    # Image options
    parser.add_argument("--all-images", action="store_true", help="Remove all images (external and local), not just data:image")
    
    # Backup options
    parser.add_argument("-b", "--backup", action="store_true", default=True, help="Create a .bak file before modifying (default: True)")
    parser.add_argument("--no-backup", action="store_false", dest="backup", help="Do not create a backup file")
    
    # Misc
    parser.add_argument("-d", "--dry-run", action="store_true", help="Show what would be removed without modifying the file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print detailed information")

    args = parser.parse_args()

    clean_document(
        args.file, 
        remove_emojis=args.no_emojis, 
        all_images=args.all_images, 
        backup=args.backup, 
        dry_run=args.dry_run, 
        verbose=args.verbose
    )

if __name__ == "__main__":
    main()
