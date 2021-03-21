url='http://211.86.128.194/suzxyjw/cas/login.action'
import requests
from lxml import etree
data=requests.get(url).text

html=etree.HTML(data)
yan=html.xpath('//div[@class="div_random"]/img/@src')
print(yan)
############
yan2=re.findall('(.*)Aug',yan)[0]
r=requests.get(yan2)
with open('image/1.png','wb')as f:
    f.write(r.content)
img=Image.open('image/1.png')
yan3=pytesseract.image_to_string(img)

driver.find_element_by_xpath("//input[@id='randnumber']").send_keys(str(yan3))
driver.find_element_by_xpath("//input[@id='login']").click()#点击按钮
