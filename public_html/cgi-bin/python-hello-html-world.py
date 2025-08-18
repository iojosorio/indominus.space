#!/usr/bin/env python3
import os
import time

# Print HTTP headers
print("Cache-Control: no-cache")
print("Content-type: text/html\n")

# Print HTML header
print("<html><head><title>Hello CGI World</title></head>")
print("<body><h1 align=center>Hello HTML World</h1><hr/>")

# Body content
print("Hello World<br/>")
print(f"This program was generated at: {time.ctime()}<br/>")
print(f"Your current IP address is: {os.environ.get('REMOTE_ADDR', 'Unknown')}<br/>")

# Print HTML footer
print("</body></html>")
