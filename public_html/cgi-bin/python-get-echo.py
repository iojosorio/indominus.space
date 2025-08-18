#!/usr/bin/env python3
import os
import urllib.parse

# Print HTTP headers
print("Cache-Control: no-cache")
print("Content-type: text/html\n")

# HTML header
print("<html><head><title>GET query string</title></head>")
print("<body><h1 align=center>GET query string</h1><hr/>")

# Raw query string
query_string = os.environ.get("QUERY_STRING", "")
print(f"Raw query string: {query_string}<br/><br/>")

# Parse query string manually
print("<table> Formatted Query String:")
if query_string:
    params = urllib.parse.parse_qs(query_string)
    for key, values in params.items():
        for value in values:
            print(f"<tr><td>{key}:</td><td>{value}</td></tr>")
print("</table>")

# HTML footer
print("</body></html>")

