# Bland AI API Reference

Base URL: `https://api.bland.ai`

## Send Call
`POST /v1/calls`

Payload:
- `phone_number`: string (required)
- `task`: string (required) - Instructions for the AI caller.
- `voice`: string (optional) - Voice ID to use.
- `first_sentence`: string (optional) - What the AI says first.
- `wait_for_greeting`: boolean (optional)
- `tools`: array (optional) - Custom tools for the AI to use.

## Get Call Details
`GET /v1/calls/:call_id`

## Inbound Numbers
`GET /v1/inbound` - List numbers.
`POST /v1/inbound/:number_id` - Update number config (webhook, task, etc).

## Webhooks
Bland sends call events to your configured webhook URL.
Useful for processing "task by voice" results.
