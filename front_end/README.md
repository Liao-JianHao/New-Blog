## 搭建 vue 项目

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
npm install --save axios vue-axios
    在 main.js 中加入：
    import Vue from 'vue'
    import axios from 'axios'
    import VueAxios from 'vue-axios'
    Vue.use(VueAxios, axios)
~~~
