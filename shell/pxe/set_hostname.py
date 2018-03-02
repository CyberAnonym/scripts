#!/usr/bin/python
#coding:utf-8
import socket,os,re
#前面是主机名，后面是ip的最后一位地址
t7={'ip':'77','hostname':'t7.alv.pub'}
t8={'ip':'78','hostname':'t8.alv.pub'}

hosts=[t7,t8]

ipstr=os.popen('ip a s ens32|grep global').read()
lastIPNumber=re.findall(r'\w\s(.*)\/',ipstr)[0].split('.')[-1]


for i in hosts:
    if lastIPNumber == i['ip']:
        os.system('hostname %s'%i['hostname'])
        os.system('echo %s > /etc/hostname'%i['hostname'])
        break
    else:
        os.system('hostname %s'%lastIPNumber+'.alv.pub')
        os.system('echo %s > /etc/hostname' %lastIPNumber+'.alv.pub')
#