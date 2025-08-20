#!/usr/bin/env python3
import os
import http.cookies

SESSION_DIR = "/tmp"

def destroy_session(session_id):
    session_file = os.path.join(SESSION_DIR, f"session_{session_id}.pkl")
    if os.path.exists(session_file):
        os.remove(session_file)

# Get cookies
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session_id = cookie.get("CGISESSID")

if session_id:
    session_id = session_id.value
    destroy_session(session_id)

# Send headers (clear the cookie as well)
print("Content-Type: text/html")
print("Set-Cookie: CGISESSID=deleted; expires=Thu, 01 Jan 1970 00:00:00 GMT")
print()

# HTML output
print("<html>")
print("<head><title>Python Session Destroyed</title></head>")
print("<body>")
print("<h1>Session Destroyed</h1>")
print('<a href="/python-cgiform.html">Back to the Python CGI Form</a><br/>')
print('<a href="/cgi-bin/python-sessions-1.py">Back to Page 1</a><br/>')
print('<a href="/cgi-bin/python-sessions-2.py">Back to Page 2</a>')
print("</body>")
print("</html>")
