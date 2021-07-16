<!--
* @UpdateTime : 2021/7/16 7:45 下午
* @description: type some description
* @Author: a27
-->
## 配置
以下参数错误
celery_task_result_expires = 60 * 60
正确应该是
result_expires = 60 * 60
这样结果会缓存1小时
如果没有配置则默认最多1天

