import re  # 用于正则
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
from selenium import webdriver  # 用于打开网站
import pytesseract.pytesseract

import time  # 代码运行停顿
img=Image.open('image/7785.jpg')
img2=img.convert('RGB')
a=pytesseract.image_to_string(img2,lang='chi_sim')
print(a)
#lang='chi_sim'