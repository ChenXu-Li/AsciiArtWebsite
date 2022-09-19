# AsciiArtWebsite
python+cgi, simple photo to ascii-art web


**通用网关接口** (英语：Common Gateway Interface，CGI) 是为提供网络服务而执行控制台应用 (或称[命令行界面](https://zh.wikipedia.org/wiki/命令行界面)）的程序，提供于服务器上实现[动态网页](https://zh.wikipedia.org/wiki/動態網頁)的通用协议。通常情况下，一次请求对应一个CGI 脚本的执行，生成一个 HTML。[[1\]](https://zh.wikipedia.org/wiki/通用网关接口#cite_note-rfc-3875-1)

简而言之，一个 HTTP POST 请求，从客户端经由 [标准输入](https://zh.wikipedia.org/wiki/标准输入) 发送数据到一个CGI 程序。同时携带其他数据，例如 URL 路径, [HTTP头字段](https://zh.wikipedia.org/wiki/HTTP头字段)数据，被转换为进程的环境变量。

![image-20220905222720135](http://cdn.lcx-blog.top/img/image-20220905222720135.png)

## 简单上手

1. 先在本机上跑一个hello world

   在www文件夹下启动python内置服务器

   ` python -m http.server --cgi 8001`

   ``http://localhost:8001/cgi-bin/hello.py`

   [详情参考](https://zhuanlan.zhihu.com/p/165953436)

2. 写个get处理脚本，直接访问能否正常运行

   `http://localhost:8001/cgi-bin/hello_get.py?name=namename&url=oneurl`

3. 通过html向服务器发送get

   `http://localhost:8001/test_get.html`

4. 实现一个加法器

   `http://localhost:8001/test_calculater.html`

   [详情参考](https://blog.csdn.net/zhyh1435589631/article/details/51530926)

5. 使用post,试试上传图片

   `http://localhost:8001/test_postimg.html`

   [详情参考](https://www.tutorialspoint.com/python3/python_cgi_programming.htm)

6. 部署到服务器，端口为

   ` python -m http.server --cgi 9999`

   如果报403的错，可能是python路径原因：https://www.cnblogs.com/sfriend/p/10451453.html

   也可能是脚本或者存储目录的权限问题：https://blog.csdn.net/jiangbo_hit/article/details/5117801

   以root身份启动端口服务程序也会有权限问题https://zhuaxia.xyz/detail/29348

   `chmod -R 777 asciiWeb`

   `http://101.133.154.72:9999/cgi-bin/hello.py`

   `http://101.133.154.72:9999/test_calculater.html`

   `http://101.133.154.72:9999/cgi-bin/hello.py`

   `http://101.133.154.72:9999/test_postimg.html`

```
Exception happened during processing of request from ('124.119.151.27', 6162)
Traceback (most recent call last):
  File "/usr/lib/python3.8/http/server.py", line 1179, in run_cgi
    os.execve(scriptfile, args, env)  
PermissionError: [Errno 13] Permission denied: '/root/asciiWeb/www/cgi-bin/hello.py'
----------------------------------------
124.119.151.27 - - [19/Sep/2022 02:02:24] CGI script exit status 0x7f00

```

可以看到`os.execve(scriptfile, args, env) `以root权限启动端口服务，但是网络服务一般以nobody身份访问

![image-20220920000144579](http://cdn.lcx-blog.top/img/image-20220920000144579.png)

```
root@iZuf60im9c3c7g0yyw4liyZ:~/asciiWeb/www# python3 -m http.server --cgi 9999
Serving HTTP on 0.0.0.0 port 9999 (http://0.0.0.0:9999/) ...
124.119.151.27 - - [19/Sep/2022 23:04:00] "GET /cgi-bin/hello_get.py?name=qq&url=ww HTTP/1.1" 200 -
----------------------------------------
Exception happened during processing of request from ('124.119.151.27', 5774)
Traceback (most recent call last):
  File "/usr/lib/python3.8/http/server.py", line 1179, in run_cgi
    os.execve(scriptfile, args, env)
FileNotFoundError: [Errno 2] No such file or directory: '/root/asciiWeb/www/cgi-bin/hello_get.py'
----------------------------------------
124.119.151.27 - - [19/Sep/2022 23:04:00] CGI script exit status 0x7f00
^C
Keyboard interrupt received, exiting.
root@iZuf60im9c3c7g0yyw4liyZ:~/asciiWeb/www# cd /root/asciiWeb/www/cgi-bin/
root@iZuf60im9c3c7g0yyw4liyZ:~/asciiWeb/www/cgi-bin# ls
calculater.py  execute_img.py  hello_get.py  hello.py  helloworld.py  post_img.py  __pycache__


```

not found 的错误原因

python 版本号问题https://stackoverflow.com/questions/55178391/filenotfounderror-errno-2-cgi-python3

也可能是编码问题https://blog.csdn.net/complay_ly/article/details/105147104













> 
