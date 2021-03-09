import requests
from lxml import etree
import random
import re
import time
session=requests.session()
headers={

'Cookie':'_uab_collina=159902822678918121752098; JSESSIONID=C45503CDB717C41996BEB20217F1A95D; _jc_save_toStation=%u676D%u5DDE%2CHZH; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; BIGipServerotn=787481098.64545.0000; RAIL_EXPIRATION=1612462654022; RAIL_DEVICEID=Z54PSzi-u40Kw6j-tsKcOWv1EcTL2CbiyR_jpIjaF5g3TEPch85o4mHYqsBVFdqkQg5YgkF_k4d-0gYl8oYgzPwV68DcB7a6J4aEwuKH2wr65WxG4q4BkgBkDeYka2lB8ghc05VcvVHULdu7g-BTQcxGjMn-vVDt; BIGipServerpool_passport=216269322.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromDate=2021-02-01; _jc_save_toDate=2021-02-01',

'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.106Safari/537.36',
    }

url_1='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2021-02-01&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=HZH&purpose_codes=ADULT'
data=requests.get(url_1,headers=headers).content.decode('utf-8')
data1=re.findall('"result":(.*?),"flag"',data)[0].strip('[').strip(']').split(',')

for i in data1:
    # try:
        #data2，先剔除部分多余数据，使得字符串接近规范化
        #data3, 获取车次、发出时间等信息的字符串，然后转化成列表，对号入座
        #data4，获取座位的信息，
        data2 = re.findall('.*\|预订|(.*)', i)[1][14:166]#剔除多余的字符串
        #print(data2)
        data3 = re.findall('(.*)\|Y|', data2)[0]  # 获取车次等一切信息
        data3_1 = data3.split('|')#变成列表获取各个属性的信息
        car_checi = data3_1[0]
        start_time = data3_1[5]
        end_time = data3_1[6]
        car_time = data3_1[7]
        i = data3_1[3]#把代号变成文字，这部分可以优化
        if i == 'AOH':
            i = "上海虹桥"
        elif i == 'HGH':
            i = "杭州东"
        elif i == 'HZH':
            i = "杭州"
        elif i == 'SHH':
            i = "上海"
        elif i == 'XHH':
            i = "杭州南"
        elif i == 'SNH':
            i = "上海南"
        start_address = i
        i = data3_1[4]
        if i == 'AOH':
            i = "上海虹桥"
        elif i == 'HGH':
            i = "杭州东"
        elif i == 'HZH':
            i = "杭州"
        elif i == 'SHH':
            i = "上海"
        elif i == 'XHH':
            i = "杭州南"
        elif i == 'SNH':
            i = "上海南"
        end_address = i
        #print('车次：' + car_checi + '; ' + '出发站：' + start_address + '; ' + '到达站: ' + end_address + '; ' + '发车时间： ' + start_time + '; ' + '到达时间：' + end_time + '; ' + '历时： ' + car_time)
        c = ['O', '3', '4', '1']#利用一个小列表是因为每个长字符串会以这些数字或字母组成的固定字母群结尾，为了就是剔除多余字符
        #也可以用其他方法优化一下，
        for i in c:
            data4 = re.findall('|2021(.*)\|' + i, data2)
            data5 = str(data4).replace(", ", '').replace("'", '').strip('[').strip(']')[19:]
            #获取座位信息，data5
            if data5 == '':
                continue
            elif len(data5) < 50:
                data7 = data5.split("|")
                # print(data7)
                try:
                    one = data7[13]  # 商务座
                except:
                    one=''
                try:
                    two = data7[12]  # 一等座
                except:
                    two=''
                try:
                    three = data7[11]  # 二等座
                except:
                    three=''
                try:
                    four = data7[10]  # 软卧二等
                except:
                    four=''
                try:
                    five = data7[9]  # 硬座
                except:
                    five=''
                try:
                    six = data7[4]  # 软卧一等
                except:
                    six=''
                print('车次：' + car_checi + '; ' + '出发站：' + start_address + '; ' + '到达站: ' + end_address + '; ' + '发车时间： ' + start_time + '; ' + '到达时间：' + end_time + '; ' + '历时： ' + car_time+'; <--> '+'商务座:' + one + ' ; 一等座:' + two + ' ; 二等座:' + three + ' ; 软卧一等:' + six + ' ; 软卧二等:' + four + ' ; 硬座:' + five)
