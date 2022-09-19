#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：test.py

# CGI处理模块
import cgi
import cgitb; cgitb.enable()
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_name = form.getvalue('name')
site_url  = form.getvalue('url')


print ("Content-Type: text/html; charset=utf-8 \n")
print ("<html>")
print ("<head>")
print ("<meta charset=\"UTF-8\">")
print ("<title>菜鸟教程 CGI 测试实例</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s官网：%s</h2>" % (site_name, site_url))
print ("<h2> aaabbb你好 </h2>" )

print ("</body>")
print ("</html>")