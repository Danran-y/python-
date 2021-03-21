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
                    data3 = requests.get(url3, headers=headers).content.decode('gbk')
                    html3 = etree.HTML(data3)
                    # 车系详细参数
                    cars_type = html3.xpath('//div[@class="spec-param"]/div[2]/div/div/p/text()')  # 车型参数
                    cars_type_name = html3.xpath('//div[@class="spec-param"]/div[2]/div/div/span/text()')  # 车型参数名称
                    print(car_name[j]+': '+cars_type_name[0] + ': ' + cars_type[0] + ', ' + cars_type_name[1] + ': ' + cars_type[
                        1] + ', ' + cars_type_name[2] + ': ' + cars_type[2] + ', ' + cars_type_name[3] + ': ' +
                          cars_type[3] + ', ' + cars_type_name[4] + ': ' + cars_type[4] + ', ' + cars_type_name[
                              5] + ': ' + cars_type[5] + ', ' + cars_type_name[6] + ': ' + cars_type[6])
                else:
                    continue
            except:
                continue

    except:
        continue




