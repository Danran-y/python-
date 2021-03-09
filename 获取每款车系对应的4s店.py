# https://api.mall.autohome.com.cn/gethomead/340600?_appid=car&callback=jQuery17206069847371936796_1598263918267&_=1598263919443
import requests
from lxml import etree
import time
import re
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}
url='https://api.mall.autohome.com.cn/gethomead/340600?_appid=car&callback=jQuery17209573280535509359_1598264452669&_=1598264453778'
data=requests.get(url,headers=headers).content.decode('utf-8')
shopname=re.findall('"providerName":"(.*?)"',data)
seriesId_data=re.findall('"seriesId":(.*?)\,"url"',data)
for i in range(200):
    try:
        car_url='https://www.autohome.com.cn/'+seriesId_data[i]+'/#levelsource=000001000_0&pvareaid=101594'#获取各个品牌旗舰店链接
        data2 = requests.get(car_url, headers=headers).content.decode('gbk')
        html2 = etree.HTML(data2)
        car_name = html2.xpath('//div[@class="spec-wrap active"]/dl/dd/div/div/p/a/text()')#获取车子类型名称
        car_href = html2.xpath('//div[@class="spec-wrap active"]/dl/dd/div/div/p/a/@href')#获取车子类型对应的链接
        for j in range(10):
            try:
                if car_href[j] != '':
                    url3 = 'https://www.autohome.com.cn' + car_href[i]#获取车子类型对应的链接（可称为二级网址）
                    car_ID = re.findall('https://www.autohome.com.cn/spec/(.*?)/#', url3)[0]  # 获取每款车系的id，便于构造4s链接网址
                    #url3_1是真正的4s店对应的网址，只需要对应的车系ID，进行构造
                    url3_1 = 'https://www.autohome.com.cn/ashx/dealer/AjaxDealersBySpecId.ashx?specId='+str(car_ID)+'&cityId=340100&provinceId=340000&countyId=0&orderType=0&kindId=1&pageIndex=1&pageSize=10'
                    data3 = requests.get(url3_1, headers=headers).content.decode('gbk')
                    shop_4s = re.findall('"companySimple":"(.*?)"', data3)
                    address1 = re.findall('"countyName":"(.*?)"', data3)
                    address2 = re.findall('"address":"(.*?)"', data3)
                    price = re.findall('"minNewsPrice":(.*?),"minOriginalPrice', data3)
                    for k in range(20):
                        try:
                            print(shop_4s[k] + '; ' + address1[k] + '; ' + address2[k] + '; ' + price[k])
                        except:
                            continue
                else:
                    continue
            except:
                continue

    except:
        continue




