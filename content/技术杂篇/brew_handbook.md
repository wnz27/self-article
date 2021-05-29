<!--
* @UpdateTime : 2021/5/29 13:31
* @Author : 27
* @description: type some description
-->
来源[Homebrew换源和更新](https://www.jianshu.com/p/906e10bb6a21)

留下来速查，防止原链接删除

# 1.更新源
```shell script
# 替换brew.git:
$ cd "$(brew --repo)"
# 中国科大:
$ git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
# 清华大学:
$ git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git

# 替换homebrew-core.git:
$ cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
# 中国科大:
$ git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
# 清华大学:
$ git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git

# 替换homebrew-bottles:
# 中国科大:
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile
$ source ~/.bash_profile
# 清华大学:
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles' >> ~/.bash_profile
$ source ~/.bash_profile

# 应用生效:
$ brew update
```

# 2.修复源
```shell script
# 诊断Homebrew的问题:
$ brew doctor

# 重置brew.git设置:
$ cd "$(brew --repo)"
$ git fetch
$ git reset --hard origin/master

# homebrew-core.git同理:
$ cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
$ git fetch
$ git reset --hard origin/master

# 应用生效:
$ brew update  
```

# 3.重置源
```shell script
# 重置brew.git:
$ cd "$(brew --repo)"
$ git remote set-url origin https://github.com/Homebrew/brew.git

# 重置homebrew-core.git:
$ cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
$ git remote set-url origin https://github.com/Homebrew/homebrew-core.git
```




