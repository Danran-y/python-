import requests
from lxml import etree
import time
import random
import re
headers={
'Accept':'application/json',
'Accept-Encoding':'gzip,deflate,br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Content-Length':'1917',
'Content-Type':'application/json',
'Cookie':'bid=t6d23ld61Zw; __gads=ID=12ca80cb48e3e52f:T=1593656932:S=ALNI_MbIDq-BTor-bdT8nqVorqekNc762w; viewed="34761976"; gr_user_id=cba25964-9a7f-4665-9821-eee11ee59319; _vwo_uuid_v2=DE6A6F7B22BEFBF90846F595B243C8BF3|41649f3ac48d75666f45576547ed62f6; douban-fav-remind=1; _ga=GA1.3.712207471.1593656933; _gid=GA1.3.1369960358.1598741255; dbcl2="222519846:scX3najSg8Q"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22251; ct=y; ll="118163"; _ga=GA1.2.382195684.1598741237; _gid=GA1.2.1416367300.1598859500; ck=5Tef; ap_v=0,6.0; __utma=30149280.382195684.1598741237.1598862248.1598944562.10; __utmc=30149280; __utmz=30149280.1598944562.10.9.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.2.10.1598944562; _pk_ref.100001.a7dd=%5B%22%22%2C%22%22%2C1598944567%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.a7dd=*; _gat=1; _pk_id.100001.a7dd=8245f16241fcd9db.1598741256.8.1598944579.1598859101.f',
'Host':'read.douban.com',
'Origin':'https://read.douban.com',
'Referer':'https://read.douban.com/tag/%E8%81%8C%E4%B8%9A%E5%A5%B3%E6%80%A7/?dcs=original-womens_fiction&dcm=info-grid',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.106Safari/537.36',
'X-CSRF-Token':'5Tef',
'X-Requested-With':'XMLHttpRequest',

}
Proxies = [
'http://52.56.220.212:80',
'http://50.233.15.242:8080',
'http://3.211.65.185:80',
'http://196.54.47.179:80',
'http://105.27.238.167:80',
'http://3.11.214.31:80',
'http://196.52.250.118:80',
]

IP = random.choice(Proxies)
proxies = {'http': IP}
url='https://read.douban.com/j/kind/'
#request payload 是字典形式
for n in range(1,50):
    try:

        payload={"sort":"hot","page":n,"tags":["职业女性"],"rootKind":"","query":"\n    query getFilterWorksList($works_ids: [ID!]) {\n      worksList(worksIds: $works_ids) {\n        \n    \n    title\n    cover\n    url\n    isBundle\n    coverLabel\n  \n    \n    url\n    title\n  \n    \n    author {\n      name\n      url\n    }\n    origAuthor {\n      name\n      url\n    }\n    translator {\n      name\n      url\n    }\n  \n    \n    abstract\n    editorHighlight\n  \n    \n    isOrigin\n    kinds {\n      \n    name @skip(if: true)\n    shortName @include(if: true)\n    id\n  \n    }\n    ... on WorksBase @include(if: true) {\n      wordCount\n      wordCountUnit\n    }\n    ... on WorksBase @include(if: true) {\n      \n    isEssay\n    \n    ... on EssayWorks {\n      favorCount\n    }\n  \n    \n    isNew\n    \n    averageRating\n    ratingCount\n    url\n  \n  \n  \n    }\n    ... on WorksBase @include(if: false) {\n      isColumn\n      isEssay\n      onSaleTime\n      ... on ColumnWorks {\n        updateTime\n      }\n    }\n    ... on WorksBase @include(if: true) {\n      isColumn\n      ... on ColumnWorks {\n        isFinished\n      }\n    }\n    ... on EssayWorks {\n      essayActivityData {\n        \n    title\n    uri\n    tag {\n      name\n      color\n      background\n      icon2x\n      icon3x\n      iconSize {\n        height\n      }\n      iconPosition {\n        x y\n      }\n    }\n  \n      }\n    }\n    highlightTags {\n      name\n    }\n  \n    isInLibrary\n    ... on WorksBase @include(if: false) {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on EbookWorks {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on WorksBase @include(if: true) {\n      ... on EbookWorks {\n        id\n        isPurchased\n        isInWishlist\n      }\n    }\n  \n        id\n        isOrigin\n      }\n    }\n  ","variables":{}}
        #运用post里的json=requestpayload字典数据
        data=requests.post(url,headers=headers,proxies=proxies,json=payload).content.decode('utf-8')
        print(data)
    except:
        continue





