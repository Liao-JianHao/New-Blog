## 博客后端服务器
> 采用Flask,依据工厂模式搭建的项目
>
> Flask1.0版本后,由代码编写app.run()语句调整为命令flask run启动

|名称|说明|
|---|---|
|Flask V1.1.2|Flask 是一个微型的 Python 开发的 Web 框架，基于Werkzeug WSGI工具箱和Jinja2 模板引擎|
|Flask-restful V0.3.8|是一个Flask拓展，提供了REST API的支持|
|Flask-Script V2.0.6|flask_script的作用是可以通过命令行的形式来操作flask例如通过一个命令跑一个开发版本的服务器，设置数据库|
|Flask-SQLAlchemy V2.4.3|是一个支持Flask的ORM拓展，提供SQL工具及对象关系映射|
|Flask-wtf V0.14.3|Flask-WTF 提供了简单地 WTForms 的集成。功能 集成wtforms。 带有csrf 令牌的安全表单。 全局的 csrf 保护|
|python-dotenv V0.13.0|使用python-dotenv管理环境变量，方便运行flask服务器|

#### 后端目录结构

~~~
back_end
├── application // flask项目文件夹
│   ├── apps // 应用文件夹
│   │   ├── __init__.py // 构建flask蓝图,设置路由
│   ├── __init__.py // 构建flask工厂模式
├── log // 后端生成的日志(flask,pymsql,sqlalchemy,fastdfs等)
├── settings // flask项目配置文件
│   │   ├── __init__.py // 全局通用配置
│   │   ├── dev.py // 开发配置
│   │   ├── prop.py // 生产配置
├── utils // 其他工具包
│   ├── fastdfs // FastDFS 分布式文件存储系统 文件
│   │   ├── blog_fdfs.py // fastdfs客户端,将图片存储至mysql
│   │   ├── client.conf // fastdfs 客户端配置文件
├── .flaskenv // python-dotenv管理flask环境变量
├── manage.py  // flask server启动文件
├── test.py  // 测试文件(生成SECRET_KEY密钥)
~~~