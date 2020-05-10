<!--
* @UpdateTime : 2020/4/16 10:06 上午
* @description: 自动化测试调研思考
-->
## 需求分析
- 需求不会频繁变更
- 界面相对稳定
- 某些手工测试点或者流程先加入
- 验证频繁使用的功能（可以看到api调用统计来做优先级？）
- 测试种类
  - 性能测试？
  - 并发测试？
## 测试方案
 - 语言
 - 架构
 - 项目自身情况
  - 测试案例非常多的情况下的测试
  - 测试数据如何管理
  - 测试服务器？
## 测试环境
- CI环境
- 版本管理
## 测试架构
- 测试量增多的考虑
- 测试数据管理（会不会有变化？比如界面或需求变动的时候）
- 配置文件组织
- 日志文件管理
## 测试用例执行
- 测试报告
- 测试与提交关联
- 跑测试时间

## 测试框架选用
#### 各种工具
- selenium3，代码实现
- Robot Framework，有个自己的界面RIDE
- Appium，有各种模拟手势的方法，与获取网页的组件定位相比复杂度稍微高一些，但是语法也不难懂。
- jenkins
- Allure 测试报告框架，需要结合pytest

#### 简单思考
1、项目中增加的话selenium3更为合适，架构比较好理解，更改跟增加相对容易。

2、RobotFramework，手工测试可以加入使用这个界面工具，感觉会比单纯手工物理设备效率更高。  
代码实现可能学习成本相对selenium较高，感觉更加抽象一些。

3、Appium做app的e2e测试感觉没有什么问题，稍微比selenium更加复杂一些，使用上语法差不多。

#### 个人方案倾向
Selenium3(做各种浏览器) + Appium（做ios和安卓） + jenkins（自动化集成) 

**测试报告**的话我不太确定自己直接用httpTestRunner是不是更方便，没看过Allure的细节，  
个人觉得这个httpTestRunner貌似用起来也不难，可以不引入Allure和pytest。 

但是jenkins好像可以方便的集成allure，所以影响不大。

#### 代码场景下应对UI变化的测试设计办法
[Example-Demo-Demonstrate（selenium3）](design-example-description.md)

#### 建议
希望leader浏览一下RobotFramework，个人觉得有些抽象，可能会比selenium的学习成本高一些。

