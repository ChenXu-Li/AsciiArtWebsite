



# ascii art web

## 简介

采用python cgi 和 nginx 搭建一个ascii艺术风格图片转换网页。

网站地址：http://ascii-art.lcx-blog.top/

## 部署在本地

在www文件夹下启动python内置服务器

` python -m http.server --cgi 8001`

`http://localhost:8001/cgi-bin/hello.py`

如果启动成功，会输出所有参数



`http://localhost:8001/index.html`

上传的图片会暂存tmp文件夹中，并交由`new_post_img.py`处理



## 部署在云服务器

1. 注册二级域名，设置dns解析地址

2. nginx端口映射，同时添加自定义404页面   http://ascii-art.lcx-blog.top/error                             

```nginx
server
{
    listen   80;
    server_name   ascii-art.lcx-blog.top;
    error_page   404    /404.html;
    
    location = /404.html {
    	root /root/asciiWeb/www/;
  	}
    location / {
        proxy_intercept_errors on;   #开启自定义404页面
        proxy_pass http://127.0.0.1:9999/;#端口映射
    }
        #默认访问index页面
}
```

   3. 在9999端口开启服务（记得把云服务商的安全策略组重新配置一下）

      ` python -m http.server --cgi 9999`

可能遇到的问题：

1.  如果报403的错，可能是python路径原因，需要在py脚本头加上python解释器的绝对路径
2.  如果报403的错，也可能是权限原因，记得把权限改成755，`chmod -R 777 asciiWeb`
3.  当产生FileNotFoundError 错误，可能是因为windows文本编辑器中的\r\n在ubuntu中无法识别，重新用vim编辑一遍就好了
