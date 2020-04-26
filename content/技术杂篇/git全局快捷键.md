<!--
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2020-04-14 09:04:39
 * @LastEditTime: 2020-04-14 09:05:27
 * @FilePath: /self-article/content/技术杂篇/git全局快捷键.md
 * @description: type some description
 -->
### git常用快捷键的配置全局配置
```
~/.gitconfig
```

我的快捷键是这样设置的"
```
[alias]
	st = status
	br = branch
	co = checkout
	ci = commit -v
```
也就是说我使用`git status`这个命令的时候，只用输入`git st`，其他同样的道理

#### 注意
这里给一点自己的建议，我commit 时候没有直接使用-m，而使用-v，原因是
-v可以看到你的哪些文件被你commit了，让你清楚地知道你有没有commit误操作
这个自己平常学习可能无所谓，但是做项目的话，还是很必要的。

其次commit的话会让你在vim编辑里去写附带信息，一般来说第一行就是title，
然后你空一行，第三行开始就是描述。

至于其他的一些在项目使用的技巧可以----->>[这篇文章](./项目中版本管理的git使用技巧.md)