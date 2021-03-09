import re
data=open('2.txt',encoding='utf-8').read()
#"companySimple":"合肥众国泓通汽车","address":"合肥市新站区物流大道777号",
#"minNewsPrice":219900,"minOriginalPrice":219900,"maxOriginalPrice":219900,
shop_4s=re.findall('"companySimple":"(.*?)"',data)
address1=re.findall('"countyName":"(.*?)"',data)
address2=re.findall('"address":"(.*?)"',data)
price=re.findall('"minNewsPrice":(.*?),"minOriginalPrice',data)
for k in range(20):
    try:
        print(shop_4s[k]+'; '+address1[k]+'; '+address2[k]+'; '+price[k])
    except:
        continue