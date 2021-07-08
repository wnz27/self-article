# 把本机文件copy 到docker
1、查看容器
``` docker ps -a ```
2、确定容器名，拿容器名获取容器ID
``` docker inspect -f '{{.ID}}' 上一步看到的容器名 ```
3、copy 本地文件到容器
docker cp 本地文件路径 上一步拿到的容器ID:docker容器里面的路径



