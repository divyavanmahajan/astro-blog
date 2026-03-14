---
title: "Converting PPTX to Markdown with pptx2md"
description: "How to use the pptx2md python tool to convert PowerPoint presentations into Markdown, preserving structure, images, and formatting."
pubDate: 2026-03-14
tags: ["python", "markdown", "automation", "tools", "pptx", "productivity"]
draft: false
---

Today I learned how to automatically convert PowerPoint (`.pptx`) presentations into Markdown files using `pptx2md`.

## The Problem

Extracting content from a PowerPoint presentation manually to create Markdown documents is tedious, especially when dealing with complex formatting, nested lists, images, and tables. Automating this process while preserving the structural hierarchy of the presentation is highly desirable for documentation.

## The Solution

The tool [`pptx2md`](https://github.com/ssine/pptx2md) is a Python utility that handles this conversion automatically. It preserves text formatting (bold, italic, colors, hyperlinks), extracts images to a local directory, and supports tables with merged cells.

First, install the package. Note that it requires Python 3.10 or later:
```bash
pip install pptx2md
```

Then, you can run the basic conversion command:
```bash
pptx2md presentation.pptx
```
By default, this generates an `out.md` file and extracts all images into an `/img/` directory.

### Advanced Features

One of the most powerful features is **Custom Titles**. If you want to generate a hierarchical table of contents, you can define your own title list in a separate text file (e.g., `titles.txt`), specifying indentation levels to indicate parent-child relationships. The tool uses fuzzy matching to map slide titles to your predefined levels. 

You can pass this file using the `-t` argument, along with other helpful flags:

```bash
pptx2md presentation.pptx -t titles.txt -o result.md --image-width 500 --enable-slides
```

*   `-o result.md`: Specifies the output markdown filename instead of the default `out.md`.
*   `-i [path]`: Specifies a custom directory for extracted pictures.
*   `--image-width 500`: Constrains the extracted image widths by utilizing HTML `<img>` tags instead of markdown syntax.
*   `--enable-slides`: Delineates slides with `\n---\n`, which is perfect if you want to convert the `.pptx` directly into Markdown slides.

## Why This Matters

This tool saves massive amounts of time typically spent manually copying and pasting when migrating presentations to wiki platforms, Markdown-based documentation sites (like Astro or Docusaurus), or generating code-based slides (like Quarto or Reveal.js). Its advanced capabilities, like fuzzy matching for slide headers and automatic table parsing, make it a very robust utility for content workflows.
