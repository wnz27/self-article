## 关闭redis-server的方法
如果你执行`redis-server`的shell窗口不小心关掉了，
看不到进程的id和port，你想关掉server重启。

1. 使用kill，输入命令`ps -ef | grep redis`看看哪个是redis-server
然后`kill -9 pid`
2. 第一种毕竟是强制的方法，不美妙，来看第二种，是正确的停止redis的姿势，
向redis发送shutdown指令：具体的做法是使用redis-cli：
`redis-cli shutdown`即可

ps：看清楚你的redis-server和redis-cli的位置。
