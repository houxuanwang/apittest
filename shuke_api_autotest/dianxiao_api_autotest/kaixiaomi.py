import requests

url = "http://11.43.192.135/backend/tmkhmc/perceptionCall/changStatus"

payload = "{\"type\":true}"
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json; charset=UTF-8',
  'Cookie': '360tmk.session.id=a62c97a5f78647d9a99b6915feea3fa7; dianxiao_c=jrCallCenter; username=wanghouxuan; __DC_sid=69067473.3706086705584057300.1720404126995.3699; JSESSIONID=91C988BDA72FA378F3C94DE7B39AC1F0; __DC_monitor_count=4; __DC_gid=69067473.628652478.1720404126998.1720405219053.4; dianxiao_c=jrCallCenter',
  'Origin': 'http://11.43.192.135',
  'Referer': 'http://11.43.192.135/backend?login',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
