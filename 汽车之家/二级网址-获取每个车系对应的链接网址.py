# https://api.mall.autohome.com.cn/gethomead/340600?_appid=car&callback=jQuery17206069847371936796_1598263918267&_=1598263919443
import requests
from lxml import etree
import time
import re
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}
url2='https://www.autohome.com.cn/5695/#levelsource=000001000_0&pvareaid=101594'
data2=requests.get(url2,headers=headers).content.decode('gbk')
html2=etree.HTML(data2)
car_name=html2.xpath('//div[@class="spec-wrap active"]/dl/dd/div/div/p/a/text()')
car_href=html2.xpath('//div[@class="spec-wrap active"]/dl/dd/div/div/p/a/@href')

for i in range(10):
   try:
       if car_href[i] != '':
           car_type_url = 'https://www.autohome.com.cn' + car_href[i]
           car_ID=re.findall('https://www.autohome.com.cn/spec/(.*?)/#',car_type_url)[0]#获取每款车系的id，便于构造4s链接网址
           print(car_name[i]+';'+car_type_url)
           print(car_ID)

       else:
           continue
   except:
       continue







