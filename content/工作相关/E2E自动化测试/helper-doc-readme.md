<!--
* @UpdateTime : 2020/4/17 12:29 下午
* @description: type some description
-->
## 下载驱动
Selenium需要浏览器的驱动来模拟和浏览器的交互。  
比如火狐用就是geckodriver，但是要放在环境路径里，可以统一放在/usr/local/bin，其他驱动一样，都要放在bin目录里。
否则应该会收到如下错误：
```  
errorselenium.common.exceptions.WebDriverException: Message:
‘geckodriver’ executable needs to be in PATH. 
```  
驱动的下载：
- [chrome，需要科学上网](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- [Firefox](https://github.com/mozilla/geckodriver/releases)
- [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

## 安装selenium
```
pip install selenium
```

## 使用selenium
初始化不同驱动的方法：
```
from selenium import webdriver
driver = webdriver.Chrome()
driver = webdriver.Safari()
driver = webdriver.Firefox()
```
#### 弹出与退出浏览器
```
driver.get(url)  # 会以驱动的浏览器弹出url的页面
driver.quit() # 会关闭弹出的浏览器
```
#### 使用id定位：
```
driver.find_element_by_id("kw").send_keys("helios威武")
```
send_keys是这个组件可以接收值得话往这个页面元素传值，比如输入框
#### 使用name定位
```
driver.find_element_by_name("kw").send_keys("helios威武")
```
#### 使用classname定位
```
driver.find_element_by_class_name("kw").send_keys("helios威武")
```
#### 使用xpath定位
[xpath语法教程](https://www.w3school.com.cn/xpath/xpath_syntax.asp)
```
driver.find_element_by_xpath("//input[@id='kw']").send_keys("helios威武")
```
#### 使用css选择器定位元素
id属性简写为"#"，class属性简写为"."，form#form表示form标签下id属性为form的元素。
层级关系用">"表示，span>input表示span标签下的input标签。有时为了简洁，也可以不写">"，
直接写成form#form span input
```
driver.find_element_by_css_selector("input#kw").send_keys("k总一个娃")
driver.find_element_by_css_selector("form#form>span>input").send_keys("磊哥两个娃")
```
这里有一个问题就是如果classname本身中间有空格，以上的为了简洁的办法就成了副作用，无法定位。
可以用这样的办法：`driver.find_element_by_css_selector("[class='j-inputtext dlemail']").send_keys("helios略略略")`
也可以在测试环境启动前后端项目之后
#### 多元素定位
比如有这样一个html
```
<div>
    <input type="checkbox" id="c1">
</div>
<div>
    <input type="checkbox" id="c2">
</div>
<div>
    <input type="checkbox" id="c3">
</div>
```
当我们使用如下语句定位input输入框时：
```
driver.find_elements_by_css_selector("input[type='checkbox']")[0].click()
```
三个相同的input标签，他们的type属性是一样的，用selector定位的时候会返回一个列表。
我们可以通过下标访问到具体的某个input。
### 使用By类定位
先导入By类。元素定位中的id、name、xpath、class、link_text和css分别在By类定位的语法是：
By.ID、By.NAME、By.XPATH、By.CLASS_NAME、By.LINK_TEXT和By.CSS_SELECTOR，示例如下：
```
from selenium import webdriver
from selenium.webdriver.common.by import By     # 导入 By类
driver = webdriver.Chrome()
deriver.get("https://www.baidu.com")
driver.find_element(By.ID, 'kw').send_keys("我们没有娃")
driver.find_element(By.ID, 'su').click()  # 在定位到的元素上执行点击
```
### 使用js定位
原理是拼装js语句来执行，使用js的dom的语句，比如getElementsByClassName(),
getElementByID(), getElementsByName(), getElementsByTagName(), 
document.querySelectorAll()等，除了ByID方法返回单个element元素之外，其他定位方式返回的都是列表。
```
from selenium import webdriver
import time as t
dr = webdriver.Chrome()
dr.get("https://www.jianshu.com/sign_in")
t.sleep(2)
js_register = 'document.getElementById("js-sign-up-btn").click();'
dr.execute_script(js_register)
t.sleep(2)
```
其他操作类似，如需要可以自行查文档

### 拿到find到的元素中的值
比如：
```
one_el = dr.find_element(By.ID, 'xxxx')
# 这个页面元素里面放的值就是：
one_el.text
这样就可以拿到里面的数据，基本列表元素常用这个方法。
```



## 下拉框操作
定位下拉框控件，首先要引用Select类，该类提供了三种方式，即，value，text和index。
#### value属性定位
如果html有如下样子：
```
<select id="hId">
    <optinon value="o1" id="id1">o1</option>
    <optinon value="o2" id="id2">o2</option>
    <optinon value="o3" id="id3">o3</option>
</select>
```
定位如下：
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
dr = webdriver.Chrome()
dr.get(url)
element = dr.find_element(By.ID,"hId")
Select(element).select_by_value("o1")
```
这就捕捉到了value值为o1的元素
#### index属性定位
通过select类下的index方法来定位下拉框中的值，
```
element = dr.find_element(By.ID, "hId")
Select(element).select_by_index(1)
```
select_by_index(1)表示定位到第二个option标签，索引从0开始
#### visible_text属性定位
这个文本属性通过获取元素本省的文本描述来哦定位的。
```
element = dr.find_element(By.ID, "hId")
Slect(element).select_by_visible_text("o3")
```

## parameterized参数化使用
```
from parameterized import parameterized
@parameterized.expand([('', '', '请输入账号'), 
                       ('admin111@baidu.com', '', '请输入账号密码'), 
                       ('', 'a123456789', '请输入账号密码')])
def test_login(self, usernamem, passward, assert_text):
    # 登录系统
    self.driver.get(self.url)
    sleep(3)
    self.baidulogin(username, password)
    self.assertEqual(self.getassertText(), assert_text)
```
这就是会把列表里元组参数依次放到方法里执行测试，也许未来会引入一次载入数据量大的问题，目前感觉不会有这种困扰，
但是还是把用生成器或者迭代器载入数据列为未来可优化的点。

## 其他api小示例
比如涉及时间选择器还需要查询一下。
暂无，后续如必要要在此补充，先搭主要的框架

## API简单使用示例
[【selenium定位简单使用案例】](./demo-test.py)

## 常用UI测试流程
[Demo里流程设计](pageObject/concrete_page/demoLoginPage.py)
[base_page抽象](pageObject/base_page/basePage.py)
[base_test_unit](pageObject/common/BaseTestUnit.py)
### 登录页面
- 获取驱动
- 登录测试url
- 输入用户名
- 输入密码
- 输入其他（如果有，比如验证信息获取模拟）
- 点击登录
#### 测试用例，这个可以使用parameterized参数化绑定方法
用户名为空，返回结果预期对比
密码为空，返回结果预期对比
验证码为空，返回结果预期对比
都不空返回结果预期对比。



