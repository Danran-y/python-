import requests
from lxml import etree
import random
import re
import time
session=requests.session()
headers={
'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.106Safari/537.36',
}
Proxies = [
'http://196.55.16.153:80',
'http://91.205.174.26:80',
]
IP = random.choice(Proxies)
proxies = {'http': IP}
url_1='https://m.douban.com/rexxar/api/v2/niffler/collection/30?for_mobile=1&ck=5Tef'
r1=session.get(url_1,headers=headers,proxies=proxies).content.decode('unicode_escape')

