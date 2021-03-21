#coding=utf-8
#selenium模拟亚马逊登录
from selenium import webdriver
import time
import re

opt = webdriver.ChromeOptions()   #创建浏览
# opt.set_headless()    #无窗口模式
driver = webdriver.Chrome(options=opt)  #创建浏览器对象
driver.get('https://www.amazon.cn/ap/signin?_encoding=UTF8&openid.assoc_handle=cnflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.cn%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_gno_signout%26signIn%3D1%26useRedirectOnSuccess%3D1') #打开网页
# driver.maximize_window()   #最大化窗口

driver.find_element_by_xpath("//input[@id='ap_email']").send_keys("17856889351") #利用xpath查找元素进行输入文本

#driver.find_element_by_id('kw').send_keys("python") #候选方法
#
driver.find_element_by_xpath("//span[@class='a-button-inner']").click()#点击按钮
#time.sleep(1)#可以简单解决反爬
driver.find_element_by_xpath("//input[@id='ap_password']").send_keys("ttwqk123") #利用xpath查找元素进行输入文本

#driver.find_element_by_id('kw').send_keys("python") #候选方法

driver.find_element_by_xpath("//span[@class='a-button-inner']").click()#点击按钮
