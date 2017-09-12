# mark down处理
## 用到的包
1. PageDown: 使用JavaScript实现的客户端MarkDown到HTML的转换程序
2. Flask-PageDown：为Flask包装的PageDown，把PageDown集成到Flask-WTF表单中
    定义了一个PageDownField类，用在TWForms里，接口和TextAreaField一致
3. Markdown：服务器端Markdown到HTML的转换程序
4. Bleach：使用Python实现的HTML清理器? *清理器是啥...*