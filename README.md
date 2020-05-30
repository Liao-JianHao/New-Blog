# 94后的Mr.C（个人博客）
> 以前的博客：www.c-blogs.cn，用的是别人的前端模板，自己用markdown语法搭建的
>
> 感觉不太满意，打算自己的想法一步一步从零到有

##  个人博客（技术栈）

> 前端以html、css、javascript为主，框架采用Vue
>
> 后端以Python为主，框架采用Flask-restful
>
> 其他技术：FastDFS、Nginx、Mysql(mariaDB)、Redis

## 技术点

#### 博客首页动态背景图

- 前端
    - Vue框架，使用axios向后端服务器发送请求，获取图片url
- 后端
    - 搭建FastDFS分布式文件系统，管理存储图片
    - 使用Nginx代理FastDFS的Storage，提升性能
    - 将FastDFS返回的图片url，存储至Mysql
        - 字段包含：image_id、image_url(图片路径)
    - Redis记录图片权重值，权重值越低，图片被选中概率越大
    - 基于权重值，随机获取图片url，通过flask-restful返回给前端


