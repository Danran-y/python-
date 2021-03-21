#coding: utf-8
#@Time    : 2020/10/31 9:19
#@Author  : Danran_y
#@FileName: d1.py
#@Software: PyCharm

import requests
from lxml import etree
import random
import re
import time

headers={
'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.106Safari/537.36',
    'Cookie': '_lxsdk_cuid=17400f4418151-0eccf76e3e09c6-4353761-100200-17400f44182c8; _lxsdk=17400f4418151-0eccf76e3e09c6-4353761-100200-17400f44182c8; _hc.v=bc5c6e80-ad61-cc94-4ff7-ec0795746eeb.1597743842; s_ViewType=10; fspop=test; cye=nanjing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604105066; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604105331; _lxsdk_s=1757c3dff85-7ba-517-f62%7C%7C2'
}
Proxies = [
'http://149.28.157.52:8080',
'http://191.235.72.144:8000',


]
IP = random.choice(Proxies)
proxies = {'http': IP}
url_1='http://www.dianping.com/nanjing/ch10'
data=requests.get(url_1,headers=headers,proxies=proxies).text#总网址
address0=re.findall('data-address="(.*?)"',data)#地址
def count(l,l2):
    data1 = str(l)
    l = data1.replace('\\u', '').strip('[').strip(']').split(',')  # 对加密数字进行处理
    for i in range(len(l)):
        l[i] = l[i].replace(' ', '').replace("'", '')
        if l[i] == 'ee0c':
            l[i] = '0'
        elif l[i] == '1':
            l[i] = '1'
        elif l[i] == 'e030':
            l[i] = '2'
        elif l[i] == 'e882':
            l[i] = '3'
        elif l[i] == 'e6a5':
            l[i] = '4'
        elif l[i] == 'f236':
            l[i] = '5'
        elif l[i] == 'f2b3':
            l[i] = '6'
        elif l[i] == 'ef20':
            l[i] = '7'
        elif l[i] == 'e05c':
            l[i] = '8'
        elif l[i] == 'f23b':
            l[i] = '9'

        else:
            l=[]
    dict['{}'.format(l2)]=''.join(l)


html=etree.HTML(data)
for i in range(0,15):
    dict={}
    try:
        dict['店名']=html.xpath('string(//div[@id="shop-all-list"]/ul/li['+str(i+1)+']/div[2]/div[1]/a//h4)')#店名
        dict['评分']=html.xpath('string(//*[@id="shop-all-list"]/ul/li['+str(i+1)+']/div[2]/div[2]/div/div[2])')#评分
        price=html.xpath('//*[@id="shop-all-list"]/ul/li['+str(i+1)+']/div[2]/div[2]/a[2]/b/svgmtsi/text()')#价格
        #price3 获取含有‘1’的列表，目的是使价格完整，正确
        price3 = html.xpath('//*[@id="shop-all-list"]/ul/li[' + str(i+1) + ']/div[2]/div[2]/a[2]/b/text()')
        price2 =count(price,'价格')
        if price3 != []:
            price3.insert(1, dict['价格'])
            dict['价格'] = ''.join(price3)
        else:
            dict['价格'] = ''
        renshu=html.xpath('//*[@id="shop-all-list"]/ul/li['+str(i+1)+']/div[2]/div[2]/a[1]/b/svgmtsi/text()')#评论人数
        renshu2=count(renshu,'评论人数')
        dict['地址']=address0[i]
        dict['url']=html.xpath('string(//div[@id="shop-all-list"]/ul/li['+str(i+1)+']/div[2]/div[1]/a/@href)')#链接url
        print(dict)
    except:
        continue