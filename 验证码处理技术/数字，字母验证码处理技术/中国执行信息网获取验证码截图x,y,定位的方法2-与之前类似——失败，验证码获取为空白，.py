#coding=utf-8
from selenium import webdriver
import time
import re
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
opt = webdriver.ChromeOptions()   #创建浏览
# opt.set_headless()    #无窗口模式
driver = webdriver.Chrome(options=opt)  #创建浏览器对象
driver.get('http://zxgk.court.gov.cn/register') #打开网页
# driver.maximize_window()   #最大化窗口
time.sleep(2)     #加载等待
#driver.find_element_by_xpath("./*//span[@class='bg s_ipt_wr quickdelete-wrap']/input").send_keys("魅族") #利用xpath查找元素进行输入文本

driver.find_element_by_id('agreement').click()#点击事件，打对勾

driver.find_element_by_xpath("//div[@class='makesure']").click()#点击确认
# 对目标网页进行截屏。这里截的是全屏
driver.save_screenshot('full_snap.png')# 对目标网页进行截屏。这里截的是全屏
img = driver.find_element_by_id('captchaImg')# 对验证码所在位置进行定位，然后截取验证码图片，定位到class标签
location = img.location  # 获取验证码x,y轴坐标
size = img.size  # 获取验证码的长宽
rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
i = Image.open("full_snap.png")  # 打开截图
result = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
result.show()