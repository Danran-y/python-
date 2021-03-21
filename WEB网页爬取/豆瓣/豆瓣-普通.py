# https://api.mall.autohome.com.cn/gethomead/340600?_appid=car&callback=jQuery17206069847371936796_1598263918267&_=1598263919443
import requests
from lxml import etree
import time
import random
Proxies = [
'http://196.55.16.153:80',
'http://91.205.174.26:80',
'http://52.179.18.244:8080',

]
IP = random.choice(Proxies)
proxies = {'http': IP}
headers={

#'Cookie': 'bid=t6d23ld61Zw; __gads=ID=12ca80cb48e3e52f:T=1593656932:S=ALNI_MbIDq-BTor-bdT8nqVorqekNc762w; viewed="34761976"; gr_user_id=cba25964-9a7f-4665-9821-eee11ee59319; _vwo_uuid_v2=DE6A6F7B22BEFBF90846F595B243C8BF3|41649f3ac48d75666f45576547ed62f6; douban-fav-remind=1; ll="118188"; _ga=GA1.3.712207471.1593656933; _gid=GA1.3.1369960358.1598741255; dbcl2="222519846:scX3najSg8Q"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22251; gr_cs1_15f5bf99-8414-44f6-9e3e-4944b8789600=user_id%3A0; ap_v=0,6.0; __utmc=30149280; __utmt_douban=1; ck=5Tef; __utmt=1; __utma=30149280.382195684.1598741237.1598752196.1598752237.5; __utmz=30149280.1598752237.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=d4eca47d-90ad-482b-b430-befced013716; gr_cs1_d4eca47d-90ad-482b-b430-befced013716=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_d4eca47d-90ad-482b-b430-befced013716=true; __utmb=30149280.7.10.1598752237; _pk_ref.100001.a7dd=%5B%22%22%2C%22%22%2C1598752286%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.a7dd=*; _pk_id.100001.a7dd=8245f16241fcd9db.1598741256.4.1598752341.1598746732.',
'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.106Safari/537.36',


}
for n in range(100):

        m=n*20
        url='https://book.douban.com/tag/%E6%97%85%E8%A1%8C?start='+str(m)+'&type=T'
        r = requests.get(url=url, headers=headers).content.decode('utf-8')
        html=etree.HTML(r)
        print('开始查询第%d页' % (n + 1))
        for i in range(1, 21):
            name = html.xpath('string(//*[@id="subject_list"]/ul/li[' + str(i) + ']/div[2]/h2/a/@title)')
            pub = html.xpath('string(//*[@id="subject_list"]/ul/li[' + str(i) + ']/div[2]/div[1])').replace('\n', '').replace(' ', '')
            rating_nums = html.xpath('string(//*[@id="subject_list"]/ul/li[' + str(i) + ']/div[2]/div[2]/span[2])')  # 评分
            with open('旅行.txt', 'a', encoding='utf-8')as f:
                f.write(str(m+i)+'----'+name + '----' + pub + '----' + rating_nums+'\n')
            print(str(m+i)+'----'+name + '----' + pub + '----' + rating_nums+'\n')








