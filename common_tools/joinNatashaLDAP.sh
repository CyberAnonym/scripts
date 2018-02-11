#!/usr/bin/env bash
echo0(){ #定义绿色字体输出success 红色字体是31m.绿色字是32m# 黄色颜色是33m,
echo -e "$1 \033[032m [success] \033[0m"
}
echo1(){ #定义红色字体输出failed
echo -e "$1 \033[031m [Failed] \033[0m"
}
checkLastCommand(){ #定义确认命令是否执行成功的消息输出的函数
if [ $? -eq 0 ];then
    echo0 "$1"
    else
    echo1 "$2"
fi
}


installLDAPSoft(){
yum install nss-pam-ldapd setuptool -y
checkLastCommand "nss-pam-ldapd setuptool已安装完成。" "nss-pam-ldapd setuptool安装失败"
}

joinLDAP(){
authconfig --enableldap  --enableldapauth --ldapserver=ldap://natasha.alv.pub --disableldaptls  --enablemkhomedir --ldapbasedn="dc=alv,dc=pub" --update
checkLastCommand "已成功加入到natasha.alv.pub LDAP系统。" "错误，没有成功加入到LDAP"
}

installAutofs(){
yum -y install autofs
checkLastCommand "autofs has been installed" "Failed install autofs"
}

configureAuthfs(){
echo "/sophiroth auto.sophiroth rw,nosuid --timeout=60" >>/etc/auto.master
echo "* dc.alv.pub:/ldapUserData/&" >> /etc/auto.sophiroth
checkLastCommand "Autofs has been configured" "Failed configure autofs"
}

startAutofs(){

systemctl start autofs
checkLastCommand "Autofs has been started" "Failed start autofs"
systemctl enable autofs
checkLastCommand "Autofs has been enabled" "Failed enable autofs"
}

main(){
installLDAPSoft
joinLDAP
installAutofs
configureAuthfs
startAutofs
}
main