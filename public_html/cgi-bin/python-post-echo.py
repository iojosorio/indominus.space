#!/usr/bin/env python3
import sys

print("Cache-Control: no-cache")
print("Content-type: text/html\n")

print("<html><head><title>POST Message Body</title></head>")
print("<body><h1 align=center>POST Message Body</h1><hr/>")

# Read POST data from stdin
body = sys.stdin.read()
print(f"Message Body: {body}<br/>")

print("</body></html>")
