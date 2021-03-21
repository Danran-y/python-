#coding: utf-8
#@Time    : 2020/10/31 9:28
#@Author  : Danran_y
#@FileName: open文档测试.py
#@Software: PyCharm
import requests
from lxml import etree
import re
data=open('1.txt',encoding='utf-8').read()
# 0   &#xee0c
# 1   1
# 2   &#xe030
# 3   &#xe882
# 4   &#xe6a5
# 5   &#xf236
# 6   &#xf2b3
# 7   &#xef20
# 8   &#xe05c
# 9  &#xf23b

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
        dict['title']=html.xpath('string(//div[@id="shop-all-list"]/ul/li['+str(i+1)+']/div[2]/div[1]/a//h4)')#店名
        dict['pingfen']=html.xpath('string(//*[@id="shop-all-list"]/ul/li['+str(i+1)+']/div[2]/div[2]/div/div[2])')#评分
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
        dict['address']=address0[i]
        dict['url2']=html.xpath('string(//div[@id="shop-all-list"]/ul/li['+str(i+1)+']/div[2]/div[1]/a/@href)')#链接url
        print(dict)
    except:
        continue


#￥\ue0301\ue882
#\ue030\uee0c\ue05c1
# data=open('1.txt',encoding='utf-8').read()
# import re
# data1=re.findall('<svgmtsi class="shopNum">(.*?);',data)
# print(data1)