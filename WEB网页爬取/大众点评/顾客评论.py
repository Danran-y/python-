#coding: utf-8
#@Time    : 2020/10/31 19:02
#@Author  : Danran_y
#@FileName: 顾客评论.py
#@Software: PyCharm

import requests
from lxml import etree
import random
import re
import time

headers={
'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.106Safari/537.36',
'Cookie': '_lxsdk_cuid=17400f4418151-0eccf76e3e09c6-4353761-100200-17400f44182c8; _lxsdk=17400f4418151-0eccf76e3e09c6-4353761-100200-17400f44182c8; _hc.v=bc5c6e80-ad61-cc94-4ff7-ec0795746eeb.1597743842; s_ViewType=10; fspop=test; cye=nanjing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; cy=5; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604105066,1604134681,1604193306; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604193425; _lxsdk_s=175815f3b15-f3e-324-da0%7C%7C25'
   # 'Cookie': '_lxsdk_cuid=17400f4418151-0eccf76e3e09c6-4353761-100200-17400f44182c8; _lxsdk=17400f4418151-0eccf76e3e09c6-4353761-100200-17400f44182c8; _hc.v=bc5c6e80-ad61-cc94-4ff7-ec0795746eeb.1597743842; s_ViewType=10; fspop=test; cye=nanjing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604105066; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604105331; _lxsdk_s=1757c3dff85-7ba-517-f62%7C%7C2'
}
Proxies = [
'39.106.223.134:80',
'119.28.65.21:80',
'113.214.13.1:1080',
]
IP = random.choice(Proxies)
proxies = {'http': 'http://'+IP}
url_1='http://www.dianping.com/ajax/json/shopDynamic/allReview?shopId=l4WjL3mL6Jo5qEmF&cityId=5&shopType=10&tcv=o1xgsmfock&_token=eJxVT01vgkAQ%2FS97LQEWdlcg8WAVrYgldcHGmB4ooCIuCmwFbPrfOyb20GSS9zHvJTPfqJ6nyMG6rhOsoGtWIwdhVVcZUpBsYMNgYZvEHlBiKij551mEQemzXk%2BQszUoU6hlfdyNFegtNhlTBgycBzWAGgTmnplDBB2kvDia1ratmuZxecnLvZqchdYczhftRN6Pvil85p1p5YopXISgKUJoAhYPjB8o%2F%2FQSXoBsk%2B9LYJnXhbwhTbVbLZtwve57e8G50fsJ9nlk%2BjdXvkb8GvRja8S%2F%2BOYw29FZsGPipTyJLma0rp67aFmNsScnb2aUF%2FKWdIG%2FuOo8wcEq9TbFyS7FDMfF9CkTlKflonVHJGyPcjQcop9f3GpnhQ%3D%3D&uuid=bc5c6e80-ad61-cc94-4ff7-ec0795746eeb.1597743842&platform=1&partner=150&optimusCode=10&originUrl=http%3A%2F%2Fwww.dianping.com%2Fshop%2Fl4WjL3mL6Jo5qEmF'
data=requests.get(url_1,headers=headers,proxies=proxies).content.decode('utf-8')
import json
d=json.loads(data)
d1=d['reviewAllDOList']
for i in d1:#获取每个顾客评论数据所在字典
    time=i['reviewDataVO']['addTimeVO']
    pingl=i['reviewDataVO']['reviewBodyBrief']
    pingl2 = i['reviewDataVO']['reviewBody']
    pingl3 = i['reviewDataVO']['reviewBodyHidden']
    d2=re.findall('<svgmtsi class="review">.*?;</svgmtsi>',pingl)
    d3 = re.findall('<svgmtsi class="review">.*?;</svgmtsi>', pingl2)
    d4 = re.findall('<svgmtsi class="review">.*?;</svgmtsi>', pingl3)
    for j in d2:
        pingl=pingl.replace(j,'')
    print(pingl)
    for j in d3:
        pingl2=pingl2.replace(j,'')
    print(pingl2)
    for j in d4:
        pingl3=pingl3.replace(j,'')
    print(pingl3)