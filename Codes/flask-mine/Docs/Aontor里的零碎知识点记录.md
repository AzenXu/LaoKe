# 东东们
app\_context_processor：上下文处理器，flask概念，可以让所有自定义变量在模板中可见

1. 作为装饰器修饰的一个函数
2. 函数返回的结果必须是dict，key在所有模板中可见
3. 前面的修饰器指定了哪些模板下可见

定义示例
```
@main.app_context_processor  
def admin_email():  
    email='879651072@qq.com'  
    return dict(email='879651072@qq.com') 
```
使用示例
```
管理员邮箱:<a href="mailto:{{email}}">{{email}}</a>  
```
