from box import Box
import requests
from records import Database
from common.api_request import ApiRequest

# SIT 域名配置
SIT_HOST = "http://sit-tmk.360-jr.com"
# UAT 域名配置
UAT_HOST = Box({"sit": "",
                  "uat": ""})
# 线上域名
PROD_HOST = ""

HEADERS = {"Content-Type": "application/json"}
FORM_HEADERS = {"Content-Type": 'application/x-www-form-urlencoded'}
R = ApiRequest()


# redis配置

# http请求相关配置
TIMEOUT = 120  # 默认超时时间
TIMEOUT_RUN_JOB = 60 * 60  # job执行的超时时间
RETRY = 3  # 接口请求失败，默认重试次数
DB_RETRY = 3  # db操作失败，默认重试次数
LOGIN_RETRY = 3  # 登陆重试次数

# 测试账号配置

# 测试账号用户名和密码


# 上市资金系统配置
uat_fund_db = {
    "host": "10.228.128.126",
    "port": 80,
    "user": "root",
    "password": "Aa123!@#qwe=buAy27Glx",
    "db": "360tmk"

}
uat_dome2_db = {
    "host": "",
    "port": 9,
    "user": "",
    "password": "",
    "db": " "
}
db_global_config = {
    'uat_fund_db': uat_fund_db,
    'uat_dome2_db': uat_dome2_db
}
db = Database("mysql+pymysql://capital_test:03f0c4cb12cb04f4@10.208.34.85:2485/capital_test", pool_recycle=1)

# sql语句配置


# config 文件


# 测试报告地址
path_report = '/.report.json'

allure_report = ''


# job相关
