#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib.request
import re
import winroute.winroute as winroute




def getcnip():
    url = "http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest"
    f = urllib.request.urlopen(url)
    #print (f.read())
    s=f.read().decode('utf-8')#.split('\n')
    
    cnregex=re.compile(r'apnic\|CN\|ipv4\|[0-9\.]+\|[0-9]+\|[0-9]+\|a.*',re.IGNORECASE)
    cndata=cnregex.findall(s)
    cniplist=[]
    #print(s)
    for i in cndata:
        tmplist=[]
    #    print(i)
        area = i.split('|')[1]
        ip = i.split('|')[3]
        pc = i.split('|')[4]
        k = 0
        while k < 32:
            if 2**k == int(pc):
                tmpnum = 32-k
                if tmpnum>0:
                    m='1'
                    for n in range(tmpnum-1):
                        m=m+"1"
                m=m.zfill(32)[::-1]
                m1=m[0:8]
                
                m1=int(m1,2)
                m2=m[8:16]
                
                m2=int(m2,2)
                m3=m[16:24]
               
                m3=int(m3,2)
                m4=m[24:32]
                
                m4=int(m4,2)            
                mask=str(m1)+"."+str(m2)+"."+str(m3)+"."+str(m4)
                #print(mask)
                           
                
                #print ("%s\t\t%s\t\t%s" % (area, ip, mask))
                tmplist=[ip,mask]
                cniplist.append(tmplist)
                break
            k += 1    
    return cniplist


def upgradecnip():
    
    print("正在更新CNip地址........")
    

    cnip= getcnip()

    f = open('cnip.txt','w') 
    for i in cnip:
        print (i[0],i[1],file=f)  #输出至文件,print会自动添加空格，用于后面的分割
        #print (cnip)
    print("IP地址更新完毕!")
    f.close()
    
def readcnip():
    tmp=[]
    try:
        f = open('cnip.txt','r') 
        cnip=f.read()
        #print (cnip)
        cnip=cnip.split('\n')
        for i in cnip:
            if len(i)>=2:
                dest=i.split(' ')[0]
                mask=i.split(' ')[1]
                tmp1=[dest,mask]
                #print (dest,mask)  
                tmp.append(tmp1)
        return tmp
                
    except:
        print("文件读取异常，重新获取CN的IP地址")
        upgradecnip()
        print("更新完成，请重新启动")
    
def wtroute():
    route=winroute.WinRoute()
    iplist=readcnip()
    print ("正在写入route")
    for i in iplist:
        route.CreateIpForwardEntry(i[0], i[1],dwForwardMetric=5)
    print ("完成")
        
up=input("是否更新CNip地址，建议每隔一段时间更新一次（Y/N)?")
while up!="Y" and up!="N" and up!="y" and  up!="n":
    up = input("输入错误请重新输入是否更新CNip地址，建议每隔一段时间更新一次（Y/N)?")
if up=="Y" or up=="y":
    upgradecnip()
if up=="N" or up=="n":
    pass

rt=input("是否开始写入路由(Y/N)?")

while rt!="Y" and rt!="N" and rt!="y" and  rt!="n":
    rt = input("输入错误请重新输入是否更新CNip地址，建议每隔一段时间更新一次（Y/N)?")
if rt=="Y" or rt=="y":
    wtroute()
    
    
if rt=="N" or rt=="n":
    pass

    
