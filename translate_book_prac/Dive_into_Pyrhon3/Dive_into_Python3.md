# Dive into Python3      |         《深入python3》

首先这本书是免费的并且作者授权了可以进行任何自由使用，[授权声明](https://creativecommons.org/licenses/by-sa/3.0/deed.zh)

英文的原版链接在这，[Dive into Python3](http://diveinto.org/python3/index.html)

## -1、这本书有哪些新特性
先略，先把主要内容搞定

## 0、安装python
这章我就略过了，主要内容如果我不幸翻译完也一样不啰嗦了~~~~~~

## 1、你的第一个Python程序
### 1.1 深入进去
传统的叙述就是我应该跟你念叨一些基础的编程的代码块，让我们可以逐步的构建一些有用的东西。让我们跳过这些，这是一个完整的可以运行的pyhton程序。
它也许会让你不能完全理解。不用担心，因为你将要逐行的分析它，如果可以的话，看看你能做些什么！

【文件名：humansize.py】
```
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
```

现在让我们在命令行执行这个程序。在windows，它应该看起来是这样的：
```
c:\home\diveintopython3\examples> c:\python31\python.exe humansize.py
1.0 TB
931.3 GiB
```
在Mac OS X 或者 Linux下执行，应该看起来是这样的：
```
you@localhost:~/diveintopython3/examples$ python3 humansize.py
1.0 TB
931.3 GiB
```

发生了什么呢？你执行了你第一个python程序，你在命令行调用了pyhton的解释器，然后你给pyhton传递了你希望它执行的脚本的名字。
这个脚本定义了一个单一的函数，`approximate_size()`,这个函数接收一个以比特（字节）为单位的确切的文件大小，计算出一个“漂亮”（但大约）的大小。

（你可能在windows的资源管理器，或者Mac OS X访达，或者Ubuntu里的Nautilus或者海豚或者运行于linux和类unix平台的Thunar文件管理器，如果你用多行
列表的形式去展示文件夹的文件，他会用一个表来显示文件图标，文件名称，大小，类型，最后修改时间等等。如果文件夹包含一个1093字节的名为TODO的文件，那么
你的文件管理器不会显示TODO 1093bytes，而是会显示TODO 1KB，这就是`approximate_size()`函数所做的事情）

看看这个脚本的最下面，你将会看到打印两次调用这个函数。这些就是函数调用，一次调用传递一些参数，然后把函数返回值直接传递给`print()`函数。

`print()`函数是Python内置的；你绝对不会看到任何一个对它的明确的声明。你就是可以使用它，任何时间，任何地点，只要小爷喜欢。
（这有非常多的内置函数，还有更多函数分开在不同的模块。Patiencce， grasshopper）

所以为什么每次在命令行运行这个脚本都会给你相同的输出？我们会做到这点。首先让我们看看`approximate_size()`这个函数
### 1.2 函数声明
侧边贴士：当你需要一个函数，声明它就可以了。

Python像其它很多语言一样有很多函数，但是它不像C++有分离的头文件或者不想Pascal有接口/执行这样部分的区分。
当你需要一个函数，声明它就可以了。就像这样：
`def approximate_size(size, a_kilobyte_is_1024_bytes=True):`

函数声明需要以`def`为关键字作为声明的开始，紧接着就是函数名称，后面跟着带圆括号的参数。多个参数用逗号分开。

也要注意这个函数没有定义返回的数据类型。Python的函数都不会给他们的返回值特别的指定数据类型；它们甚至都不会去管返回的是不是一个值。
（事实上，每个Python函数都返回一个值；如果这个函数已经执行了返回语句，它都将会返回那个值，除非它返回None，Python的空值。）
> 在一些语言里，有返回值的函数一般以function开头，没有返回值的子程序一般以sub开头。在Python里没有子程序这种说法。所有都是叫函数，所有函数都返回值，即使是None，而且所有的函数都以def开头

`approximate_size()`函数需要两个参数`size`和`a_kilobyte_is_1024_bytes`，但是没有一个参数明确的指定了数据类型。在Pyhton里，
变量绝对不需要明确类型。Python会明白一个变量的类型还有会保持追踪每一个变量的本质。

> 在Java或者其他的一些静态语言，你必须声明函数返回值以及参数的数据类型。在Python里，你绝对不需要明确给任何东西声明数据类型。在你分配的值的基础上，Python会保持对它内在的数据类型的追踪。

#### 1.2.1 可选参数和参数命名
Python允许函数参数有它的默认值；如果函数调用的时候没有提供参数，那么这些参数会获得它们的默认值。更进一步说，使用名字参数的时候，它们可以用任意的顺序指定。

让我们再来看一下`approximate_size()`函数的声明：
`def approximate_size(size, a_kilobyte_is_1024_bytes=True):`

第二个参数`a_kilobyte_is_1024_bytes`，明确指定了一个默认值是True。这样的意思就是这个参数是可选的，在你调用函数的时候可以不需要提供这个参数，
在python执行函数的时候就好像你提供了一个True作为第二个参数一样。

现在让我们看看脚本的最后两行：
```
if __name__ == '__main__':
    print(approximate_size(1000000000000, False))  ①
    print(approximate_size(1000000000000))         ②
```
①  调用这个函数的时候传递了两个参数，。所以在函数里面`a_kilobyte_is_1024_bytes`的值将会是False，因为明确的把False作为第二个参数传递进去

②  调用这个函数的时候仅仅传递了一个参数。但是这是完全ojbk的，因为第二个参数是可选的！因为调用者没有明确参数，所以第二个参数默认是True，就像函数声明的定义一样。

你可以通过名称给函数传值：
```
>>> from humansize import approximate_size
>>> approximate_size(4000, a_kilobyte_is_1024_bytes=False)       ①
'4.0 KB'
>>> approximate_size(size=4000, a_kilobyte_is_1024_bytes=False)  ②
'4.0 KB'
>>> approximate_size(a_kilobyte_is_1024_bytes=False, size=4000)  ③
'4.0 KB'
>>> approximate_size(a_kilobyte_is_1024_bytes=False, 4000)       ④
  File "<stdin>", line 1
SyntaxError: non-keyword arg after keyword arg
>>> approximate_size(size=4000, False)                           ⑤
  File "<stdin>", line 1
SyntaxError: non-keyword arg after keyword arg
```

①	这个调用用4000作为第一个参数，而False用了名称传递

②	这个调用两个参数都是用名称调用的 （这两个名称调用的顺序与函数声明里是一样的）

③	这两个参数也都是用名称调用的 但是顺序与函数声明里不一样，也可以函数调用成功

④	这个函数调用失败了，因为你使用了名称调用，然后跟了一个位置参数（非名称调用），它没有成功。函数读取参数列表是从左至右的，当参数顺序变了（我自己加的一句话），一旦你使用了一个名称调用，那么另一个参数也必须使用名称来调用

⑤	这个调用也失败了，原因和上一个调用时一样的。惊喜吗老铁？4000你用名称调用，那么显然False就应该是`a_kilobyte_is_1024_bytes`参数的值。但是Python并不能成功运行，一旦你使用了一个名称调用，（上面我已经提到函数读取参数列表是从左至右的），那么位于这个参数**右边**的所有参数也都要使用名称调用

### 1.3 书写具有可读性的代码
