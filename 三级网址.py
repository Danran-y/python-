# https://api.mall.autohome.com.cn/gethomead/340600?_appid=car&callback=jQuery17206069847371936796_1598263918267&_=1598263919443
import requests
from lxml import etree
import time
import re
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}
url3='https://www.autohome.com.cn/ashx/dealer/AjaxDealersBySpecId.ashx?specId=46879&cityId=340100&provinceId=340000&countyId=0&orderType=0&kindId=1&pageIndex=1&pageSize=10'
data3=requests.get(url3,headers=headers).content.decode('gbk')
with open('2.txt','w',encoding='utf-8')as f:
    f.write(data3)






