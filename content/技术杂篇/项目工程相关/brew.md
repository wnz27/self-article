## brew 的一些（对 m1 max 好像没效果）

1、 chown: /usr/local: Operation not permitted
解决方法:
```shell
sudo chown -R $(whoami) /usr/local/*
```

2、Mac-安装Homebrew报错error: could not lock config file .git/config:
Mac-brew报错error: could not lock config file .git/config: Permission denied
```shell
sudo chgrp -R admin /usr/local
sudo chmod -R g+w /usr/local
```
可以cat一下 .git/config 有可能url 已经是了

- 
