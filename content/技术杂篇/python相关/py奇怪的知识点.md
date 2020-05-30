<!--
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2020-05-31 02:49:20
 * @LastEditTime: 2020-05-31 02:51:03
 * @FilePath: /self-article/content/技术杂篇/python相关/py奇怪的知识点.md
 * @description: type some description
--> 
## 双大括号转义
python长字符串中如果要用format给字符串中的大括号赋值，
但是如果字符串中有很多大括号，但是你只想给你需要的大括号的位置赋值，
那么你就可以用双大括号来标识：`{{}}`这样长字符串中的单个大括号的位置不会被format匹配。