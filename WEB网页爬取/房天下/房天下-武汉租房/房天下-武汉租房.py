import requests
from lxml import etree
import time
from PIL import Image
from lxml import etree
import requests
import re
import json
import random
import pymysql
from retrying import retry
import requests
from random import choice

db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='ttwqk123',
        port=3306,
        database='python',
    )
cursor = db.cursor()
proxie_list = [
 #ip代理
]


# stop_max_attempt_number 最大重试次数，wait_fixed 每次重试的时间，单位为毫秒
@retry(stop_max_attempt_number=10, wait_fixed=1000)
# def get_content(url,headers):
#
#     splash_url = choice(proxie_list)
#     proxies = {'http': splash_url, 'https': splash_url}
#     resp = requests.get(url, proxies=proxies, timeout=2,headers=headers)
#     return resp
def get_content(url,headers):
    for i in range(10):
        splash_url = choice(proxie_list)
        proxies = {'http': splash_url, 'https': splash_url}
        resp = requests.get(url, proxies=proxies, timeout=2,headers=headers)
        if resp.text.find('访问验证-房天下')==-1:
            return resp
        else:
            continue

def get_user_agent():
    user_agent = [
        'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.88Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'
    ]
    headers = random.choice(user_agent)
    return headers


headers={
'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.88Safari/537.36'
}
d1=requests.get(url='https://wuhan.fang.com/',headers=headers).text
h=etree.HTML(d1)
#租房
d1=h.xpath('//div[@class="newtool"]/div/div[3]//a/@href')[0]
d2=requests.get(d1,headers=headers).text
h=etree.HTML(d2)
#三种租房分类
d3=h.xpath('//div[@class="page-menu"]/ul/li/a/@href')
list=[]
for j in range(3):

#https://wuhan.zu.fang.com/house/a21-i32/
    url_0='https://wuhan.zu.fang.com'+d3[j]
    if j<2:
        for n in range(1, 101):
            url = url_0+'i3' + str(n) + '/'
            list.append(url)

    else:
        for n in range(1, 43):
            url = 'https://wuhan.zu.fang.com/house/a21-i3' + str(n) + '/'
            list.append(url)

def spider(url,path):


        headers = {
             'authority':'wuhan.zu.fang.com',
             'method':'GET',
             'path':path,
             'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip,deflate,br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'city=wuhan;global_cookie=y7xisntwii1anrf3bjwfigssn2akm2t3bk7;__utma=147393320.182544045.1615342293.1615342293.1615342293.1;__utmc=147393320;__utmz=147393320.1615342293.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);xfAdvLunbo=;searchConN=1_1615342315_570%5B%3A%7C%40%7C%3A%5D04e1f70f9c445902ed32d292ff692297;newhouse_user_guid=7C1A1ECB-7C46-B144-4B53-6C9840F3B7E0;newhouse_chat_guid=731B9988-A191-0FF4-3C2C-46E2216A205A;vh_newhouse=1_1615342371_864%5B%3A%7C%40%7C%3A%5D663802084c9432738d71afeb17f0ecdc;newhouse_ac4=1_1615342492_754%5B%3A%7C%40%7C%3A%5Db2761ea732c53ad9541420b3cc8db31c;new_search_uid=b2f50236284b2e1daef97773d70c774d;ASP.NET_SessionId=ugnsjncoidufbfr1bnadddi0;integratecover=1;Rent_StatLog=d9b71bf3-0171-497c-8f3c-b00a8cb9cbb2;g_sourcepage=zf_fy%5Elb_pc;__utmt_t0=1;__utmt_t1=1;__utmt_t2=1;Captcha=4C6C75426872514162433144555446556F423375366F2F2F65656B714968306179466244334C6637653762346E636F7075656734336369515271414F784145772F46364230394D4565464D3D;__utmb=147393320.86.10.1615342293;unique_cookie=U_y7xisntwii1anrf3bjwfigssn2akm2t3bk7*22',
            'referer': 'https://wuhan.zu.fang.com/',
            'sec-ch-ua': '"Chromium";v="88","GoogleChrome";v="88",";NotABrand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'User-Agent': get_user_agent(),
        }

        data=get_content(url,headers).text
        html0 = etree.HTML(data)
        href = html0.xpath('//div[@class="houseList"]/dl/dd/p[1]/a/@href')
        title0=html0.xpath('//div[@class="houseList"]/dl/dd/p[1]/a/text()')

        for i in range(len(href)):
            try:
                headers2 = {
                    'authority': 'wuhan.zu.fang.com',
                    'method': 'GET',
                    'path': href[i]+'?channel=1,2',
                    'scheme': 'https',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip,deflate,br',
                    'accept-language': 'zh-CN,zh;q=0.9',
                    'cookie': 'city=wuhan; global_cookie=y7xisntwii1anrf3bjwfigssn2akm2t3bk7; __utmc=147393320; searchConN=1_1615342315_570%5B%3A%7C%40%7C%3A%5D04e1f70f9c445902ed32d292ff692297; newhouse_user_guid=7C1A1ECB-7C46-B144-4B53-6C9840F3B7E0; newhouse_chat_guid=731B9988-A191-0FF4-3C2C-46E2216A205A; vh_newhouse=1_1615342371_864%5B%3A%7C%40%7C%3A%5D663802084c9432738d71afeb17f0ecdc; new_search_uid=b2f50236284b2e1daef97773d70c774d; ASP.NET_SessionId=ugnsjncoidufbfr1bnadddi0; integratecover=1; Rent_StatLog=d9b71bf3-0171-497c-8f3c-b00a8cb9cbb2; Captcha=533739644B5556552F45385043344439364267636A474855442F434F6F4F56324A3361755A5530345541633078674E6A31784B4C387436445057525A4E73536D73506A43797867574548453D; g_sourcepage=zf_fy%5Exq_pc; __utma=147393320.182544045.1615342293.1615342293.1615347937.2; __utmz=147393320.1615347937.2.2.utmcsr=wuhan.zu.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/house/i32/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmb=147393320.18.10.1615347937; unique_cookie=U_y7xisntwii1anrf3bjwfigssn2akm2t3bk7*46',
                    'referer': 'https://wuhan.zu.fang.com/integrate/i3'+str(n)+'/',
                    'sec-ch-ua': '"Chromium";v="88","GoogleChrome";v="88",";NotABrand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'User-Agent': get_user_agent(),
                }
                # 租房连接
                url1 = 'https://wuhan.zu.fang.com' + href[i]
                title=title0[i]
                print(title)
                print(url1)
                #url1='https://wuhan.zu.fang.com/chuzu/3_196762103_1.htm?rfss=1-804eb8cf27992f0b1a-6a'
                data2 = get_content(url1,headers=headers2).text

                html = etree.HTML(data2)
                #价格及押付方式
                p = html.xpath('string(//div[@class="tab-cont-right"]/div[2]/div)')

                p2 = re.findall('(.*?)（(.*?)）', p)
                if p2 == []:
                    # //div[@class="tab-cont-right tab-cont-yx"]/div[2]/div
                    p = html.xpath('string(//div[@class="tab-cont-right tab-cont-yx"]/div[2]/div)').replace(' ','').replace('\n','').replace('\t','')
                    p2 = re.findall('(.*?)\((.*?)\)', p)
                else:
                    p2 = p2
                try:
                    price = p2[0][0]

                    # 押付方式
                    unit = p2[0][1]
                except:
                    price = html.xpath('string(//div[@class="trl-item sty1"])').replace(' ', '').replace('\n',
                                                                                                        '')
                    unit = '面议'

                # 出租方式
                t1 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[3]/div[1]/div[1])')

                # 户型
                t2 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[3]/div[2]/div[1])')

                # 建筑面积
                t3 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[3]/div[3]/div[1])')
                print(t3)
                # 朝向
                t4 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[4]/div[1]/div[1])')
                # 所在楼层
                t5 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[4]/div[2]/div[1])')
                # 建筑楼层
                t6 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[4]/div[2]/div[2])')
                # 装修
                t7 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[4]/div[3]/div[1])')
                # 小区
                t8 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[5]/div[1]/div[2])').replace(' ', '').replace('\n',
                                                                                                                        '')
                # 小区位置说明：
                t9 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[5]/div[2]/div/a)').replace(' ', '').replace('\n', '')

                # 地址
                t10 = html.xpath('string(///div[@class="tab-cont clearfix"]/div/div[5]/div[3]/div[2])').replace(' ', '').replace('\n',
                                                                                                                         '')
                # 联系人
                t11 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[6]/div/div/div[3]//a)')
                if t11 == '':
                    # //div[@class="tab-cont clearfix"]/div/div[6]/div/div//span/a
                    t11 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[6]/div/div//span/a)')
                    if t11 == '':
                        t11 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[6]/div/div/div//a[1])').replace('地图','')
                    else:
                        t11 = t11

                else:
                    t11 = t11
                # 联系方式
                t12 = re.findall("agentMobile: '(.*?)'", data2)
                if t12 == []:
                    # //div[@class="tab-cont clearfix"]/div/div[6]/div/div[2]
                    t12 = html.xpath('string(//div[@class="tab-cont clearfix"]/div/div[6]/div/div[2])').replace(' ',
                                                                                                                '').replace(
                        '\n', '')
                else:
                    t12 = t12[0]
                # print(title,price, unit, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10,t11,t12,url1)
                save(title,price, unit, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10,t11,t12,url1)
            except:
                continue


def init():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS 武汉租房_三种分类(title VARCHAR (500) ,price VARCHAR (255),unit VARCHAR (255),t1 VARCHAR (255),t2 VARCHAR (255),t3 VARCHAR (255),t4 VARCHAR (255),t5 VARCHAR (255),t6 VARCHAR (255),t7 VARCHAR (255),t8 VARCHAR (500),t9 VARCHAR (500),t10 VARCHAR (500),t11 VARCHAR (255),t12 VARCHAR (255),url VARCHAR (500) primary key)
        """)

    db.commit()

def save(title,price, unit, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10,t11,t12,url1):
    cursor.execute("""
        REPLACE into 武汉租房_三种分类 (title,price, unit, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10,t11,t12,url)VALUES(
        "{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}"
        )
        """.format(title,price, unit, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10,t11,t12,url1))
    db.commit()


if __name__ == '__main__':

    #init()
    for s in list:
        url=s
        path=s.replace('https://wuhan.zu.fang.com','')
        spider(url,path)
