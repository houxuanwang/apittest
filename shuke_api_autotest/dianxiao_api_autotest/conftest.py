import pytest
import logging
import sys
# from user.services.user_service import UserService
# import requests
import requests

from dianxiao_api_autotest.shuke_settings import R

from dianxiao_api_autotest.shuke_settings import uat_fund_db
#from common.database import DataBase

logger = logging.getLogger(__name__)


# @pytest.fixture(scope="session", autouse=True)
# def login_user():
#     """
#     登录前置
#     """
#     logger.info(f'[setUp session scope login:"开始登录"')
#     username = "thinkgem"
#     password = "Admin123$"
#     login(username=username, password=password)
#     logger.info(f'[登陆成功]:{username}]')
#     yield 1

@pytest.fixture(scope="session", autouse=True)
def login_user():
    R.session.headers['Cookie']= "dianxiao_c=jrCallCenter; 360tmk.session.id=3f5f3cf802ae4b778ed624b63a3411eb; username=wanghouxuan; JSESSIONID=0905E0586C3A48787CAFFF772AF727CB; __DC_sid=69067473.1353034741945867300.1718678855435.8604; __DC_monitor_count=9; __DC_gid=69067473.808472191.1716443922924.1718678966447.626"
    R.session.headers['Cookie']= "360tmk.session.id=e026b02d05964a96aa9b906c942d71e1;"
    # R.session.headers['Content-Type']='application/json;charset=UTF-8'
    yield 1

#     """
#     登录前置
#     """
#     logger.info(f'[setUp session scope login:"开始登录"')
#     username = "thinkgem"
#     password = "Admin123$"
#     login(username=username, password=password)
#     logger.info(f'[登陆成功]:{username}]')
#     yield 1

# 1@pytest.fixture(scope="session", autouse=True)
# def db():
#     """
#     连接数据库
#     """
#     db = DataBase(uat_fund_db)
#     logger.info(f'[数据库连接成功]]')
#     yield db


def change_user(username: str, password: int):
    """
    切换账号
    """
    del R.session.headers['Authorization']
    login(username, password)
    logger.info(f'[切换成功]: {username}')


def login(username='thinkgem', password='Admin123$'):
    url = "http://tmk.uat.360jie.com.cn/backend/login"
    payload = 'username='+username+'&password='+password+'&companyNameId=jrCallCenter'
    # payload = 'username=thinkgem&password=Admin123$&companyNameId=jrCallCenter'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'}
    s = requests.request('POST',url, headers=headers, data=payload)
    Cookies = s.request.headers['Cookie']

    h = {
        "Cookie": Cookies
    }
    # 更新header
    print("***********************")
    print(R.session.headers)
    R.session.headers.update(h)
    print(R.session.headers)



