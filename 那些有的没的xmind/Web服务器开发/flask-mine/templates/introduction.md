
1. 这里聊聊模板中的变量类型
Jinja2 文档(http://jinja.pocoo.org/docs/templates/#builtin-filters)
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>

还可以以过滤器的方式修改变量的值
 方式：
   变量|过滤器
 举例:
    name|capitalize -> 首字母大写
  过滤器们：
    safe 渲染值的时候不转义 - Jinja2默认自动转义，不能解释变量中的html，需要加这个过滤器
    capitalize 把值的首字母转成大写，其他字母转成小写
    lower 把值转成小写
    upper 把值转成大写
    title 把值中的每个单词的首字母都转成大写
    trim  去掉首尾空格
    striptages 删掉值中的所有HTML标签

  2. 控制结构及宏的使用
  2.1. 条件控制
  {% if user %}
    Hello, {{ user }}
  {% else %}
    Who, are Your
  {% endif %}

  2.2. 循环
  {% for comment in comments %}
    <li> {{ comment }} </li>
  {% endfor %}

  2.3. 宏
  2.3.1. 定义
  {% macro render_comment(comment) %}
    <li>{{ comment }}</li>
  {% endmacro %}

  2.3.2. 使用
  {% for comment in comments %}
    {{ render_comment(comment) }}
  {% endfor %}

  2.3.3. 引入其他.html宏文件
  {% import '宏定义文件.html' as macros %}

  2.3.4. 引入模板代码
  {% include '模板代码.html' %}

  3. 模板继承
  3.1. 定义基模板base.html
  <html>
  <head>
    {% block head %}
    <title>{% block title %}{% endblock %} - My Application</title>
    {% endblock %}
  </head>
  <body>
    {% block body %}
    {% endblock %}
  </body>
  </html>

  3.2. 衍生模板
  {% extends "base.html" %}
  {% block title%}real title{% endblock %}
  {% block head %}
    {{ super() }}
    <style>
    </style>
  {% endblock %}
  {% block body %}
  <h1>Hello, World</h1>
  {% endblock %}
