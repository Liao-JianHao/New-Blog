from fdfs_client.client import Fdfs_client
import os


from back_end.utils.sql_curd.blog_mysql import DataBaseHandle


# 清除FastDFS的storage命令： find ./ -name "*.jpg"|xargs rm -r
class FastDFS:
    def __init__(self):
        self.filepath = '../../../image_storage'
        self.ip_port = "192.168.47.132:8888/"

    def upload_image(self):
        mysql = DataBaseHandle(host="localhosts", user="root", password="liao", database="blog")

        client = Fdfs_client("./client.conf")
        for filename in os.listdir(self.filepath):
            image_url = client.upload_by_filename("/home/mrc/blog/image_storage/" + filename)

            query = 'insert into top_image(url) value(%s)'
            url = self.ip_port + image_url['Remote file_id']

            mysql.insertDB(query, url)
        mysql.closeDB()


if __name__ == '__main__':
    fdfs = FastDFS()
    fdfs.upload_image()



