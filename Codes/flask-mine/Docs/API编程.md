# 第14章 - API编程
> 这种形式其实才是客户端最熟悉的形式。

其实分析下，之前访问接口，返回的是渲染好的HTML文件
 - 路由函数（controller）先从数据库里捞model
 - 然后CURD
 - 然后做成viewMode（Form）
 - 然后丢给模板（View）渲染成HTML，View有事件产生，则通过重定向的方式将事件回传给controller
 
API和HTML区别在于：
1. 渲染的「模板」不一样 - 之前需要模板渲染成HTML，现在需要的是JSON
2. 请求参数不一样 - 以前POST请求直接把整个HTML都塞在请求体里了，所以viewModel是可以直接从请求里获取到，但是API的话，不可能直接得到viewModel - 当然也不需要ViewModel了嘛，因为都木有view了，要viewModel干啥...
3. 可以通过请求参数的形式判断状态，不过这样在设计接口的时候一定要把需要的参数注明才行
4. 版本 - 以前由客户端完全控制版本，现在API对接的应用版本多种多样，所以肯定需要考虑版本兼容问题 - 方案是使用版本区分客户端访问的资源 /api/v1/posts/

然后，不瞎猜了，看书~

## 笔记
### RIA架构 - Rich Internet Application
- 背景：业务逻辑被越来越多的移到了客户端一侧
- 服务器的主要功能（有的时候是唯一功能），是为客户端提供数据存取服务
- 服务器变成了Web服务或应用编程接口（API）

### 客户端和服务器通信方式
1. RPC - 远程过程调用（Remote Procedure Call）协议 几年前...
2. REST - Representational State Transfer 表现层状态转移

### REST
####简介
特征：
1. 客户端 - 服务器（客户端和服务器之间必须有明确的界线）
2. 无状态 - 客户端发出的请求中必须包含所有必要的信息。服务器不能在两次请求之间保存客户端的任何状态
3. 缓存 - 服务端发出的响应可以标记为可缓存和不可缓存，这样处于优化的目的，客户端可以使用缓存
4. 接口统一 - 客户端访问服务器资源时，使用的协议必须一致，定义良好，且已经标准化。最常使用的统一接口是HTTP协议
5. 系统分层 - 客户端和服务器之间可以按需插入代理服务器、缓存或网关，以提高性能
5. 按需代码 - 客户端可以选择从服务器上下载代码，在客户端的环境中执行

#####资源就是一切

如：博客程序中，用户、博客文章、评论都是资源

#####每个资源都要使用唯一的URL表示

如：
- 一偏文章：/api/posts/12345
- 某一类资源的集合：/api/posts/、api/comments/
- 资源的逻辑子集，如某篇文章的所有评论：/api/posts/12345/comments/
- 表示集合的路径，习惯性在末尾加/，表示是一个文件夹

博客API的JSON表示：

```
{
         "url": "http://www.example.com/api/posts/12345",
         "title": "Writing RESTful APIs in Python",
         "author": "http://www.example.com/api/users/2",
         "body": "... text of the article here ...",
         "comments": "http://www.example.com/api/posts/12345/comments"
}
```

注意url、author、comments字段都是完整的资源URL，客户端可以通过这些URL发掘新资源


