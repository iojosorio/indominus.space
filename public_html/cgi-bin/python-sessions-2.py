#!/usr/bin/env python3
import os
import http.cookies
import pickle

SESSION_DIR = "/tmp"

def load_session(session_id):
    session_file = f"{SESSION_DIR}/session_{session_id}.pkl"
    if os.path.exists(session_file):
        with open(session_file, "rb") as f:
            return pickle.load(f)
    return {}

# Read cookies
cookie_header = os.environ.get("HTTP_COOKIE", "")
cookie = http.cookies.SimpleCookie(cookie_header)
if "CGISESSID" in cookie:
    session_id = cookie["CGISESSID"].value
    session = load_session(session_id)
else:
    session = {}
    session_id = None  # no session yet

# Access stored data
name = session.get("username")

# Send headers
print("Content-Type: text/html")
if session_id:
    # Keep the session cookie alive
    print(f"Set-Cookie: CGISESSID={session_id}; Path=/cgi-bin/")
print()

# HTML Output
print("<html>")
print("<head><title>Python Sessions</title></head>")
print("<body>")
print("<h1>Python Sessions Page 2</h1>")

if name:
    print(f"<p><b>Name:</b> {name}</p>")
else:
    print("<p><b>Name:</b> You do not have a name set</p>")

print("<br/><br/>")
print('<a href="/cgi-bin/python-sessions-1.py">Session Page 1</a><br/>')
print('<a href="/python-cgiform.html">Python CGI Form</a><br/>')

print('<form style="margin-top:30px" action="/cgi-bin/python-destroy-session.py" method="get">')
print('<button type="submit">Destroy Session</button>')
print('</form>')
print("</body></html>")
