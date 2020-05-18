<!--
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2020-05-18 20:48:13
 * @LastEditTime: 2020-05-18 21:24:25
 * @FilePath: /self-article/content/工作相关/mongoengine/helperDoc.md
 * @description: type some description
--> 
#### 内嵌文档添加索引
如下结构：
```
class Cotent(EmbeddedDocument):
    meta = {
        'indexs': [
            'method'
        ]
    }
    method = StringField()
    content = StringField()

class MainBody(Document):
    meta = {
        'indexs': [
            'content.method'
        ]
    }
    state = StringField()
    content = EmbeddedDocumentField(Content, Required=True)
```
可以用点语法指定索引

#### 内嵌文档与引用文档的区别
向上面的例子，内嵌文档数据库中只会有一张表，就是MainBody的表。

而引用文档使用ReferenceField字段指定的引用文档，就是两张表了，被引用的也会是一张表。

#### 内嵌文档的查询
比如以Content的method在MainBody中查询
```
# 使用双下划线指定是内嵌文档的哪个字段
MainBody.objects(Q(content__method = 'xxxxx'))
或者也可以使用in关键字
MainBody.objects(Q(content__methon__in = ['aa', 'bb', 'cc']))
```
