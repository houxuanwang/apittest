# -*- coding:utf-8 -*-
# Time   : 2024/10/23 17:03
# Author : zhuyuqing
# File   : demo.py

import time
import pymysql

class MySQL:
    def __init__(self, db):
        self.host = db['host']
        self.user = db['user']
        self.password = db['password']
        self.port = db['port']
        self.db = db['db']
        self.sqlConn = None
        self.sqlCursor = None
        self.err = None
        self.value = True

    def __enter__(self):
        try:
            self.sqlConn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db,
                charset="utf8",
                port=self.port)
            self.sqlCursor = self.sqlConn.cursor()
            logger.info('数据库连接成功')  # 添加数据库连接成功的日志
        except BaseException as e:
            self.value = False
            self.err = e
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.sqlCursor.close()
        except BaseException as e:
            self.err = e
            self.value = False
        try:
            self.sqlConn.close()
        except BaseException as e:
            self.err = e
            self.value = False

    def select(self, sql, number=1, sleep=1, log=True):
        data = []
        for i in range(number):
            try:
                self.sqlCursor.execute(sql)
                cur = self.sqlCursor.description
                result = self.sqlCursor.fetchall()
            except BaseException as e:
                self.err = e
                logger.info('数据库查询异常: {}'.format(str(e)))
                return None

            try:
                data = [{cur[j][0]: result[i][j].strftime("%Y-%m-%d %H:%M:%S") if isinstance(result[i][j], datetime.datetime) else result[i][j] for j in range(len(cur))}]
            except BaseException as e:
                self.err = e
                return None

            if not data and number != 1:
                time.sleep(sleep)

        return data

    def update(self, sql):
        logger.info('数据修改类sql: {}'.format(sql))
        try:
            self.sqlCursor.execute(sql)
            self.sqlConn.commit()
            logger.info('sql执行正常')
            return True
        except BaseException as e:
            self.sqlConn.rollback()
            self.err = e
            logger.info('数据库更新异常: {}'.format(str(e)))
            return None


class LinkMySql:
    def __init__(self, db_config):
        self.db_config = db_config

    def select(self, sql, number=1, sleep=1, log=True):
        with MySQL(self.db_config) as mysql:
            return mysql.select(sql, number, sleep, log)

    def update(self, sql):
        with MySQL(self.db_config) as mysql:
            return mysql.update(sql)

# 10.228.128.127
if __name__ == '__main__':
    db_config = {
        "host": "10.228.128.127",
        "user": "root",
        "password": "Aa123!@#qwe=buAy27Glx",
        "port": 80,
        "db": "jie_arrcol"
    }
    mysql = LinkMySql(db_config)
    sql = 'select id from hj_customer limit 1;'
    result = mysql.select(sql)
    if result is not None:
        print(result)
    else:
        print("查询失败")