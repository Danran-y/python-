import requests
import re
import json
session=requests.session()
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}
url=('https://wkretype.bdimg.com/retype/text/9a41886f26d3240c844769eae009581b6bd9bd6e?md5sum=de679a1e4f76df8ac8366bd7663285d6&sign=00fde7dc85&callback=cb&pn=1&rn=4&type=txt&rsign=p_4-r_0-s_896f2&_=1593157742792')
content_url=url
#content=json.loads(session.get(content_url).content.decode('utf-8'))
#a=json.loads(session.get(content_url))
a=session.get(content_url)
#b=eval(a.text)
#cb([{"parags":[{"c":"?#Filename
b=session.get(url).content.decode('utf-8')[2:]
c=eval(b)
print(c)
result=''

for item in c:
    for i in item['parags']:
        result+=i['c'.replace('\\r','\r').replace('\\n','\n')]
filename =  '1.txt'

with open(filename, 'w', encoding='utf-8') as f:
    f.write(result)












