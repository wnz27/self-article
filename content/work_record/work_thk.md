<!--
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2020-04-13 22:11:05
 * @LastEditTime: 2020-04-16 01:40:30
 * @FilePath: /self-article/content/work_record/work_thk.md
 * @description: type some description
 -->
#### 2020.4.13
1、查看测试对项目代码的覆盖率
使用coverage模块

`pip install coverage`

在py文件里调用coverage：
```
import coverage
cov = coverage.Coverage()
cov.start()
# 这里执行test代码，比如testsuite或者其它unitest的测试
cov.stop()
cov.save()
# 生成html
cov.html_report()
```
这时候会在代码所在目录生成一个htmlcov的文件夹，里面存着html的报告文件

还有会生成一个`.coverage`文件，这是配置文件可以配置一些参数，如include或者omit
其中有[run] 或者 [report]的区别，我配置report指定查看哪些文件的测试覆盖率情况。

2、测试没有测到的文件，不会出现在报告里，所以一个办法是专门写一个测试文件，
把那些待查看的文件都导入，相当于过了一遍，这时候可以看到那些文件的测试覆盖情况

至于执行可以把命令放在.sh文件中，来脚本执行

#### 2020.4.14
python的.pth文件作用，把路径加入sys.path中
这种方法弊端是，如果其中某些目录有同名的文件，但是你并不想导入，很难去区分

最终解决办法
我利用绝对路径和路径底下的模块名称，拼接成导入语句形式：比如“from xxx.xx.xxx import xxx”
然后利用python系统exec来直接执行导入字符串

再次熟悉git操作，git stash的使用

git 时只用git push即可，防止push到其他分支

单一分支针对一个东西的更新，方便追踪。

zsh 的安装配置使用

#### 2020.4.15 
目标提升一下test的覆盖率，先从了解teacher，班级，学生开始

熟悉baseDocument模块，熟悉clazz模块，并且针对模块写了方法简介

补充creat_clazz的模块测试，针对这个方法的测试覆盖完全

晚上浏览自动化测试相关文章

#### 2020.4.16




