#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import execute_img
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

text_img="qweasdzxc"

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('tmp/' + fn, 'wb').write(fileitem.file.read())
   #open('D:\\justplay\\asciiweb\\www\\tmp\\' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'
   text_img = execute_img.exe_img('tmp/' + fn)
else:
   message = 'No file was uploaded'
print('Content-type:text/html \n\n')#\n\n很重要
print(

'''
<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"utf-8\">
        <title>img</title>
    </head>
    <body>
        <p>{0}</p>     
        <p>{1}</p>  
        
        <textarea name="description">{2}</textarea>
    
        <tt style="line-height:0;background-color: pink;"></tt>
   
    </body>
</html>
    '''.format(message,fn,text_img)
)

