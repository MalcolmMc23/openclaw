import sys
import json
import requests
import os
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 sync_calls.py <call_id>")
        sys.exit(1)

    call_id = sys.argv[1]

    # Load config
    config_path = os.path.expanduser("~/.config/bland/config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    
    api_key = config.get("apiKey")
    log_path = os.path.expanduser("~/memory/call-logs.jsonl")

    # Fetch call details
    url = f"https://api.bland.ai/v1/calls/{call_id}"
    headers = {"authorization": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Extract only what we need
        log_entry = {
            "timestamp": data.get("created_at"),
            "to": data.get("to"),
            "answered_by": data.get("answered_by"),
            "transcript": data.get("concatenated_transcript"),
            "call_id": call_id,
            "status": data.get("status")
        }

        # Write to memory (append)
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        with open(log_path, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        
        print(f"Logged call {call_id} to {log_path}")

    except Exception as e:
        print(f"Error syncing call: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
