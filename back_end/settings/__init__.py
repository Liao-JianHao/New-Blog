class Config:
    DEBUG = True

    # mysql数据库的配置信息
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'blog'
    USERNAME = 'root'
    PASSWORD = 'liao'

    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                            password=PASSWORD,
                                                                                            host=HOST, port=PORT,
                                                                                            db=DATABASE)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


    SECRET_KEY = "rJ79s0MhamX/wTg72AutpaVmVQGnXPIX8/+PnAHccSRjeJt+9vWzjgUVAzLo4+xB"