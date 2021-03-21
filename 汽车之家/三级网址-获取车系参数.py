import requests
from lxml import etree
import time
import re
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}
url3='https://www.autohome.com.cn/spec/46878/#pvareaid=3454492'
data3=requests.get(url3,headers=headers).content.decode('gbk')
html3=etree.HTML(data3)
#车系详细参数
cars_type=html3.xpath('//div[@class="spec-param"]/div[2]/div/div/p/text()')#车型参数
cars_type_name=html3.xpath('//div[@class="spec-param"]/div[2]/div/div/span/text()')#车型参数名称
#print(cars_type_name[0]+': '+cars_type[0]+', '+cars_type_name[1]+': '+cars_type[1]+', '+cars_type_name[2]+': '+cars_type[2]+', '+cars_type_name[3]+': '+cars_type[3]+', '+cars_type_name[4]+': '+cars_type[4]+', '+cars_type_name[5]+': '+cars_type[5]+', '+cars_type_name[6]+': '+cars_type[6])
shop_4s=html3.xpath('//div[@class="dealer-list"]/div/div/a')
print(shop_4s)






