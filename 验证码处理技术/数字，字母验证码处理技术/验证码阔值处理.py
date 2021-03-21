#################阙值化处理后的图像,图片背景为白色############
# 模式“L”为灰色图像，它的每个像素用8个bit表示，
# 0表示黑，255表示白，其他数字表示不同的灰度，
# 转换为灰度图，以便后面提取文本
import re  # 用于正则
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
from selenium import webdriver  # 用于打开网站
import pytesseract.pytesseract
img=Image.open('image/8.png')
gray = img.convert('L')
gray.save('image/8-1.png')
