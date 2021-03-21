#coding: utf-8
#@Time    : 2020/10/31 10:28
#@Author  : Danran_y
#@FileName: 数据测试.py
#@Software: PyCharm

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
import re
data=open('1.txt',encoding='utf-8').read()
#评论人数的zhengze
list=[]
list2=[]
l2=re.findall('<b><svgmtsi class="shopNum">.*</svgmtsi></b>',data)#评论人数的zhengze
print(len(l2))
# l3=re.findall('<b>￥<svgmtsi class="shopNum">.*</svgmtsi></b>',data)#价格
# for j in l2:
#     print(j)
#     l=re.findall('<svgmtsi class="shopNum">(.*?);',j)
#     for i in range(len(l)):
#         if l[i] == '&#xee0c':
#             l[i] = '0'
#         elif l[i] == '1':
#             l[i] = '1'
#         elif l[i] == '&#xe030':
#             l[i] = '2'
#         elif l[i] == '&#xe882':
#             l[i] = '3'
#         elif l[i] == '&#xe6a5':
#             l[i] = '4'
#         elif l[i] == '&#xf236':
#             l[i] = '5'
#         elif l[i] == '&#xf2b3':
#             l[i] = '6'
#         elif l[i] == '&#xef20':
#             l[i] = '7'
#         elif l[i] == '&#xe05c':
#             l[i] = '8'
#         elif l[i] == '&#xf23b':
#             l[i] = '9'
#
#         else:
#             count = 0
#
#     count=''.join(l)
#     list.append(count)
# print(list)
# for j in l3:
#     l=re.findall('<svgmtsi class="shopNum">(.*?);',j)
#     for i in range(len(l)):
#         if l[i] == '&#xee0c':
#             l[i] = '0'
#         elif l[i] == '1':
#             l[i] = '1'
#         elif l[i] == '&#xe030':
#             l[i] = '2'
#         elif l[i] == '&#xe882':
#             l[i] = '3'
#         elif l[i] == '&#xe6a5':
#             l[i] = '4'
#         elif l[i] == '&#xf236':
#             l[i] = '5'
#         elif l[i] == '&#xf2b3':
#             l[i] = '6'
#         elif l[i] == '&#xef20':
#             l[i] = '7'
#         elif l[i] == '&#xe05c':
#             l[i] = '8'
#         elif l[i] == '&#xf23b':
#             l[i] = '9'
#
#         else:
#             count = 0
#
#     count=''.join(l)
#
#     list2.append(count)


