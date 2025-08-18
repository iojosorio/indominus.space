#!/usr/bin/env python3
import os
import cgi

# Print HTTP headers
print("Cache-Control: no-cache")
print("Content-type: text/html\n")

# Print HTML header
print("<html><head><title>GET query string</title></head>")
print("<body><h1 align=center>GET query string</h1><hr/>")

# Raw query string
query_string = os.environ.get("QUERY_STRING", "")
print(f"Raw query string: {query_string}<br/><br/>")

# Parse query string
print("<table> Formatted Query String:")
form = cgi.FieldStorage()
for key in form.keys():
    value = form.getvalue(key)
    print(f"<tr><td>{key}:</td><td>{value}</td></tr>")
print("</table>")

# Print HTML footer
print("</body></html>")
