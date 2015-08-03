#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
name=form.getvalue("name")


print"Content-Type: text/html"
print
print" <title>CGI script output</title> "
print" <h1>This is my first CGI script</h1> "
print("hello, " + name)
