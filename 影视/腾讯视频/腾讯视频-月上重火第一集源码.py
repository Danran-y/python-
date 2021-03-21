import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
import os
import time
session=requests.session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
}
url=('https://apd-63d6a4475d94d218cec210159893c489.v.smtcdns.com/moviets.tc.qq.com/ArosRhRuy6FbsAnRMuBy6KBHmy4WtoVL0mbkEUw5x0xo/uwMROfz2r5zAoaQXGdGnC2df644E7D3uP8M8pmtgwsRK9nEL/XHaEET9GTof5Y_VW1571IScfGbVsDSoAtxScr5QzpvfgIATMbra0WlOb0gChQv6umqaC_9SCjq_FQ-rZ6AjpSnXqoQIFlG1W2F5juXlcFPVpPZa8bBXKw0LdjilD2P2jA88bDmnoBrfzF1jaDACguSj96HRN2GGN5CMRywZZEM4/d0034ube5wo.321002.ts.m3u8?&ver=4')
title=url[343:369]
r=session.get(url,headers=headers)
a=str(r.content)

c=a.strip("\\n'")
b=c.split('\\n')

for i in range(1000):
    if i<10:
        j='000'+str(i)
        n=int(j)

    elif i<100:
        j='00'+str(i)
        n = int(j)

    elif i<1000:
        j='0'+str(i)
        n = int(j)

    else:
        break
    if n<5:
        continue
    elif n%2==1:
        continue
    elif n%2==0:
        try:
            url_ts = (
                        'https://apd-63d6a4475d94d218cec210159893c489.v.smtcdns.com/moviets.tc.qq.com/ArosRhRuy6FbsAnRMuBy6KBHmy4WtoVL0mbkEUw5x0xo/uwMROfz2r5zAoaQXGdGnC2df644E7D3uP8M8pmtgwsRK9nEL/XHaEET9GTof5Y_VW1571IScfGbVsDSoAtxScr5QzpvfgIATMbra0WlOb0gChQv6umqaC_9SCjq_FQ-rZ6AjpSnXqoQIFlG1W2F5juXlcFPVpPZa8bBXKw0LdjilD2P2jA88bDmnoBrfzF1jaDACguSj96HRN2GGN5CMRywZZEM4/' + str(b[n]))
            title = url_ts[343:368]
            r2 = session.get(url_ts, headers=headers)
            with open('一寸相思/y/'+j+'.ts', "wb")as f:
                f.write(r2.content)
            print('成功下载' + title)
        except:
            break
    else:
        break
list=os.popen(' copy /b F:\python\网络爬虫基础\movie\MP4\一寸相思\y\*.ts F:\python\网络爬虫基础\movie\MP4\一寸相思\-1.mp4 ').read()
#copy /b F:\python\网络爬虫基础\video\MP4\一寸相思\y\*.ts F:\python\网络爬虫基础\video\MP4\一寸相思\4.mp4
#shell_str = 'copy /b ' + shell_str + ' 5.mp4'+'\n'+'del *.ts'

