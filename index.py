
import cgi

import cgitb
cgitb.enable()

import platform

print "Content-Type: text/html"
print

print "<html>"
print "<head><title>Who am I?</title></head>"
print "<body>"
print "<h1>Who am I?</h1>"
print "<p>Machine: <b>{0}</b></p>".format(platform.machine())
print "</body>"
print "</html>"
