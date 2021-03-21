data=open('1.txt',encoding='utf-8').read()
data1=data.split('\n')
for i in data1:
    data2=str(i.split(':')[0].split(' ')).strip('[').strip(']')+':'+str(i.split(':')[1])+','
    print(data2)