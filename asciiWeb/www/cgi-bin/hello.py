#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import cgitb; cgitb.enable()
print('Content-type:text/html \n\n')
print('Hello CGI~')
print("<meta charset=\"utf-8\">")
print ("<b>环境变量</b><br>")
print ("<ul>")
for key in os.environ.keys():
    print ("<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key]))
print ("</ul>")