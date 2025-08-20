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
cookie_header = os.environ.get("HTTP_COOKIE", "")
cookie = http.cookies.SimpleCookie(cookie_header)
if "CGISESSID" in cookie:
    session_id = cookie["CGISESSID"].value
else:
    session_id = str(uuid.uuid4())

# Load or create session
session = load_session(session_id)

# Read form/query input
if os.environ.get("REQUEST_METHOD", "") == "POST":
    length = int(os.environ.get("CONTENT_LENGTH", 0))
    post_data = sys.stdin.read(length)
    form = parse_qs(post_data)
else:
    query = os.environ.get("QUERY_STRING", "")
    form = parse_qs(query)

name = session.get("username") or form.get("username", [None])[0]

if name:
    session["username"] = name

# Save session
save_session(session_id, session)

# Send headers (with path!)
print("Content-Type: text/html")
print(f"Set-Cookie: CGISESSID={session_id}; Path=/cgi-bin/")  # important!
print()

# HTML output
print("<html>")
print("<head><title>Python Sessions</title></head>")
print("<body>")
print("<h1>Python Sessions Page 1</h1>")
if name:
    print(f"<p><b>Name:</b> {name}</p>")
else:
    print("<p><b>Name:</b> You do not have a name set</p>")

print('<br/><br/>')
print('<a href="/cgi-bin/python-sessions-2.py">Session Page 2</a><br/>')
print('<a href="/python-cgiform.html">Python CGI Form</a><br/>')
print('<form style="margin-top:30px" action="/cgi-bin/python-destroy-session.py" method="get">')
print('<button type="submit">Destroy Session</button>')
print('</form>')
print("</body></html>")
