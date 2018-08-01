# encoding:utf-8
'''
使用方法：1.在主程序中先实例化DB Mysql数据库操作类。
      2.使用方法:db=database()  db.fetch_all("sql")
'''
import pymysql
import configparser
import logging
import logging.config

rd = configparser.ConfigParser()  # 调用配置操作句柄
rd.read('database_conf.ini')
DBHOST = rd.get('mysql', 'mysql_server')
DBPORT = rd.get('mysql', 'mysql_port')
DBUSER = rd.get('mysql', 'mysql_username')
DBPAWD = rd.get('mysql', 'mysql_password')
DBNAME = rd.get('mysql', 'mysql_database')
DBCSET = rd.get('mysql', 'mysql_charset')
LOGPATH = rd.get('logger','logger_path')


logging.config.fileConfig(LOGPATH)
logger = logging.getLogger('main')

#test
logger.info('------------日志加载------------')


# 数据库操作类
class database:
    def __init__(self, dbname=None, dbhost=None):
        self._logger = logger
        # 这里的None相当于其它语言的NULL
        if dbname is None:
            self._dbname = DBNAME
        else:
            self._dbname = dbname
        if dbhost is None:
            self._dbhost = DBHOST
        else:
            self._dbhost = dbhost

        self._dbuser = DBUSER
        self._dbpassword = DBPAWD
        self._dbcharset = DBCSET
        self._dbport = int(DBPORT)
        self._conn = self.connectMySQL()

    def getLogger(self):
        return self._logger

    # 数据库连接
    def connectMySQL(self):
        conn = False
        try:
            conn = pymysql.connect(host=self._dbhost,
                                   user=self._dbuser,
                                   passwd=self._dbpassword,
                                   db=self._dbname,
                                   port=self._dbport,
                                   charset=self._dbcharset,
                                   )
        except Exception as e:
            self._logger.error("connect database failed, %s" % e)
            conn = False
        return conn

    # 获取查询结果集
    def fetch_all(self, sql):
        cursor = self._conn.cursor()
        res = ''
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            self._conn.commit()
            cursor.close()
            print(res)
        except Exception as e:
            self._conn.rollback()
            res = False
            cursor.close()
            self._logger.warn("query database exception, %s" % e)
        return res

    def update(self, sql):
        flag = False
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql)
            self._conn.commit()
            flag = True
            cursor.close()
        except Exception as e:
            self._conn.rollback()
            flag = False
            cursor.close()
            self._logger.warn("update database exception, %s" % e)
        return flag

    # 关闭数据库连接
    def close(self):
        if (self._conn):
            try:
                self._conn.close()
            except Exception as e:
                self._logger.warn("close database exception, %s,%s,%s" % e)
