#coding: utf-8
#@Time    : 2020/11/1 9:34
#@Author  : Danran_y
#@FileName: 顾客评论文笔处理.py
#@Software: PyCharm

from lxml import etree
import re
data=open('2.txt',encoding='utf-8').read()
import json
d=json.loads(data)
d1=d['reviewAllDOList']
for i in d1:#获取每个顾客评论数据所在字典
    time=i['reviewDataVO']['addTimeVO']
    pingl=i['reviewDataVO']['reviewBodyBrief']
    pingl2 = i['reviewDataVO']['reviewBody']
    pingl3 = i['reviewDataVO']['reviewBodyHidden']
    d2=re.findall('<svgmtsi class="review">.*?;</svgmtsi>',pingl)
    d3 = re.findall('<svgmtsi class="review">.*?;</svgmtsi>', pingl2)
    d4 = re.findall('<svgmtsi class="review">.*?;</svgmtsi>', pingl3)
    for j in d2:
        pingl=pingl.replace(j,'')
    print(pingl)
    for j in d3:
        pingl2=pingl2.replace(j,'')
    print(pingl2)
    for j in d4:
        pingl3=pingl3.replace(j,'')
    print(pingl3)
    break