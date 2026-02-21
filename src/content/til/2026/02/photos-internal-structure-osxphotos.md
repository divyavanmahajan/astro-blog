---
title: "TIL: Apple Photos Library Internal Structure via osxphotos"
description: "Insights into the undocumented schema of Apple's Photos.sqlite database based on the osxphotos project."
pubDate: 2026-02-21
categories: ["Databases", "macOS"]
tags: ["Photos.sqlite", "osxphotos", "SQLite", "Reverse-Engineering"]
---

While Apple's Photos database (`Photos.sqlite`) is undocumented, the [osxphotos](https://github.com/RhetTbull/osxphotos) project has done extensive work reverse-engineering its schema. Here’s a summary of the internal structure and how it manages your media.

## The Photos Ecosystem
The Photos app relies on multiple interconnected databases:
- **`Photos.sqlite`**: The primary database storing media metadata, albums, and relationship info.
- **`mediaanalysis.db`**: Stores results from AI/ML analysis (scene recognition, quality scores).
- **`psi.sqlite`**: Contains searchable text strings (OCR) from photo content.

## Key Tables in `Photos.sqlite`
The database uses Apple's Core Data framework, so most names start with `Z`.

| Table | Purpose |
| :--- | :--- |
| `ZASSET` | The core table. Each row is a single photo or video. |
| `ZADDITIONALASSETATTRIBUTES` | Stores metadata like original filenames and user-added descriptions. |
| `ZEXTENDEDATTRIBUTES` | Technical EXIF data: ISO, Aperture, Camera/Lens models. |
| `ZINTERNALRESOURCE` | Maps assets to the actual files on disk (Originals, Thumbs). |
| `ZGENERICALBUM` | Manages both Albums and Folders. |
| `ZPERSON` & `ZDETECTEDFACE` | Stores facial recognition data and person identities. |
| `ZMOMENT` | Groups photos by time and location. |

## Tracking Changes
To stay in sync with iCloud and other processes, the database uses **Persistent History**:
- `ACHANGE` / `ATRANSACTION`: These tables track every modification to the database, allowing the Photos app to "catch up" on changes efficiently.

## Practical Direct Querying
Because the schema is complex and changes between macOS versions, projects like `osxphotos` create an in-memory abstraction layer to provide a stable API. If you need to query it directly, focus on joining `ZASSET` with `ZADDITIONALASSETATTRIBUTES` to get human-readable filenames:

```sql
SELECT a.ZUUID, att.ZORIGINALFILENAME, a.ZDATECREATED
FROM ZASSET a
JOIN ZADDITIONALASSETATTRIBUTES att ON a.Z_PK = att.ZASSET;
```

This structural understanding is essential for data recovery or building custom photo management tools.
