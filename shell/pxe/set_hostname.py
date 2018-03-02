#!/usr/bin/python
#coding:utf-8
import socket,os
#前面是主机名，后面是ip的最后一位地址
t7={'ip':'77','hostname':'t7.alv.pub'}
t8={'ip':'78','hostname':'t8.alv.pub'}

hosts=[t7,t8]

ip=socket.gethostbyname(socket.gethostname())
lastIPNumber=ip.split('.')[-1]

for i in hosts:
    if lastIPNumber == i['ip']:
        os.system('hostnamectl set-hostname %s'%i['hostname'])
        break
    else:
        os.system('hostnamectl set-hostname %s'%lastIPNumber+'.alv.pub')

#