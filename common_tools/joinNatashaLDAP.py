#!/usr/bin/python
#conding:utf-8
import os
def op0(content): #op是out put简写定义绿色字体输出success 红色字体是31m.绿色字是32m# 黄色颜色是33m,
    print(content+'\033[032m [success] \033[0m')
def op1(content):
    print(content + '\033[031m [success] \033[0m')
def processCommand(command,successLog,failedLog): #定义确认命令是否执行成功的消息输出的函数
    if command == 0:
        op0(successLog)
    else:
        op1(failedLog)
def installLDAPSoft():
    processCommand(os.system('yum install nss-pam-ldapd setuptool -y'),"nss-pam-ldapd setuptool已安装完成。","nss-pam-ldapd setuptool安装失败")
def joinLDAP():
    processCommand(os.system('authconfig --enableldap  --enableldapauth --ldapserver=ldap://natasha.alv.pub --disableldaptls  --enablemkhomedir --ldapbasedn="dc=alv,dc=pub" --update'),"已成功加入到natasha.alv.pub LDAP系统。","错误，没有成功加入到LDAP")
def installAutofs():
    processCommand(os.system('yum -y install autofs nfs-utils'),"autofs has been installed","Failed install autofs")
def configureAuthfs():
    processCommand(os.system('echo "/sophiroth auto.sophiroth rw,nosuid --timeout=60" >>/etc/auto.master && echo "* dc.alv.pub:/ldapUserData/&" >> /etc/auto.sophiroth'),"Autofs has been configured","Failed configure autofs")

def startAutofs():
    processCommand(os.system('systemctl start autofs'),"Autofs has been started","Failed start autofs")
    processCommand(os.system('systemctl enable autofs'),"Autofs has been enabled","Failed enable autofs")
    os.system('systemctl start autofs')


def main():
    installLDAPSoft()
    joinLDAP()
    installAutofs()
    configureAuthfs()
    startAutofs()
if __name__ == "__main__":
    main()