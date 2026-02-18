# Greed Discord Bot

## Overview
Greed is a Discord bot built with Python (discord.py) featuring clustering support, music, economy, moderation, social integrations, and more. Originally migrated from a GitHub repository to run in the Replit environment.

## Current State
- Bot loads and attempts to connect to Discord successfully
- Requires a valid DISCORD_TOKEN secret to operate
- Runs as cluster 1 with command: `python run.py 1`

## Project Architecture
- **run.py** - Entry point, launches the bot with cluster ID
- **tool/greed.py** - Main bot class (Greed extends Bot)
- **tool/important/** - Core utilities, database, subclasses, services
- **tool/managers/** - IPC, Bing search, etc.
- **tool/processing/** - File/audio/text processing
- **tool/worker/** - Task offloading (stubbed Dask replacement using asyncio thread pool)
- **cogs/** - Discord command extensions (music, economy, moderation, etc.)
- **rival/** - Inter-process communication library
- **config.py** - Configuration (uses environment variables for secrets)

## Stub Packages (local replacements for unavailable packages)
- **rival_tools/** - Provides ratelimit, lock, timeit, thread decorators
- **fast_string_match/** - Uses difflib for fuzzy string matching
- **unidecode_rs/** - Wraps unidecode package

## Environment Variables / Secrets Required
- `DISCORD_TOKEN` - Discord bot token (required)
- `RIVAL_API_KEY` - Rival API key
- `LASTFM_API_KEY` - Last.fm API key
- `LASTFM_API_SECRET` - Last.fm API secret
- `OUTAGES_API_KEY` - Outages API key

## Recent Changes
- 2026-02-18: Migrated from GitHub to Replit environment
  - Installed Python 3.12 and 50+ dependencies
  - Created stub packages for rival_tools, fast_string_match, unidecode_rs
  - Replaced Dask distributed worker with local asyncio thread pool executor
  - Moved hardcoded secrets to environment variables
  - Installed system deps: ffmpeg, cairo, imagemagick, gcc-unwrapped

## Workflow
- **Run**: `python run.py 1` (console mode)
