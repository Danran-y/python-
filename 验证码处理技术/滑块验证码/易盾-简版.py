'''先加速后减速'''
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import random
from selenium.webdriver import ActionChains


opt = webdriver.ChromeOptions()   #创建浏览
# opt.set_headless()    #无窗口模式
driver = webdriver.Chrome(options=opt)  #创建浏览器对象
time.sleep(1)

driver.get('https://dun.163.com/trial/jigsaw',) #打开网页
action = ActionChains(driver)
# driver.maximize_window()   #最大化窗口
#driver.find_element_by_xpath("./*//span[@class='bg s_ipt_wr quickdelete-wrap']/input").send_keys("魅族") #利用xpath查找元素进行输入文本
# driver.find_element_by_id('kw').send_keys("小米") #候选方法
time.sleep(2)
driver.find_element_by_xpath('//ul[@class="tcapt-tabs__container"]/li[2]').click()#点击按钮，开始出现图片
time.sleep(7)
huakuai=driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div[2]')#需要滑动的元素
def get_track(distance):      # distance为传入的总距离
    # 移动轨迹
    track=[]
    # 当前位移
    current=0
    # 减速阈值
    mid=distance*4/5
    # 计算间隔
    t=0.2
    # 初速度
    v=0

    while current<distance:
        if current<mid:
            # 加速度为2
            a=2
        else:
            # 加速度为-2
            a=-3
        v0=v
        # 当前速度
        v=v0+a*t
        # 移动距离
        move=v0*t+1/2*a*t*t
        # 当前位移
        current+=move
        # 加入轨迹
        track.append(round(move))
    return track
def move_to_gap(slider,tracks):     # slider是要移动的滑块,tracks是要传入的移动轨迹
    ActionChains(driver).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(driver).move_by_offset(xoffset=x,yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(driver).release().perform()

if __name__ == '__main__':
    move_to_gap(huakuai,get_track(340))