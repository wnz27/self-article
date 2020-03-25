## 更新问题
如果mac上的vscode出现这个更新问题：
Could not create temporary directory: 权限被拒绝

那么打开终端执行这个指令：
`sudo chown $USER ~/Library/Caches/com.microsoft.VSCode.ShipIt/`
之后重启vscode重新检查更新即可