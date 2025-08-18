#!/usr/bin/env python3
import os
import sys

# Print HTTP headers
print("Cache-Control: no-cache")
print("Content-type: text/html\n")

# Print HTML header
print("<html><head><title>General Request Echo</title></head>")
print("<body><h1 align=center>General Request Echo</h1><hr/>")

# Protocol and Method
protocol = os.environ.get("SERVER_PROTOCOL", "Unknown")
method = os.environ.get("REQUEST_METHOD", "Unknown")

# Read message body (from stdin)
body = sys.stdin.read(1000)

# Print values in a table
print("<table>")
print(f"<tr><td>Protocol:</td><td>{protocol}</td></tr>")
print(f"<tr><td>Method:</td><td>{method}</td></tr>")
print(f"<tr><td>Message Body:</td><td>{body}</td></tr>")
print("</table>")

# Print HTML footer
print("</body></html>")
