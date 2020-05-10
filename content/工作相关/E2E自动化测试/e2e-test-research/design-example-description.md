<!--
* @UpdateTime : 2020/4/16 3:20 下午
* @description: type some description
-->
## 自动化测试项目组织结构，以PageObject设计模式
#### PageObject方式（可推广至app页面，一回事）
- PO(dir)
  - BasePage: 基础页面测试封装类，封装url，driver，以及定位元素方法
    - \_\_init__.py
    - BasePage.py
  - Page: 其他所有页面继承基础页面对象
    - \_\_init__.py
    - xxxxPage.py
    - .....
  - Common：分离测试固件，一些基础的东西是相同的，可以在这里做封装，让所有测试类来继承，或者其他lib，比如失败截图等
    - \_\_init__.py
    - helper.py(log系统)
    - testReport.py(测试报告相关,比如记录，或者以邮件发送等)
    - FixUnit.py
    - .....
  - TestCases：实际测试用例目录
    - \_\_init__.py
    - testLogin.py
    - .........
  - Data：分离测试数据，记录log信息
    - \_\_init__.py
    - otherDataFile(xls、csv、blablabla。。。。)

###### 代码demo说明
BasePage.py:
```
class HomePage:
    def __init__(self, url, driver):
        self.url = url  # 定义页面地址
        self.dr = driver    # 定义驱动
    def find_element(self, *loc):
        try：
            根据定位参数获取目标组件
        except：
            抛异常
```
这时候你的比如LoginPage就可以继承这个基类
```
class LoginPage(HomePage):
    # 继承了构造方法
    # 直接拿这个页面的定位元素即可，（所以当页面变动的时候就是改这里的属性获取方法）
    username_loc = self.find_element(By.id, 'mobilePhone')
    xxxxxxxxxxxxx
    xxxxxxx
    xxxxxx
    def openLoginPage(self):
        self.dr....
        ...
    def input_userName(self, userName):
        self.find_element(....).sendkeys(userName)
    
    
    def xxxxxxx
    
    def xxxxxx
```
然后测试的示例如下，我们可以在common做测试固件分离，所谓测试固件就是测试中不变的部分封装在一个基类里，其他测试继承，
减少代码冗余，增加复用。
```
class MyunitTests(unittest.TestCase):
    def setUp(self):
        self.url = "实际你要测得url"
        self.dr = 你需要的驱动（比如Chrome、firefox或者ie等等）
        # 把你要测试的页面放在这里
        self.loginpage = LoinPage
    def tearDown(self):
        # 在这里把驱动关闭
        self.dr.quit()
```
然后去写测试用例，使用你这个页面上定义的方法去较为轻松的构建测试流程：
```
class TestLoginPage(MyunitTests):
    def testLogin(self):
        testcode
    
    def test_username_null(self):
        testcode
    
    def test_password_null(self):
        testcode
```
然后可以构建读取测试数据的地方，就是data：
```
class DataHelper:
    def readExcels(self):
        pass
    def readCsv(self):
        pass
    def readusername(self):
        pass
    
    def readpassword(self):
        pass
    
    def readdatafromRow(self, rowx):
        pass
    
    xxxxxx
```
还可以构建失败页面截图来更清晰的定位失败，driver通常有这样的实现,  
我们可以把类似这些方法也放在common里面，比如getImage.py文件，来处理图片相关的逻辑。
```
def get_fail_Image(driver, errorImage)：
    driver.get_screenshot_as_file(picture)
```
我们再加上python自己的logging模块的使用，来标注日志记录
把相关的方法写在DataHelper的类里，比如
```
def makelog(self):
    pass
def dirname(self):
    pass
```
然后我们在测试用例里多继承去使用里面的log方法即可:
```
class TestLoginPage(MyunitTest, DataHelper):
    pass
```

最后可以在common里加入一个生成报告的文件，如testreport.py文件，把生成报告的逻辑放在里面。






