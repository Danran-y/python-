#coding: utf-8
#@Time    : 2020/12/6 11:30
#@Author  : Danran_y
#@FileName: 验证码处理.py
#@Software: PyCharm

from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
from selenium import webdriver  # 用于打开网站
import pytesseract.pytesseract
img=Image.open('image/BALLFE.jpg')
print(pytesseract.image_to_string(img))
