import time

import requests

url = "https://lingxi-qoa.daikuan.qihoo.net/apis/common/api/qoaTools/"

payload = ("{\"url\":\"http://stg1-qoatools-app.daikuan.qihoo.net/finance/loanFunction/\",\"method\":\"post\","
           "\"requestBody\":{\"env\":\"STG2\",\"selected_methods\":\"借款\",\"user_no\":\"UR6529526412867809281\","
           "\"repay\":\"E\",\"user_level\":\"15\",\"term\":3,\"product_code\":\"360JIETIAO\",\"amount\":500,"
           "\"flex\":\"0\",\"capital_code\":\"\",\"purpose\":\"13\"},\"timeout\":60,\"headers\":{"
           "\"user\":\"wanghouxuan-jk\",\"cardId_admin\":\"145\"}}")
headers = {
  'Host': 'lingxi-qoa.daikuan.qihoo.net',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMTU1MjcsInVzZXJuYW1lIjoid2FuZ2hvdXh1YW4tamsiLCJleHAiOjE3MjE4MTI1OTAsImVtYWlsIjoid2FuZ2hvdXh1YW4tamtAMzYwc2h1a2UuY29tIn0.ocuyuU4piItavpXZUcM0vBSQoIbADSZJnsYHMeUUCrk',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
  'qoa-user': 'wanghouxuan-jk',
  'Content-Type': 'application/json;charset=UTF-8',
  'Accept': 'application/json, text/plain, */*',
  'qoa-request-id': '01J2BM1J504J577E17BQ87V1E2',
  'qoa-timestamp': '1720524523680',
  'X-CSRFToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMTU1MjcsInVzZXJuYW1lIjoid2FuZ2hvdXh1YW4tamsiLCJleHAiOjE3MjE4MTI1OTAsImVtYWlsIjoid2FuZ2hvdXh1YW4tamtAMzYwc2h1a2UuY29tIn0.ocuyuU4piItavpXZUcM0vBSQoIbADSZJnsYHMeUUCrk',
  'sec-ch-ua-platform': '"Windows"',
  'Origin': 'https://lingxi-qoa.daikuan.qihoo.net',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://lingxi-qoa.daikuan.qihoo.net/toolsCards',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': '_username=wanghouxuan-jk; jrops-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NDg0OSwidXNlcm5hbWUiOiJ3YW5naG91eHVhbi1qayIsInV1aWQiOiI1ZjQ4NjE0Mi03NzVlLTRkYWQtYTY4My1hYmFkM2Q1ZWIxMWEiLCJleHAiOjE3MjA1NzgzNzR9.nCFsNs_DNZbh6FcgZThmLnibN9UFbncJMjkT5pJkq88; jrops-token-timeout=1720664774689; jrops-refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNWY0ODYxNDItNzc1ZS00ZGFkLWE2ODMtYWJhZDNkNWViMTFhIiwidXNlcl9pZCI6NDg0OSwidXNlcm5hbWUiOiJ3YW5naG91eHVhbi1qayIsImV4cCI6MTcyMTcwMTU3NH0.MsiLAgYr0XXkGbhtD0ZS1TaSx0j1_3Ab8OoCaVH2VQU; jrops-refresh-token-timeout=1721701574689; sessionid=2zmaw1pyzivag6ft848n8085kgrpfgua'
}
i = 0
for i in range(0,200):
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)

  time.sleep(300)
  i = i+1
