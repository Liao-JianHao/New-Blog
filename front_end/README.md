## 搭建 vue 项目

Canvas transition animations

|名称|说明|
|---|---|
|ubuntu20|（安装64位系统）|
|Vue V2.9.6|前端框架|
|less|Less是一门css预处理语言|

~~~
第一步：安装 nodejs
sudo apt install nodejs

第二步：安装 npm
sudo apt install npm

第三步：安装 cnpm
sudo npm install -g cnpm --registry=https://registry.npm.taobao.org

第四步：下载 vue
sudo cnpm install -g vue-cli

第五步：创建 vue 项目
sudo vue init webpack project_name

第六步：初始化安装依赖
cnpm install 或 npm install

第七步：运行 vue 项目
npm run dev

第八步：安装 less axios 等拓展
npm install less less-loader --save-dev
    在 build 文件夹中的 webpack.base.conf.js 的 rules 中加入
    { test: /.less$/, loader: "style-loader!css-loader!less-loader", }
    如果运行项目依然有 less 错误(可能因less版本太高):
        卸载当前版本：npm uninstall less-loader
        下载低版本：npm install less-loader@4.1.0 --save

npm install axios
    在 main.js 中加入：
    import Vue from 'vue'
    import axios from 'axios'
    使用方法一： main.js 写 Vue.prototype.$http = axios 后，就可以在 vue 中使用 this.$http.get()等
    使用方法二： 在需要的文件中导入 import axios from 'axios',直接使用 axios.get() 即可
~~~

#### 随机壁纸
> 使用的是Vue2.0，非3.0后版本
>
> 在config文件夹中，配置 index.js，解决 cors 等问题

~~~
proxyTable: {
        '/api': {
          target: 'http://127.0.0.1:5000/', // 要访问的接口域名
          changeOrigin: true, // 开启代理：在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
          pathRewrite: {
            '^/api': 'http://127.0.0.1:8080/' // 这里理解成用'/api'代替target里面的地址,比如我要调用'http://40.00.100.100:3002/user/add'，直接写'/api/user/add'即可
          }
      }
~~~

~~~
使用 vue 语法，绑定 style ，原写法 v-bind:style ， 简写 :style
<div id="top_image" :style="{backgroundImage: 'url(http://' + img + ')'}"></div>

设置默认背景图片
data() {
    return {
        img: 图片地址
    }
}

定义方法，发送 axios get 请求，获取后端服务器返回的随机图片的地址
methods: {
    方法名() {
        axios.get('服务器图片接口').then(res => {this.img = res.data})
    }
}

Vue 的生命周期，created 这个钩子在实例被创建后调用，一般可以在 created 函数中调用 ajax 获取页面初始化
created:function() {
    this.方法名()
}
~~~
