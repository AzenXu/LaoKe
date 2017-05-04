{% extends "bootstrap/base.html" %}
从flask-bootstrap中导入bootstrap/base.html，实现模板继承。
base中提供了一个网页框架，引入了bootstrap中的所有css和js文件

下面重定义基模板提供的三个块：
1. title标签
{% block title %} 这是标题 {% endblock %}

2. 页面中的导航条
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
  <div class="container">  -> 这里是一个div容器
    <div class="navbar-header">
      <button type="button" class="navbar-toggle"
      data-toggle="collapse" data-target=".navbar-collapsse">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="/">Flasky</a>
    </div>
  </div>
</div>
{% endblock %}

3. 页面的主体
{% block content %}
<div class="container">
  <div class="page-header">
    <h1>Hello, {{name}}!</h1>
  </div>
</div>
{% endblock %}

4. base.html里面定义的其他块
doc -> 整个HTML文档
html_attribs -> <html>标签的属性
html -> html标签的内容
head
title
metas
styles
body_attribs
body
navbar
content
scripts
记得使用super()以防止定义的东东被覆盖

5. 使用模板继承技术抽取代码 - base.html

6. 链接 -> 使用url_for辅助函数
  url_for('index') 结果-> / 相对路径
  url_for('index', _external=True) 结果-> 绝对地址http://localhost:5000/

内部跳转用相对路径即可，外部用绝对路径

传参示例 url_for('user', name='john', _external=True) -> http://localhost:5000/user/john
url_for('index', page=2) -> /?page=2
