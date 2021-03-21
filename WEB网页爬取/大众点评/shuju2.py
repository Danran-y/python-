#coding: utf-8
#@Time    : 2020/10/31 17:01
#@Author  : Danran_y
#@FileName: shuju2.py
#@Software: PyCharm

#//*[@id="shop-all-list"]/ul/li[1]/div[2]/div[2]/text()
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

html=etree.HTML(data)







def count(l,price):
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
            count = '0'
    price4 = ''.join(l)

#count(l=price,price4)
for i in range(1,16):
    price4='34'
    # 获取含有‘1’的列表，目的是使价格完整，正确
    price3 =html.xpath('//*[@id="shop-all-list"]/ul/li[' + str(i) + ']/div[2]/div[2]/a[2]/b/text()')
    # if price3!=[]:
    #     price3.insert(1,price4)
    #     price5=''.join(price3)
    #     print(price5)
    print(price3)
