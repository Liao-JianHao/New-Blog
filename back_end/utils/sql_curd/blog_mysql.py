from loguru import logger
from pathlib import Path
import pymysql


# debug < info< warning< error< critical

logger.add("/home/mrc/New-Blog/back_end/log/sql.log", format="{time:YYYY-MM-DD HH:mm} {level} {message}", level="DEBUG", retention="10 days")


class DataBaseHandle:
    def __init__(self, host, user, password, database, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, charset=self.charset)

    def insertDB(self, sql, *args):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql, args)

        except:
            logger.error("execute failed：" + sql)
        finally:
            self.cursor.close()

    def deleteDB(self, sql):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
        except:
            logger.error("execute failed：" + sql)
        finally:
            self.cursor.close()

    def updateDB(self, sql):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
        except:
            logger.error("execute failed：" + sql)
        finally:
            self.cursor.close()

    def selectDB(self, sql):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except:
            logger.error("execute failed：" + sql)
        finally:
            self.cursor.close()

    def closeDB(self):
        self.conn.close()

