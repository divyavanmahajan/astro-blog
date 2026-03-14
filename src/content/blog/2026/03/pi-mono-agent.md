---
title: "Pi: The Minimal Coding Agent & Master of Mischief"
description: "Exploring Pi-mono, a minimalistic coding agent, and pi-mom, a self-managing Slack bot that writes its own tools."
pubDate: 2026-03-14
author: "Divya van Mahajan"
categories: ["AI"]
tags: ["ai-agent", "agents", "pi", "automation", "slack-bot"]
heroImage: "/images/pi-mono-agent-hero.png"
linkedin: true
linkedinMessage: "Agents building agents! 🤯 Discover how Pi-mono and its Slack bot Master of Mischief (Mom) throw out predefined skills in favor of writing their own tools. Read the latest in the AI Agent series."
series: "ai-agent"
draft: false
---

# Introduction

In the rapidly evolving landscape of AI agents, projects often trend toward maximalism—bundling countless skills, massive configuration files, and rigid tool ecosystems. However, one of the most fascinating approaches making waves recently is the exact opposite. 

Let's talk about **Pi**, a minimalistic coding agent at the core of projects like OpenClaw, and its self-managing Slack bot counterpart, **Mom** (Master of Mischief).

## What is Pi?

[Pi](https://github.com/badlogic/pi-mono/) (specifically the `pi-mono` monorepo created by Mario Zechner) is a tiny but incredibly powerful coding agent toolkit. At its core, Pi is defined by what it *doesn't* have:
- **No massive toolsets**: It ships with an incredibly short system prompt and only four foundational tools: `Read`, `Write`, `Edit`, and `Bash`.
- **No built-in MCP (Model Context Protocol) reliance**: Instead of downloading external extensions or relying on predefined protocols out of the box, Pi extends *itself*. If you want it to do something new, you ask it to write code and run it.

As Armin Ronacher points out in his deep dive, ["Pi: The Minimal Agent Within OpenClaw"](https://lucumr.pocoo.org/2026/1/31/pi/), Pi is an agent built for agents building agents. It supports persistent session state, hot-reloading extensions, and a malleable architecture that turns software into moldable clay.

## Mom (Master of Mischief)

One of the most impressive practical applications built on top of the Pi toolkit is [Mom](https://github.com/badlogic/pi-mono/tree/main/packages/mom). 

Mom is a Slack bot powered by an LLM that autonomously interacts with your development environment. Because it uses Pi's philosophy, **she is entirely self-managing**. She doesn't come with pre-built skills for reading APIs or manipulating databases; instead, she writes bash scripts, installs her own tools (like `jq` or `git`), and crafts highly specific CLI tools for whatever task you assign her.

Mom operates within a secure environment, ideally an isolated Docker sandbox, keeping your host system safe while she iterates and solves problems in her private workspace.

***

## Demo: Setting up Pi-Mom

Here is a quick step-by-step guide to get Mom running in a secure Docker sandbox.

### 1. Set Environment Variables
You'll need tokens to authenticate the Slack App, the Slack Bot, and your LLM of choice (like Anthropic).
```bash
export MOM_SLACK_APP_TOKEN=xapp-...
export MOM_SLACK_BOT_TOKEN=xoxb-...

# Using Anthropic API directly
export ANTHROPIC_API_KEY=sk-ant-...
```
*(Note: You can also use Pi's `/login` feature to authenticate via a browser).*

### 2. Create the Docker Sandbox
We highly recommend running Mom inside a Docker container rather than on your host machine, since she has the power to execute arbitrary bash commands.
```bash
docker run -d \
  --name mom-sandbox \
  -v $(pwd)/data:/workspace \
  alpine:latest \
  tail -f /dev/null
```

### 3. Run Mom
Now, run the Mom package, pointing it to the Docker sandbox and your local data directory.
```bash
npx @mariozechner/pi-mom --sandbox=docker:mom-sandbox ./data
```

Once running, you can @mention mom in your designated Slack channel. Ask her to create a tool to monitor a server, write a python script, or track issue metrics. She will autonomously construct the tools she needs and execute them in the sandbox.

***

## Sources and Further Reading

- [Pi: The Minimal Agent Within OpenClaw](https://lucumr.pocoo.org/2026/1/31/pi/) by Armin Ronacher
- [Pi-mono GitHub Repository](https://github.com/badlogic/pi-mono)
- [Pi-mom Package Documentation](https://github.com/badlogic/pi-mono/tree/main/packages/mom)

***

## The AI Agent Roadmap

This post is part of a series on **AI Agents**. Stay tuned as we dive deeper into agentic workflows and how they reshape modern software engineering!
