# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:54:51 2020

@author: hp
"""
import re
import urllib.request as r  
import hanzhi as py #导入自己写好的汉字转换拼音的函数包
a=["成都","深圳","宜宾","广西","武汉","南昌","南充","攀枝花","珠江","重庆","西藏",
   "贵州","广汉","邻水","北京","天津","大理","黑龙江","安徽","山西","江苏","湘西",
   "香港","兰州","台湾","湖南","湖北","达州","广安","惠州"]

b=""
for i in range(len(a)):
    c=str(py.pingyin(a[i]))
    url="http://api.openweathermap.org/data/2.5/weather?q="+c+"&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996"#    data=r.urlopen(url).read().decode("utf-8")
    data=r.urlopen(url).read().decode("utf-8","ignore")
    temp=re.compile('"temp":(.*?),').findall(data)
    description=re.compile('"description":(.*?),').findall(data)
    pressure=re.compile('"pressure":(.*?),').findall(data)
    b+="城市名字："+str(a[i])+"，温度："+str(temp)+"，天气状况："+str(description)+"，气压："+str(pressure)
    
#写入txt文件
f=open("城市天气状况.txt","w",encoding="utf-8")
f.write(b)
f.close()

    
    
    
    
    
    
    