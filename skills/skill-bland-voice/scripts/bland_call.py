import sys
import json
import requests
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 bland_call.py <phone_number> <task>")
        sys.exit(1)

    phone_number = sys.argv[1]
    task = sys.argv[2]

    # Load config for API key
    config_path = os.path.expanduser("~/.config/bland/config.json")
    if not os.path.exists(config_path):
        print(json.dumps({"error": "Bland API key not configured. Create ~/.config/bland/config.json"}))
        sys.exit(1)

    with open(config_path, "r") as f:
        config = json.load(f)
    
    api_key = config.get("apiKey")
    if not api_key:
        print(json.dumps({"error": "apiKey missing in config.json"}))
        sys.exit(1)

    url = "https://api.bland.ai/v1/calls"
    headers = {
        "authorization": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "phone_number": phone_number,
        "task": task,
        "reduce_latency": True
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(json.dumps(response.json()))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
