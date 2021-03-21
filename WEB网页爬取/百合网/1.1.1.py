import requests
import re
import json
session=requests.session()
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}
url=('https://wenku.baidu.com/view/9a41886f26d3240c844769eae009581b6bd9bd6e.html?fr=search')
content=session.get(url).content.decode('gbk')
#https://wkretype.bdimg.com/retype/text/9a41886f26d3240c844769eae009581b6bd9bd6e?
# md5sum=de679a1e4f76df8ac8366bd7663285d6&
# sign=00fde7dc85&
# callback=cb&
# pn=1&
# rn=4&
# type=txt&
# rsign=p_4-r_0-s_896f2&
# _=1593130632062
#--------------------------------------


#https://wenku.baidu.com/api/doc/getdocinfo?
# callback=cb&
doc_id='9a41886f26d3240c844769eae009581b6bd9bd6e'
# t=1593130632443&
# _=1593130632060
url2=('https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=9a41886f26d3240c844769eae009581b6bd9bd6e&t=1593157743332&_=1593157742790')
content_url='https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id={}'.format(doc_id)
r2=session.get(url2,headers=headers).content.decode('gbk')
md5sum=re.findall('"md5sum":"(.*?)"',r2)[0]#&md5sum=de679a1e4f76df8ac8366bd7663285d6&sign=00fde7dc85
#md5sum+sign
rsign=re.findall('"rsign":"(.*?)"',r2)[0]#p_4-r_0-s_896f2
rn=re.findall('"totalPageNum":"(.*?)"',r2)[0]#4
pn=re.findall('"valueCount":(.?)',r2)[0]#1
print(pn)