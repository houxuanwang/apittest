from requests_toolbelt.multipart.encoder import MultipartEncoder
import platform
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST
import random
import time


# 封装上传文件接口
def uploadfile(host, url,filename,all_filename="./shangshizijin_api_autotest/fundmanage/testcases/43395911.jpg"):
    """上传附件"""
    url = host + url
    if platform.system().lower() == 'windows':
        multipart_encoder = MultipartEncoder(
            fields={'file': (filename, open(filename, 'rb'), 'multipart/form-data'), },
            boundary='----------------------------' + str(random.randint(1e28, 1e29 - 1)))
    elif platform.system().lower() == 'linux':
        multipart_encoder = MultipartEncoder(
            fields={'file': (
                filename, open(all_filename, 'rb'),
                'multipart/form-data'), },
            boundary='----------------------------' + str(random.randint(1e28, 1e29 - 1)))
    #R.session.headers['Content-Type'] = multipart_encoder.content_type
    headers = {}
    headers['token'] = '2dd76c667106366290f3e71c37e8a7a1aeab68f902f714630dbd722c5fd30e2da4dda16317f0f382c195a2cbe9d2df3825e70813d6d9e737aded865ddf0a02a1d36abcf78251c87a '
    headers['Content-Type'] ='multipart/form-data; boundary=--------------------------004734069158989553651229'
    # res = R.post(url, headers=R.headers, data=multipart_encoder)
    print(multipart_encoder)
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'token': '2dd76c667106366290f3e71c37e8a7a1aeab68f902f714630dbd722c5fd30e2da4dda16317f0f382c195a2cbe9d2df3825e70813d6d9e737fc682224b2d579d5994f5537a7e4dcec',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://jumper.360-jr.com:9999',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://jumper.360-jr.com:9999/',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    payload = {'requestid':'09df2fd300d9a8d285bfad8512e2391a4c56d346','sender':'1688856203334882'}
    files = [
        ('file', ('12345.jpg', open('12345.jpg', 'rb'), 'image/jpeg'))
    ]
    res = R(url=url, method='POST', headers=headers, data=payload,files=files)
#    del R.session.headers['Content-Type']
    fileid = res.json()['data']['fileId']
    print(fileid)
    filename = res.json()['data']['fileName']
    print(filename)
    return res.json(), fileid, filename
