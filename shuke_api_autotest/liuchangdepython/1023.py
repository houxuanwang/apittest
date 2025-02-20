# -*- coding: utf-8 -*-
import mysql.connector
con = mysql.connector.connect(
    host="10.228.128.127", port="80",
    user="root", password="Aa123!@#qwe=buAy27Glx",
    database="jie_arrcol"
)

# 创建游标
cursor=con.cursor()
sql = "select * from hj_customer limit 1;"
for one in cursor:
    print(one)

con.close()
