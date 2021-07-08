<!--
* @UpdateTime : 2021/7/9 00:35
* @Author : 27
* @description: type some description
-->
## wget
wget 出现该类问题时：
```shell script
ERROR: The certificate of ‘xxx’ is not trusted.
ERROR: The certificate of ‘xxx’ was signed using an insecure algorithm.
```
如不介意可以使用以下参数
```shell script
--no-check-certificate
```

## yum
yum 安装好的某些应用在默`./configure`时如果出现了非期望的行为，可能往往是
你的linux少了某些依赖~可以先从这入手

