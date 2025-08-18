#!/usr/bin/env python3
import os
import time
import json

# Headers
print("Cache-Control: no-cache")
print("Content-type: application/json\n")

# Build JSON response
response = {
    "message": "Hello World",
    "date": time.ctime(),
    "currentIP": os.environ.get("REMOTE_ADDR", "Unknown")
}

# Output JSON
print(json.dumps(response))
