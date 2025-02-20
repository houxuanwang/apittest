import pytest
import logging

import requests

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def login_user():
    """
    登录前置
    """
    logger.info(f'[setUp session scope login:"开始登录"')
    print("123" * 100)
    headers = {
        'Host': 'wecom-msg.360-jr.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://wecom-sidebar.360-jr.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://wecom-sidebar.360-jr.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    user = {
        "account": "7471",
        "password": "1qaz@wsx123"
    }
    us = requests.request("POST",url="https://wecom-msg.360-jr.com/message/business/user/login",headers = headers,json=user)
    print(us.url)

    logger.info(f'[登陆成功]:{12345}]')
    yield us
