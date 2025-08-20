#!/usr/bin/env python3
import os
import cgi
import http.cookies
import uuid
import pickle

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

# Get cookies
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session_id = cookie.get("CGISESSID")

if session_id:
    session_id = session_id.value
else:
    session_id = str(uuid.uuid4())

# Load or create session
session = load_session(session_id)

# Get form input
form = cgi.FieldStorage()
name = session.get("username") or form.getfirst("username", None)

if name:
    session["username"] = name

# Save session back
save_session(session_id, session)

# Send headers
print("Content-Type: text/html")
print(f"Set-Cookie: CGISESSID={session_id}")
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

print("<br/><br/>")
print('<a href="/cgi-bin/python-sessions-2.py">Session Page 2</a><br/>')
print('<a href="/python-cgiform.html">Python CGI Form</a><br/>')

print('<form style="margin-top:30px" action="/cgi-bin/python-destroy-session.py" method="get">')
print('<button type="submit">Destroy Session</button>')
print('</form>')

print("</body></html>")
