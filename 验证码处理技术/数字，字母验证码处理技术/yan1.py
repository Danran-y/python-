from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字

def get_snap(driver):  # 对目标网页进行截屏。这里截的是全屏
    driver.save_screenshot('full_snap.png')
    page_snap_obj = Image.open('full_snap.png')
    return page_snap_obj


def get_image(driver):  # 对验证码所在位置进行定位，然后截取验证码图片
    img = driver.find_element_by_id('btnSendCheckCode')
    time.sleep(2)
    location = img.location
    size = img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    page_snap_obj = get_snap(driver)
    image_obj = page_snap_obj.crop((left, top, right, bottom))
    # image_obj.show()
    return image_obj  # 得到的就是验证码
def start():
    driver = webdriver.Chrome()
    driver.get('http://zxgk.court.gov.cn/register')
    driver.find_element_by_id('agreement').click()  # 点击事件，打对勾

    driver.find_element_by_xpath("//div[@class='makesure']").click()  # 点击确认

    image1 = get_image(driver)
    image1.show()  # 可以开启这行，查看所截取的验证码图片是否正确


if __name__ == '__main__':
    start()