# 个人博客（技术栈）



## FastDFS + Nginx
> fastdfs作者github地址：https://github.com/happyfish100
> 大部分所需工具都在内


|名称|说明|
|---|---|
|Ubuntu 20|（安装64位系统）|
|libfastcommon V1.0.43|FastDFS分离出的一些公用函数包|
|FastDFS V6.06|FastDFS本体|
|fastdfs-nginx-module V1.22|FastDFS和nginx的关联模块，解决组内同步延迟问题|
|nginx V1.17.7|nginx主体|

#### FastDFS 环境安装 与 关闭防火墙
~~~
sudo apt install net-tools
sudo apt install openssh-server
sudo apt install gcc
sudo apt install libevent-dev

# 测试环境关闭防火墙
systemctl stop firewalld.service
# 开机警用防火墙
systemctl disable firewalld.service
# 查看防火墙状态
firewall-cmd --state
~~~

#### libfastcommon 安装
~~~
第一步：克隆项目 并 解压
wget -c "https://github.com/happyfish100/libfastcommon/archive/V1.0.43.tar.gz"
tar -zxvf libfastcommon-1.0.43.tar.gz

第二步：进入 libfastcommon 文件夹中 进行编译和安装
./make.sh 及 ./make.sh install

第三步：设置环境变量
export LD_LIBRARY_PATH=/usr/lib64/

第四步：创建软连接
ln -s /usr/lib64/libfastcommon.so /usr/local/lib/
~~~

#### FastDFS 安装
~~~
第一步：克隆项目 并 解压
wget -c "https://github.com/happyfish100/fastdfs/archive/V6.06.tar.gz"
tar -zxvf fastdfs-6.06.tar.gz

第二步：进入 fastdfs 文件夹中 进行编译和安装
./make.sh 及 ./make.sh install

第三步：重命名配置文件
cd /etc/fdfs/
cp storage.conf.sample storage.conf
cp client.conf.sample client.conf
cp tracker.conf.sample tracker.conf

第四步：配置 tracker
mkdir -p /fastdfs/tracker
vim /etc/fdfs/tracker.conf

    修改：base_path = /fastdfs/tracker
         http.server_port = 8888

第五步： 配置 storage
mkdir -p /fastdfs/storage
vim /etc/fdfs/storage.conf
    
    修改：base_path = /fastdfs/tracker
         tracker_server = 当前ip地址:22122
         http.server_port = 8888

第五步： 启动 tracker 和 storage 服务
/etc/init.d/fdfs_trackerd start
/etc/init.d/fdfs_storaged start

或
sudo /usr/bin/fdfs_storaged /etc/fdfs/storage.conf
sudo /usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf

第六步：配置 client.conf
vim /etc/fdfs/client.conf

    修改：base_path = /fastdfs/tracker
         tracker_server = 当前ip地址:22122

第七步：进入 fastdfs 文件夹中，将http.conf，mime.types两个文件拷贝到/etc/fdfs/目录下
cd fastdfs-6.06/conf/
sudo cp http.conf mime.types /etc/fdfs/

第八步：创建一个软连接，在/fastdfs/storage文件存储目录下创建软连接，将其链接到实际存放数据 的目录
ln -s /fastdfs/storage/data/ /fastdfs/storage/data/M00

备注：
将 tracker 和 storage 服务设置开机启动
vim /etc/rc.d/rc.local
/etc/init.d/fdfs_trackerd start
/etc/init.d/fdfs_storaged start
~~~

#### Nginx 环境安装
~~~
sudo apt-get install libpcre3 libpcre3-dev
sudo apt-get install zlib1g-dev
sudo apt-get install openssl libssl-dev 
~~~

#### fastdfs-nginx-module 安装
~~~
第一步：克隆项目 并 解压
wget -c "https://github.com/happyfish100/fastdfs-nginx-module/archive/V1.22.tar.gz"
tar -zxvf fastdfs-nginx-module.1.22.tar.gz

第二步：修改配置fastdfs-nginx-module-1.22/src/config
将/usr/local替换成/usr
~~~

#### Nginx 安装
~~~
第一步：克隆项目 并 解压
wget -c http://nginx.org/download/nginx-1.17.7.tar.gz
tar -zxvf nginx.1.17.7.tar.gz

第二步：进入文件夹添加 http_stub_status_module 模块
./configure --prefix=/usr/local/nginx --with-http_stub_status_module

第三步：添加 fastdfs-nginx-module
./configure --add-module=/home/mrc/fastdfs-nginx-module-1.22/src/

第四步：安装和编译
编译：sudo make
安装：sudo make install

第五步：复制并修改fastdfs-ngin-module中的配置文件
sudo cp /home/mrc/fastdfs-nginx-module-1.22/src/mod_fastdfs.conf /etc/fdfs/
vim /etc/fdfs/mod_fastdfs.conf
    
    修改：connect_timeout=10
         tracker_server=192.168.0.154:22122
         url_have_group_name = true
         store_path0=/fastdfs/storage

第六步：配置 nginx.conf
vim /usr/local/nginx/conf/nginx.conf
    
    修改：
        server {
            listen       80;
            server_name  192.168.0.154;
            location ~/group([0-9])/M00 {
                    root  /fastdfs/storage/data;
                    ngx_fastdfs_module;
            }
        }

第七步：启动 nginx
/usr/local/nginx/sbin/nginx
~~~

## Mysql(MariaDB)

#### Mysql安装
~~~
第一步：更新 并 下载 mariadb
sudo apt update
sudo apt install mariadb-server

第二步：配置 root 用户
sudo mysql_secure_installation
    输入：Enter current password for root (enter for none): Enter
         Set root password? [Y/n] n # 是否需要设置root密码
         Remove anonymous users? [Y/n] Y # 是否删除匿名用户
         Disallow root login remotely? [Y/n] Y # 是否禁止root远程登录
         Remove test database and access to it? [Y/n] Y # 是否删除test数据库
         Reload privilege tables now? [Y/n] Y # 是否重新加载权限表

第三步：将 mysql.user 的 unix_socket 插件更改为 mysql_native_password
sudo mysql
update mysql.user set plugin='mysql_native_password';

第四步：更改密码并刷新
update mysql.user set password=PASSWORD("your password") where User='root';
flush privileges;

第五步：配置 root 用户远程连接
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'your password' WITH GRANT OPTION; 
GRANT ALL PRIVILEGES ON *.* TO 'root'@'your ip' IDENTIFIED BY 'your password' WITH GRANT OPTION;
FLUSH PRIVILEGES;
~~~

#### 创建库和表
~~~
# 创建库
create database blog charset=utf8;

# 创建表
create table top_image(
    id smallint unsigned auto_increment primary key not null,
    url varchar(255) default null
)engine=MyISAM default charset=utf8;
~~~

#### Mysql 与 Python 交互
~~~
版本：
python2.x - python3.4：pip install mysql-python
python.3x：pip install pymysql

~~~

