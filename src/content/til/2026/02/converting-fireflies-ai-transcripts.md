---
title: "Converting Fireflies.ai transcripts to clean Markdown"
description: "Workflow to turn messy Fireflies.ai HTML exports into clean, readable Markdown."
pubDate: 2026-02-05
tags: ["fireflies", "markdown", "python", "automation", "productivity"]
draft: false
---

Fireflies.ai is great for meeting transcripts, but exporting them as usable Markdown can be messy due to embedded images, tracking pixels, and weird capitalization typos (like doubled uppercase letters at sentence starts). 

Here is my workflow for converting a Fireflies transcript into a clean, searchable Markdown file.

## 1. Get the HTML Transcript
Fireflies doesn't always provide a direct clean Markdown export. The most reliable way to get all the data is to save the web page itself:

1. **Open the transcript**: Navigate to the specific meeting in your Fireflies dashboard.
2. **Load all content**: Scroll through the entire transcript to ensure lazy-loading elements are rendered.
3. **Save as HTML**: 
   - Press `Cmd + S` (macOS) or `Ctrl + S`.
   - Choose **"Webpage, HTML Only"** (important: don't save the "Complete" webpage with assets).
   - Save it to your project folder (e.g., `my-meeting.html`).

## 2. Process with Automation
I use a master Python script that chains three specialized tools:
1. **Pandoc**: Converts HTML to GF-Markdown while stripping raw HTML tags.
2. **Image/Emoji Remover**: Cleans out data-URIs, tracking pixels, and distracting emojis.
3. **Double-Cap Fixer**: Fixes common sentence-start typos (e.g., "AAple" → "Apple").

### The Master Script
Run the script on your saved HTML file:

```bash
python3 scripts/process_firefly_transcript.py path/to/transcript.html
```

The script automatically creates a `.md` file in the same directory, cleaned and ready for your notebook or blog.

## 3. The Logic Behind the Clean-up
The most satisfying part of this automation is fixing "Double Caps" using Regex. Meeting transcripts often capture the first letter twice when the speaker starts abruptly:

**Regex Pattern:** `(?m)(^|[.?!]\s+)(\s*)([A-Z])\3`  
**Replacement:** `\1\2\3`

This ensures that only double letters at the **start of a line or sentence** are fixed, while names like "Aaron" in the middle of a sentence remains untouched.
