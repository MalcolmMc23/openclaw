---
name: skill-bland-voice
description: "Automate phone calls and voice-to-task workflows using Bland AI. Use when the user wants to: (1) receive urgent phone notifications, (2) make outbound AI calls to businesses or people, (3) set up an inbound number where voice notes become tasks, or (4) analyze phone call transcripts."
---

# Bland AI Voice Skill

This skill enables phone-based interactions using the Bland AI API.

## Configuration

The skill requires a Bland AI API key stored in `~/.config/bland/config.json`:

```json
{
  "apiKey": "your_bland_api_key"
}
```

## Outbound Calls

Use the `bland_call.py` script to trigger an outbound call.

```bash
python3 scripts/bland_call.py "+1234567890" "Hey, this is Milk..."
```

**Important:** After triggering a call, always schedule a one-shot cron job to run `sync_calls.py <call_id>` in 5 minutes to capture the outcome and transcript.

## Logging & Sync

Calls are logged to `memory/call-logs.jsonl`. Use `sync_calls.py` to fetch details from Bland AI:

```bash
python3 scripts/sync_calls.py <call_id>
```

## Inbound Voice Tasks

To set up an inbound tasking line:
1. Purchase/Configure a number at [bland.ai](https://www.bland.ai).
2. Point the webhook to your OpenClaw gateway (if exposed) or use a sub-agent to periodically poll `GET /v1/calls`.
3. Set the prompt for the inbound number to: "You are Milk's voice assistant. The user is calling to leave a task. Ask them what they need to get done, confirm the details, and say goodbye. Keep it brief."

## API Reference

See [references/api_docs.md](references/api_docs.md) for more details on the Bland AI API.
