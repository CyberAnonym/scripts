#!/usr/bin/python
#coding:utf-8
import socket,os,re
ipaddstr=os.popen('ip a s|grep global').read().split('\n')[:-1]
osInfo=os.popen('cat /etc/redhat-release').read().split('\n')[0]
kernel=os.popen('uname -r').read().split('\n')[0]
cpuLine=os.popen('cat /proc/cpuinfo |grep process|wc -l').read().split('\n')[0]
memTotalstr=os.popen('cat /proc/meminfo |grep -i memtotal').read().split('\n')[0]
memAvailable=os.popen('cat /proc/meminfo |grep -i MemAvailable').read().split('\n')[0]
user=os.popen('whoami').read().split('\n')[0]
homedir=os.popen('echo $HOME').read().split('\n')[0]
#a=socket.get
#print(a)
hostname=socket.gethostname()


def value(content):
#    return ('\033[1;4;031m %s\033[0m'%content)  #\033[代表开始定义字体格式，1代表高亮显示，4代表使用下划线 ，031m代表红色字体，\033[0m代表使用终端设置，即取消颜色设置
    return ('\033[1;031m %s\033[0m'%content)  #\033[代表开始定义字体格式，1代表高亮显示，4代表使用下划线 ，031m代表红色字体，\033[0m代表使用终端设置，即取消颜色设置

def title(content):
    return ('\033[033m %s\033[0m'%content)  #定义黄色字体
def sophiroth_print(t,v):
    print('| '+title(t.ljust(20))+value(v.ljust(50))+'|')
def print_nic():
    for i in ipaddstr:
        ip=re.findall(r'inet\s(\w.*)/',i)[0]
        nicName=str('NIC '+i.split(' ')[-1]+':')
        sophiroth_print(nicName,ip)

def print_osInfo():
    sophiroth_print('OS info:',osInfo)

def print_hostname():
    sophiroth_print('Hostname:',hostname)
def print_LinuxKernel():
    sophiroth_print('LinuxKernel:',kernel)
def print_cpuLIne():
    sophiroth_print('CPU line:',cpuLine)
def print_memState():
    totalMem=str(int(int(re.findall(r'\d.*\d',memTotalstr)[0])/1024))+' MB'
    availableMem=str(int(int(re.findall(r'\d.*\d',memAvailable)[0])/1024))+' MB'
    sophiroth_print("Total Memory:",totalMem)
    sophiroth_print("Availible Memory:",availableMem)
def print_userInfo():
    sophiroth_print('User Name:',user)
    sophiroth_print('Home Directory:',homedir)


print('╭'+'\033[5;1;032mWelcome to Alvin\'s Compute Center\033[0m'.center(87,'-')+'╮')
print_hostname()
print_nic()
print_osInfo()
print_LinuxKernel()
print_cpuLIne()
print_memState()
print_userInfo()
print('╰'+'\033[4;1;035mSophiroth Cluster\033[0m'.center(87,'-')+'╯')
print('ok,test again.')