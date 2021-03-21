#汽车之家-简单获取车系对应的小的类别的所售4s店以及车系参数
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
                    # url3_1是真正的4s店对应的网址，只需要对应的车系ID，进行构造
                    url3_1 = 'https://www.autohome.com.cn/ashx/dealer/AjaxDealersBySpecId.ashx?specId=' + str(car_ID) + '&cityId=340100&provinceId=340000&countyId=0&orderType=0&kindId=1&pageIndex=1&pageSize=10'
                    data3 = requests.get(url3_1, headers=headers).content.decode('gbk')
                    shop_4s = re.findall('"companySimple":"(.*?)"', data3)
                    address1 = re.findall('"countyName":"(.*?)"', data3)
                    address2 = re.findall('"address":"(.*?)"', data3)
                    price = re.findall('"minNewsPrice":(.*?),"minOriginalPrice', data3)
                    #data4是指请求每个具体车系的网址所获得文本内容（请求三级网址）
                    data4 = requests.get(url3, headers=headers).content.decode('gbk')
                    html3 = etree.HTML(data4)
                    # 获得车系详细参数列表cars_type，cars_type_name
                    cars_type = html3.xpath('//div[@class="spec-param"]/div[2]/div/div/p/text()')  # 车型参数
                    cars_type_name = html3.xpath('//div[@class="spec-param"]/div[2]/div/div/span/text()')  # 车型参数名称

                    for k in range(20):#目的是每输出一个4s店也把车的参数带上
                        try:
                            print(car_name[j]+': '+shop_4s[k] + '; ' + address1[k] + '; ' + address2[k] + '; ' + price[k]+'------'+cars_type_name[0] + ': ' + cars_type[0] + ', ' + cars_type_name[1] + ': ' + cars_type[
                        1] + ', ' + cars_type_name[2] + ': ' + cars_type[2] + ', ' + cars_type_name[3] + ': ' +
                          cars_type[3] + ', ' + cars_type_name[4] + ': ' + cars_type[4] + ', ' + cars_type_name[
                              5] + ': ' + cars_type[5] + ', ' + cars_type_name[6] + ': ' + cars_type[6])
                        except:
                            continue
                else:
                    continue
            except:
                continue

    except:
        continue




