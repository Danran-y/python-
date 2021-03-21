#coding: utf-8
#@Time    : 2021/3/13 16:30
#@Author  : Danran_y
#@FileName: 千1.py
#@Software: PyCharm

import requests
import time
# url='http:\u002F\u002Faudio04.dmhmusic.com\u002F71_53_T10057218352_128_4_4_0_sdk-cpm\u002Fcn\u002F0412\u002FM00\u002F6F\u002F39\u002FChAKEV-BZnSAYaQHAAdYIlSRU08829.mp3?xcode=a000824d467406327e505cae9bb56c1093a9cc9'
#
# url = url.encode('utf-8').decode("unicode_escape")
# print(url)
import hashlib
TSID='T10044518961'
timestamp=str(int(time.time()))
#timestamp='1615715765'
print(timestamp)
def md5sum(str):
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    return m.hexdigest()
secret="0b50b02fd0d73a9c4c8c3a781c30845f"
r='TSID='+TSID+'&appid=16073360&timestamp='+timestamp+secret

sign=md5sum(r)
url='https://music.taihe.com/v1/song/tracklink?sign='+sign+'&appid=16073360&TSID='+TSID+'&timestamp='+timestamp
print(url)
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
data=requests.get(url,headers=headers).content.decode('utf-8')
print(data)


