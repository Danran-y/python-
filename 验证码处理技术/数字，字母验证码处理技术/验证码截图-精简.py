from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytesseract  # 用于图片转文字
import time
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字

driver = webdriver.Chrome()
driver.get('http://211.86.128.194/suzxyjw/cas/login.action')
# # 对目标网页进行截屏。这里截的是全屏
# driver.save_screenshot('full_snap.png')# 对目标网页进行截屏。这里截的是全屏
# page_snap_obj = Image.open('full_snap.png')#打开截图
# img = driver.find_element_by_id('randpic')# 对验证码所在位置进行定位，然后截取验证码图片，定位到class标签
# location = img.location
# size = img.size
# left = location['x']
# top = location['y']
# right = left + size['width']
# bottom = top + size['height']
# image_obj = page_snap_obj.crop((left, top, right, bottom))
# image_obj.show()