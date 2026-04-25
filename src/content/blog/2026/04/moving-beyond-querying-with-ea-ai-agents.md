---
title: "Moving Beyond Querying: Building Deterministic EA Tools with AI Agents"
description: "Learn how to move beyond interactive querying with LLMs by instructing them to maintain memory and code reusable Python scripts for Enterprise Architecture."
pubDate: 2026-04-25
author: "Divya van Mahajan"
categories: ["AI", "Enterprise Architecture"]
tags: ["Agents", "Automation", "Copilot", "Claude", "Python", "Neo4j"]
heroImage: "/images/moving-beyond-querying-with-ea-ai-agents-hero.png"
linkedin: true
linkedinMessage: "Part 4 of our AI in Architecture series is here! We are moving beyond interactive queries. Discover how to instruct Copilot or Claude to maintain contextual memory and build deterministic, reusable Python tools for Enterprise Architecture analysis. 🚀 #EnterpriseArchitecture #AI #AgenticAI #Python"
series: "ai_in_arch-004"
draft: false
---

# Introduction

In our previous explorations of integrating AI with Enterprise Architecture (EA), we focused heavily on extracting data into highly traversable Neo4j Knowledge Graphs and conversing with that data. While interactive querying with tools like Copilot or Claude is incredibly powerful, it is only the tip of the iceberg. 

Today, we are going to move beyond conversational queries. We are going to explore how to instruct AI agents to **learn, remember, and build reusable tools** for your architecture practice.

## The Power of Contextual Memory

When working on complex architectural assignments—such as migrating core systems or mapping thousands of business capabilities—a standard AI session can quickly lose track of the overarching constraints and goals.

The secret to unlocking advanced agentic workflows is explicit prompting for persistent memory. By giving your AI Copilot or Claude the following core instruction, you completely change how it operates:

> "Create and maintain a running memory of key details, constraints, and goals. Update it as we go. Before answering, review that memory and use it. Store this in memory.md. Keep any code created in the scripts folder and keep track of what they do."

This simple directive shifts the AI from a stateless chatbot to an integrated development partner. It ensures the model grounds its reasoning in your evolving, localized context.

## From Conversation to Deterministic Tools 

When you establish this persistent memory loop, the AI is no longer just "answering questions." It begins to write persistent Python programs that can perform multi-step investigations and prepare comprehensive Markdown reports on its findings.

These programs become incredibly valuable building blocks:
1. **Compounding Agentic Intelligence:** Your coding agent can use these scripts as foundations for even more complicated analysis, chaining them together to explore the knowledge graph autonomously.
2. **Deterministic Artifact Generation:** These scripts can be run *without the need for AI*. You essentially use the LLM to write deterministic programmatic tools that generate the exact same high-quality EA artifacts over and over again, completely eliminating hallucination risk for those specific reports.

This mixed approach to AI—combining dynamic, probabilistic reasoning with deterministic, scripted tools—enables you to rapidly bootstrap your own custom EA helper utilities. 

## A Real-World Use Case: Mapping Capabilities to Apps

I recently applied this exact methodology to a classic, tedious EA problem: **Mapping Business Capabilities to Applications**.

Instead of manually analyzing spreadsheets or having a lengthy back-and-forth chat with Claude, I gave it my instruction for persistent memory and told it the overarching objective. The AI autonomously authored a suite of Python scripts that connected to our architecture sources, traversed the relationships, and generated a deep analysis report.

I was genuinely pleasantly surprised by the depth of the analysis, the accuracy of its capability-to-application bridging, and the strategic suggestions it surfaced. What used to take days of manual correlation was accomplished efficiently and turned into a repeatable, click-button Python tool for the future.

***

Good luck architecting!

## The AI Agent Roadmap

This post is part of a series on AI in Enterprise Architecture. Continue reading the previous parts here:

1. **[Building the Integration: Extracting LeanIX to Neo4j](/blog/2026/04/building-the-leanix-neo4j-integration/)** - A deep dive into extracting LeanIX data and modeling it into a Neo4j Knowledge Graph.
2. **[Connecting Neo4j to AI Agents with MCP](/blog/2026/04/connecting-neo4j-to-ai-agents-with-mcp/)** - Wiring your graph directly into Claude using the Model Context Protocol.
