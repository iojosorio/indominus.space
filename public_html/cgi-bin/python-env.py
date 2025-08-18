#!/usr/bin/env python3

import os

# Print HTTP header
print("Cache-Control: no-cache")
print("Content-type: text/html\n")

# Print HTML header
print("<html><head><title>Environment Variables</title></head>")
print("<body><h1 align=center>Environment Variables</h1><hr/>")

# Loop through environment variables
for key, value in os.environ.items():
    print(f"{key}={value}<br/>")

# Print HTML footer
print("</body></html>")
