---
title: "Building the Integration: Extracting LeanIX to Neo4j"
description: "A deep dive into extracting LeanIX data and modeling it into a Neo4j Knowledge Graph using dvm-leanix and idempotent Cypher load scripts."
pubDate: 2026-04-12
author: "Divya van Mahajan"
categories: ["AI", "Enterprise Architecture"]
tags: ["Knowledge Graph", "Neo4j", "SAP LeanIX", "Integration", "Cypher"]
heroImage: "/images/building-the-leanix-neo4j-integration-hero.png"
linkedin: true
linkedinMessage: "Part 2 of the AI in Architecture series is out! Learn how to extract your SAP LeanIX factsheets and model them directly into a Neo4j Knowledge Graph. #EnterpriseArchitecture #Neo4j #KnowledgeGraph"
series: "ai_in_arch-002"
draft: false
---

# Introduction

In our previous post, we explored the massive potential of combining Enterprise Architecture, Knowledge Graphs, and LLMs. The theory makes sense, but how do we actually build this? 

In this second part of the series, we take a deep dive into the practical side: extracting your operational data out of SAP LeanIX and modeling it into Neo4j as a highly traversable graph.

## Step 1: Setting up the LeanIX Proxy

First, we need to authenticate and connect to our workspace. To bypass complex API limitations, we'll leverage a proxy CLI tool called `dvm-leanix`. 

You can investigate its capabilities by running the help command locally:
```bash
uvx dvm-leanix --help
```

This reveals standard options for proxying LeanIX:
```text
Options
-------
    --url           LeanIX workspace base URL
    --port          Port to listen on (default: 8765)
    --connect       Chrome DevTools Protocol endpoint to connect to an existing browser
```

Using this tool, you can easily deploy a local proxy (`dvm-leanix serve`) that handles the OAuth handshakes and interfaces with your LeanIX workspace, giving you a streamlined pipeline to query exactly the data you need.

## Step 2: Generating the Schema Mapping

With the proxy running, we need to translate the LeanIX data model into a graph structure. LeanIX uses **Factsheets** (e.g., Applications, IT Components) and deeply nested **Relationships**. A GraphQL extraction returns verbose relations like `relApplicationToBusinessCapability`.

In our Neo4j model, we want to flatten and clarify this semantic link into a clear Graph edge:
```cypher
(Application)-[:SUPPORTS]->(BusinessCapability)
```

To automate this, we use the `dvm-eagraph` tool. First, we generate a mapping file:
```bash
uvx dvm-eagraph --generate-mapping
```
This scans your live LeanIX workspace and generates a YAML mapping file that controls which FactSheet types to load and how Neo4j node labels and relationship names are derived.

## Step 3: Downloading and Loading into Neo4j

Once your mapping is configured, `dvm-eagraph` handles the heavy lifting of pulling the data and writing it to Neo4j.

You can see its capabilities via the help command:
```bash
uvx dvm-eagraph --help
```

```text
Usage
-----
    # Full run (download from LeanIX + load into Neo4j)
    dvm-eagraph

    # Use a custom mapping file
    dvm-eagraph --mapping my-mapping.yaml

    # Download only (saves JSON, skips Neo4j)
    dvm-eagraph --skip-neo4j
```

Instead of manually crafting complex, idempotent Cypher `MERGE` queries, `dvm-eagraph` takes your mapping file, downloads the necessary JSON payloads via the proxy, and automatically executes optimal Neo4j transaction batches. 

With the nodes instantiated and the relationships forged, what used to be nested JSON objects is now a rich, visual map of your entire enterprise ecosystem.

## What's Next?

Our enterprise logic is now mathematically modeled in a graph database. The next step? Giving it a proxy to speak! 

In our next follow-up, we will explore **Connecting Neo4j to Copilot (or Claude)**, detailing how to utilize the Model Context Protocol (MCP) to let your AI agents query your new architecture graph in natural language.
