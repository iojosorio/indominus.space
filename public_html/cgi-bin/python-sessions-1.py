#!/usr/bin/env python3
import os
import http.cookies
import uuid
import pickle
import sys
from urllib.parse import parse_qs

SESSION_DIR = "/tmp"

def load_session(session_id):
    session_file = os.path.join(SESSION_DIR, f"session_{session_id}.pkl")
    if os.path.exists(session_file):
        with open(session_file, "rb") as f:
            return pickle.load(f)
    return {}

def save_session(session_id, session_data):
    session_file = os.path.join(SESSION_DIR, f"session_{session_id}.pkl")
    with open(session_file, "wb") as f:
        pickle.dump(session_data, f)

# Read cookies
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session_id = cookie.get("CGISESSID")

if session_id:
    session_id = session_id.value
else:
    session_id = str(uuid.uuid4())

# Load or create session
session = load_session(session_id)

# Read form/query input
if os.environ.get("REQUEST_METHOD", "") == "POST":
    length = int(os.environ.get("CONTENT_LENGTH", 0))
    post_data_
