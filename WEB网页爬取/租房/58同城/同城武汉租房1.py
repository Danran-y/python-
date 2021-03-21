#coding: utf-8
#@Time    : 2021/3/12 21:12
#@Author  : Danran_y
#@FileName: 同城武汉租房1.py
#@Software: PyCharm

#https://wh.58.com/chuzu/pn2/?PGTID=0d3090a7-0009-e09a-0208-8342f5a576a7&ClickID=2
#https://wh.58.com/chuzu/pn1/?PGTID=0d3090a7-0009-ed6f-a4ff-d52f4aa95edd&ClickID=2

import requests
from lxml import etree
import time
from PIL import Image
from lxml import etree
import requests
import re
import json
import random
import pymysql
from retrying import retry
import requests
from random import choice


cursor = db.cursor()
proxie_list = [
#ip代理
]


# stop_max_attempt_number 最大重试次数，wait_fixed 每次重试的时间，单位为毫秒
@retry(stop_max_attempt_number=10, wait_fixed=1000)

def get_content(url,headers):
    for i in range(10):
        splash_url = choice(proxie_list)
        proxies = {'http': splash_url, 'https': splash_url}
        resp = requests.get(url, proxies=proxies, timeout=2,headers=headers)
        if resp.text.find('class')!=-1:
            return resp
        else:
            continue

def get_user_agent():
    user_agent = [
        'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.88Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'
    ]
    headers = random.choice(user_agent)
    return headers

headers = {
            'User-Agent': get_user_agent(),

        }

url='https://wh.zu.ke.com/zufang/WH2523180143950962688.html?nav=0&unique_id=994c3790-e46f-4804-ad87-5c5bf4e13d7fzufangpg51615560336840'
data=get_content(url,headers).text
print(data)