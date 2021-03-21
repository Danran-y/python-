#coding=utf-8
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time
import random
import time
from selenium.webdriver import ActionChains
opt = webdriver.ChromeOptions()   #创建浏览
# opt.set_headless()    #无窗口模式
driver = webdriver.Chrome(options=opt)  #创建浏览器对象
time.sleep(1)
driver.get('https://promotion.aliyun.com/ntms/act/captchaIntroAndDemo.html') #打开网页
# driver.maximize_window()   #最大化窗口
#driver.find_element_by_xpath("./*//span[@class='bg s_ipt_wr quickdelete-wrap']/input").send_keys("魅族") #利用xpath查找元素进行输入文本
# driver.find_element_by_id('kw').send_keys("小米") #候选方法
time.sleep(15)
need_move_span =driver.find_element_by_id('nc_1_n1z')#点击按钮，开始出现图片

# 模拟按住鼠标左键
from selenium.webdriver import ActionChains

action = ActionChains(driver)

source=driver.find_element_by_id('nc_1_n1z')#需要滑动的元素
action.click_and_hold(source).perform()  #鼠标左键按下不放
action.move_by_offset(340,0)#需要滑动的坐标
action.release().perform() #释放鼠标



