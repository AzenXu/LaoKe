# mark down处理
## 用到的包
1. PageDown: 使用JavaScript实现的客户端MarkDown到HTML的转换程序
2. Flask-PageDown：为Flask包装的PageDown，把PageDown集成到Flask-WTF表单中
    定义了一个PageDownField类，用在TWForms里，接口和TextAreaField一致
3. Markdown：服务器端Markdown到HTML的转换程序
4. Bleach：使用Python实现的HTML清理器? *清理器是啥...*

## 11.4.1说明
11.4.1的作用是在markdown文本框中可以看到markdown的效果

但是，点击提交之后，发送的POST请求还是纯文本，并不是被渲染成的HTML

直接发送HTML是有安全隐患的，解决方案：
1. 我们只提交Markdown源文本
2. 在服务器上使用Markdown将其转换为HTML
3. 使用Bleach这个包，对HTML进行清洗，确保其中只包含几个允许使用的HTML标签
4. 我们在创建文章的时候，将其转为HTML，并存在Post的一个字段里