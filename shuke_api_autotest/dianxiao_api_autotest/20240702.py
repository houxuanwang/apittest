import requests

url = "http://11.43.192.135/backend"

payload = {}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Proxy-Connection': 'keep-alive',
  'Upgrade-Insecure-Requests': '1'
}

response = requests.request("GET", url, headers=headers, data=payload,allow_redirects=False)

print(response.headers['Set-Cookie'])
import requests

url = "http://11.43.192.135/backend/login"

payload = 'username=wanghouxuan&password=Admin123%24&companyNameId=jrCallCenter'
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'max-age=0',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': '360tmk.session.id=299aa296bc324e8da2825397375358cf; JSESSIONID=255F0487BBCCD5392E727AAAFFA7AAC9; 360tmk.session.id=f29f828924cb4da4a5fbfbee837df3de; dianxiao_c=jrCallCenter; username=wanghouxuan',
  'Origin': 'http://11.43.192.135',
  'Proxy-Connection': 'keep-alive',
  'Referer': 'http://11.43.192.135/backend/login',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
headers['Cookie'] = response.headers['Set-Cookie']

response = requests.request("POST", url, headers=headers, data=payload,allow_redirects=False)

print(response.text)