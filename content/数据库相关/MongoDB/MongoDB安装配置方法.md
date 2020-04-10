<!--
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2019-12-31 06:56:55
 * @LastEditTime: 2020-04-10 18:23:42
 * @FilePath: /self-article/content/数据库相关/MongoDB/MongoDB安装配置方法.md
 * @description: type some description
 -->
## 基于Mac的安装
1. 首先官网下载包，选定好自己的版本，应该是tgz格式
2. 解压缩，把**解压后的文件夹**放在自己想放的路径下，比如这个路径是A（绝对路径，如xxxx/xxxx/xxxx）
3. 可以看到这个文件夹下有个bin文件夹，里面有很多脚本，最常用的就是mongo和mongod，我们需要在这个文件夹下建立一个配置文件，命名为mongodb.config，两个方法：
- terminal中，cd到bin的目录下，touch一个配置文件(命名为上面的那个名称)，在用vi命令编辑文件
- 不管你在哪个目录下，直接在terminal中执行`vi A/bin/mongodb.config`，A是啥请看步骤2
4. 然后想让配置生效，去bin目录下，执行`mongod --config A/bin/mongodb.config`，这时候到某一行会卡住不动，这就是连接成功了
5. 打开另一个终端窗口，输入`mongo`，出现`>`输入`db.version()`，弹出版本，说明成功了

## 把bin文件加到系统路径底下
这样你在任何目录下都可以肆无忌惮的执行mongo和mongod了
1. 不管你在哪个目录，执行`cd ~`
2. 输入`open -e .bash_profile`
3. 会打开一个文件，在这个文件里这样修改：
    ![](../img/截屏2019-12-3107.24.36.png)
4. command+s保存，然后执行`source .bash_profile`
5. 然后输入命令即可，如果没有生效就重启下terminal
