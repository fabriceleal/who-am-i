#!/usr/bin/env python

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

displayme = [("Machine", platform.machine()), ("Platform", platform.platform()),
             ("Compiler", platform.python_compiler()), ("Implementation", platform.python_implementation()),
             ("System", "{0}; {1}".format(platform.system(), platform.release())),
             ("Python version", platform.python_version())]



for info in displayme:
    (name, value) = info
    print "<p>{0}: <b>{1}</b></p>".format(name, value)

print "</body>"
print "</html>"
