#coding:utf-8
import os,re

systemVersion=re.findall(r'\d',os.popen('cat /etc/redhat-release').read())[0]
repoUrl='https://github.com/AlvinWanCN/TechnologyCenter/raw/master/linux/software/centos%s.dc.alv.pub.repo'%systemVersion
os.system('curl -fsSL %s > /etc/yum.repos.d/centos%s.dc.alv.pub.repo'%(repoUrl,systemVersion))
os.system('yum repolist')