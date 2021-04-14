<!--
* @UpdateTime : 2021/4/14 4:31 下午
* @description: type some description
* @Author: a27
-->
想做本地调试
前端服务启动在localhost:8081, 后端服务启动在localhost:9104
在前端.env文件中修改下面一行：
`VUE_APP_PROJECT_CONSTNAME_API=http://localhost:9104/api`
运行会有跨域问题。
因为tornado的handler里面关于跨域的请求代码是类似这样的:
```
    def set_default_headers(self):
        origin = self.request.headers.get('Origin', '')
        if 'self_host.com' in origin:
            self.set_header("Access-Control-Allow-Origin", origin)
        else:
            self.set_header("Access-Control-Allow-Origin", "*")
```
修改/etc/hosts文件：
```
127.0.0.1       local.self_host.com
```
之后访问和请求没问题
发现登陆成功后设置cookie不成功，初步感觉可能是samesite问题，相关链接：[Cookie 的 SameSite 属性](http://www.ruanyifeng.com/blog/2019/09/cookie-samesite.html)
暂时未解决, 暂搁置
