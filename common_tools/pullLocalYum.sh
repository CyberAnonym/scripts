#!/usr/bin/env bash

systemVersion=$(python -c "import os,re;print(re.findall(r'\d',os.popen('cat /etc/redhat-release').read()))[0]")

repoUrl=https://github.com/AlvinWanCN/TechnologyCenter/raw/master/linux/software/centos7.dc.alv.pub.repo

curl -sSL $repoUrl > /etc/yum.repos.d/centos7.dc.alv.pub.repo