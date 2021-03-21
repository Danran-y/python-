import  os
import requests
session=requests.session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
}
f=open('熊出没/x.m3u8')
url=f.read()
a=url.split('\n')
for j in range(200):
    m=j+1
    path=os.mkdir('熊出没/m/熊出没第%d集'%m)
    try:
        r1 = session.get(a[j], headers=headers).content.decode('utf-8')
        b = r1.split("\n")
        for i in range(1000):
            try:
                if i < 5:
                    continue
                elif i % 2 == 0:
                    #print(url[:343] + str(b[i]))
                    url_ts = url[:343] + str(b[i])
                    r2 = session.get(url_ts, headers=headers)
                    if i < 10:
                        n = '000' + str(i)
                    elif i < 100:
                        n = '00' + str(i)
                    else:
                        n = '0' + str(i)
                    with open('熊出没/m/熊出没第%d集/'%m+n+'.ts', 'wb')as f:
                        f.write(r2.content)
                elif i % 2 == 1:
                    continue
                else:
                    break
            except:
                break
        path2 = 'copy /b F:\python\网络爬虫基础\movie\MP4\熊出没\m\熊出没第' + str(
            m) + '集\*.ts F:\python\网络爬虫基础\movie\MP4\熊出没\熊出没第' + str(m) + '集' + '.mp4'
        movie = os.popen(path2).read()
        print(movie)

        print('成功下载熊出没第%d集' % (m))

    except:
        break




