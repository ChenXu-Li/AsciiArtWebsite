#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# filename：test.py

# CGI处理模块
import cgi
import cgitb; cgitb.enable()
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_v1 = form.getvalue('v1')
site_v2  = form.getvalue('v2')
result = int(site_v1)+int(site_v2)

print ("Content-Type: text/html; charset=utf-8\n")

print(
'''
<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"utf-8\">
        <title>牛马</title>
    </head>
    <body>
        <form action="/cgi-bin/calculater.py" method="get">
            数1: <input type="number" name="v1" value="{0}"><br />
            数2: <input type="number" name="v2" value="{1}"><br />
            结果: <input type="number" name="re" value="{2}"><br />
            <input type="submit" value="提交" />
        </form>
    </body>
</html>
    '''.format(site_v1,site_v2,result)
)