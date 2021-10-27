## JWT（JSON Web Token）认证，[官方文档学习总结](https://jwt.io/introduction/)

### 什么是JWT？

JSON Web Token（JWT）是一个开放标准（RFC 7519），它定义了一种紧凑且自包含的方式，
用于在各方之间安全地将信息作为JSON对象传输。
由于此信息是经过数字签名的，因此可以被验证和信任。
可以使用两种方法进行签名：
* 秘钥（如使用HMAC算法）签名
* RSA或ECDSA的公共/私有密钥对对JWT进行签名。

签名的令牌可以验证其中包含的声明的完整性，同时将这些声明隐藏在其他方的面前。
当使用公钥/私钥对对令牌进行签名时，签名还证明只有持有私钥的一方才是对其进行签名的一方。

### 什么时候应该使用JWT？
这些场景下JWT较为有用：
* 授权（Authorization）：这是使用JWT最广泛的场景。一旦一个用户登录进来，
那么随后的请求都会带着jwt的token，通过这个token，就允许用户访问服务器的路由、
服务、资源。单一登录是现在广泛使用的一项功能，它开销小，并且可以简单的在不同域使用。
* 信息交换（Infomation Exchange）：JWT是一个在不同部分之间安全传输信息的很好的方法。
因为它能进行签名，比如当使用秘钥对时，你可以知道它是不是它自己说的那个身份。
同时，签名是通过header和payload计算出来的，你也可以确认内容是否被篡改过。

### JSON Web Token的结构是什么样的？
是一个简洁紧凑的格式，通过`.`分割三个部分：
* Header
* Payload
* Signature

看起来就像下面这个样子：
```
xxxxx.yyyyy.zzzzz
```
分解来看各个部分
#### Header
JWT的头部通常包含这两个部分：token的类型，是JWT，
和生成签名的算法，如 HMAC SHA256 或者 RSA。

比如：
```
{
  "alg": "HS256",
  "typ": "JWT"
}
```
然后，这个json基于Base64Url编码成JWT格式的第一部分。

#### Payload
第二个部分是有效负载（payload），包含声明。
声明是有关实体（通常是用户）和其他数据的声明，有三种类型的声明：
注册声明、公共声明、私人声明。

* 注册声明：是一组非强制的但是建议使用的预定义声明，用来提供有用的可交互操作的声明。
其中有：iss(发布者)，exp（过期时间），sub（主题），aud（受众），和[其他一些](https://tools.ietf.org/html/rfc7519#section-4.1)。
> 注意：声明名称都是3个字符！！！！因为JWT是紧凑或者说简洁的。
* 公共声明：这个可以由使用JWT的人员随意定义。 但是为避免冲突，应在[IANA JSON Web令牌注册表](https://www.iana.org/assignments/jwt/jwt.xhtml)
中定义它们，或将其定义为包含抗冲突名称空间的URI（统一资源表示符）。
* 私人声明：这是自定义声明，目的是为了在同意使用它们的各方之间共享信息，既不是注册声明也不是公共声明。

一个有效负载示例如下：
```
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
```
然后，有效负载基于Base64Url编码为JWT格式的第二个部分。

>请注意，对于已签名的令牌，此信息尽管可以防止篡改，但任何人都可以读取。 
>除非将其加密，否则请勿将重要私人或机密信息放入JWT的有效负载或报头元素中。

#### Signature
创建签名部分需要提供编码的header和payload，一个加密方法，是header指出的那个算法，
来生成签名。
比如，如果你希望使用HMAC SHA256 算法，那么签名将通过以下方式创建：
```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```
签名用于验证消息在此过程中没有更改。
对于使用私钥进行签名的token，它还可以验证JWT的发送者是它所说的真实身份。

### 合起来解释
这个输出是三个由`.`分开的Base64-URL字符串，它们可以容易的在HTML和HTTP环境下传递。
同时与基于XML-based标准的如SAML相比也是更简洁的。
下面展示的就是之前的header和payload编码的JWT，它们是靠加密算法生成的签名。
![encoded-jwt](./img/encoded-jwt3.png)

如果你想在实际中使用这些概念，你可以使用[jwt.io Debugger](https://jwt.io/)来解码，
验证或者生成JWT。
![legacy-app-auth-5](./img/legacy-app-auth-5.png)




