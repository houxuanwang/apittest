import requests

url = "http://11.43.192.135/backend/seatStatusMonitor/reportSeatStatus"

payload = 'status=idle'
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': '360tmk.session.id=a62c97a5f78647d9a99b6915feea3fa7; dianxiao_c=jrCallCenter; username=wanghouxuan; __DC_sid=69067473.3706086705584057300.1720404126995.3699; JSESSIONID=91C988BDA72FA378F3C94DE7B39AC1F0; __DC_monitor_count=8; __DC_gid=69067473.628652478.1720404126998.1720405954605.8; dianxiao_c=jrCallCenter',
  'Origin': 'http://11.43.192.135',
  'Referer': 'http://11.43.192.135/backend?login',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
