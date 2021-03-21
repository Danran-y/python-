import requests
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data={
'i':'学习英语太难',
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':'16068904451128',
'sign':'00f3dcd67238f7a2c38fe33a66602a7d',
'lts':'1606890445112',
'bv':'b0ff5d17f404993192085bf8b1e93587',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTlME',
}
headers = {
    # 'Accept': 'application/json,text/javascript,*/*;q=0.01',
    # 'Accept-Encoding': 'gzip,deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '252',
    # 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=132182552.34341024;OUTFOX_SEARCH_USER_ID="963744056@10.108.160.17";_ntes_nnid=1b5c52d1e3bf62948e36770742583f6a,1606275725694;JSESSIONID=aaa_Qb42h1m8_6I5TgIyx;fanyi-ad-id=93877;fanyi-ad-closed=1;___rl__test__cookies=1606890004984',
    # 'Host': 'fanyi.youdao.com',
    # 'Origin': 'http',
    'Referer': 'http',
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/86.0.4240.198Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
r=requests.post(url,data=data,headers=headers).content.decode('utf-8')
print(r)