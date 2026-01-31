---
title: "Deploying Datasette to Cloudflare Workers"
description: "TIL how to use datasette-ts and Alchemy to deploy SQLite databases to the edge using Cloudflare Workers and D1."
pubDate: 2026-02-01
tags: ["cloudflare", "datasette", "sqlite", "serverless"]
draft: false
---

Today I learned how to deploy a Datasette-style interface to Cloudflare Workers using the [datasette-ts](https://github.com/scttcper/datasette-ts) utility. This transition from Python to TypeScript allows for hosting data explorers on Cloudflare's global edge network.

## Getting Started

The deployment process is remarkably streamlined, leveraging a tool called **Alchemy** to manage the Cloudflare resources.

### 1. Installation

First, install the CLI tool globally:

```bash
npm install -g datasette-ts
```

### 2. Configuration

Before deploying, you need to link the tool to your Cloudflare account. Alchemy handles the authentication:

```bash
npx alchemy configure
npx alchemy login
```

### 3. Deployment

To deploy a local SQLite database, you simply point the tool at your `.db` file. The command automatically provisions a Cloudflare Worker and a **D1 database** instance:

```bash
datasette-ts deploy cloudflare ./my-data.db
```

### Advanced Options:
- **Custom Name**: Use `--name my-app-name` to define the worker's name.
- **Metadata**: Add a `datasette.yml` file to configure site-wide settings and SEO:
  ```bash
  datasette-ts deploy cloudflare ./my-data.db --metadata datasette.yml
  ```
- **Caching**: Performance can be tuned using the `--setting default_cache_ttl <seconds>` flag (defaults to 5 seconds).

## Why this matters

By porting Datasette to TypeScript and Cloudflare, we get:
- **Zero-maintenance infrastructure**: No servers to manage.
- **Global Performance**: Data is served from the edge, closest to the user.
- **Scalability**: Cloudflare D1 and Workers handle the scaling automatically.

For more details and the full source code, check out the repository: [scttcper/datasette-ts](https://github.com/scttcper/datasette-ts).
