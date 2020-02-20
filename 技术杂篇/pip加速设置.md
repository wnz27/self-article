清华的pip加速镜像站是：[https://pypi.tuna.tsinghua.edu.cn/simple](https://pypi.tuna.tsinghua.edu.cn/simple)

#### 一次性方法
可以在使用pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple

例如：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gevent，这样就会从清华这边的镜像去安装gevent库。

#### 永久修改，一劳永逸：
linux下，修改 ~/.pip/pip.conf (没有就创建一个)， 修改 index-url，内容如下：
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

##### 其他
有其他镜像的网站也可。