import execjs
import requests
import json

import execjs

js = r'''
var i = "320305.131321201"
function n(r, o) {
            for (var t = 0; t < o.length - 2; t += 3) {
                var e = o.charAt(t + 2);
                e = e >= "a" ? e.charCodeAt(0) - 87 : Number(e),
                e = "+" === o.charAt(t + 1) ? r >>> e : r << e,
                r = "+" === o.charAt(t) ? r + e & 4294967295 : r ^ e
            }
            return r
        }
function a(r) {
            var t = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
            if (null === t) {
                var a = r.length;
                a > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(a / 2) - 5, 10) + r.substr(-10, 10))
            } else {
                for (var C = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), h = 0, f = C.length, u = []; f > h; h++) "" !== C[h] && u.push.apply(u, e(C[h].split(""))), h !== f - 1 && u.push(t[h]);
                var g = u.length;
                g > 30 && (r = u.slice(0, 10).join("") + u.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + u.slice(-10).join(""))
            }
            var l = void 0, d = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
            l = null !== i ? i : (i = o.common[d] || "") || "";
            for (var m = l.split("."), S = Number(m[0]) || 0, s = Number(m[1]) || 0, c = [], v = 0, F = 0; F < r.length; F++) {
                var p = r.charCodeAt(F);
                128 > p ? c[v++] = p : (2048 > p ? c[v++] = p >> 6 | 192 : (55296 === (64512 & p) && F + 1 < r.length && 56320 === (64512 & r.charCodeAt(F + 1)) ? (p = 65536 + ((1023 & p) << 10) + (1023 & r.charCodeAt(++F)), c[v++] = p >> 18 | 240, c[v++] = p >> 12 & 63 | 128) : c[v++] = p >> 12 | 224, c[v++] = p >> 6 & 63 | 128), c[v++] = 63 & p | 128)
            }
            for (var w = S, A = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), b = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), D = 0; D < c.length; D++) w += c[D], w = n(w, A);
            return w = n(w, b), w ^= s, 0 > w && (w = (2147483647 & w) + 2147483648), w %= 1e6, w.toString() + "." + (w ^ S)
        }'''

def sign(keyword):
    print(execjs.compile(js).call("a",keyword))
def spider():
    url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en&query=%E5%AD%A6%E4%B9%A0&simple_means_flag=3&sign=275626.55195&token=78a0906fa0c08a3a372f583b9642b6a9&domain=common"
    headers = {
        #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    #'cookie': 'BIDUPSID=110E294221AC9C4A459CDBBAAC38A3BB; PSTM=1603246690; BAIDUID=110E294221AC9C4AD451451634CA6DC8:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID_BFESS=110E294221AC9C4AD451451634CA6DC8:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=2; BCLID=7994709119155404827; BDSFRCVID=GZFOJexroG3STncrxpR4JFJrT_weG7bTDYLE2IcaprdK7U8VJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3h3RrX26rDHJTg5DTjhPrMQn6lWMT-MTryKKORQnrjq4nx06OkQxIX3bnfKx-fKHnRhlRNtqTjHtJ4bM4b3jkZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDMJ9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DKmejLb3e; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1605775595,1605775604,1606120034,1606120038; H_PS_PSSID=1445_33074_33059_33099_33101_32962_33115_26350_33149_22160; yjs_js_security_passport=b29d62575d0b42262b1e2a3db720ff23a344d082_1606126216_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1606126233; __yjsv5_shitong=1.0_7_c673df84c81675f69f1f6c06befb4424385b_300_1606126240150_58.240.82.178_90d99273'
        'authority': 'fanyi.baidu.com',
        'method': 'POST',
        'path': '/v2transapi?from=zh&to=en',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip,deflate,br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '129',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'cookie': 'BIDUPSID=110E294221AC9C4A459CDBBAAC38A3BB;PSTM=1603246690;BAIDUID=110E294221AC9C4AD451451634CA6DC8',
        'origin': 'https://fanyi.baidu.com',
        'referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/86.0.4240.198Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    # data = {
    #     "from": "zh",
    #     "to": "en",
    #     "query": "学习",  # query 即我们要翻译的的内容
    #     "simple_means_flag": "3",
    #     "sign": "275626.55195",  # sign 是变化的需要我们执行js代码得到
    #     "token": "78a0906fa0c08a3a372f583b9642b6a9", # token没有变化
    #     'domain': 'common'
    # }
    res=requests.get(url,headers=headers)
    print(res)

#keyword='学习'
#sign(keyword)
spider()