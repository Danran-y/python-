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
    img = driver.find_element_by_class_name('code')
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
    driver.get('https://www.zhipin.com/captcha/popUpCaptcha?redirect=https%3A%2F%2Fwww.zhipin.com%2Fgongsi%2F38bd5c757efa4ab6331z.html%3Fka%3Dindex_rcmd_companylogo_6_custompage')
    # 当爬取zhipin.com 出现验证码时，进入任何一个公司首页都需要验证码，这里拿的是要进入网易的公司首页时显示的验证链接
    #wait = WebDriverWait(driver, 10)
    #time.sleep(3)
    image1 = get_image(driver)
    #image1.show()  # 可以开启这行，查看所截取的验证码图片是否正确
    image1.save('image1.png')

if __name__ == '__main__':
    start()