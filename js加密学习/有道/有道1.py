import requests
import time, random
import requests
session = requests.session()




ts = str(int((time.time()*1000)))
salt = str(ts) + str(random.randint(0, 10))

print (ts)
print (salt)



def getmd5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()
    return sign

def getSign(key, salt):

    sign = "fanyideskweb" + str(key) + str(salt) + "]BjuETDhU)zqSxf-=B#7m"

    sign = getmd5(sign)
    return sign

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': getSign(key, salt),
        'lts': ts,
        'bv': 'b0ff5d17f404993192085bf8b1e93587',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',

    }
    headers = {

        'Cookie': 'Cookie: OUTFOX_SEARCH_USER_ID_NCOO=132182552.34341024; OUTFOX_SEARCH_USER_ID="963744056@10.108.160.17"; _ntes_nnid=1b5c52d1e3bf62948e36770742583f6a,1606275725694; JSESSIONID=aaa_Qb42h1m8_6I5TgIyx; fanyi-ad-id=93877; fanyi-ad-closed=1; ___rl__test__cookies=1606902525069',
        # 'Host': 'fanyi.youdao.com',
        # 'Origin': 'http',
        'Referer': 'http',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/86.0.4240.198Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    result =requests.post(url=url, data=data, headers=headers)
    print (result.text)


if __name__ == '__main__':
    youdao("好人")