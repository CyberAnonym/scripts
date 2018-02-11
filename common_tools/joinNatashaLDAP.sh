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


installSoft(){
yum install nss-pam-ldapd setuptool -y
checkLastCommand "相关软件已安装完成。" "相关软件安装失败"
}

joinLDAP(){
authconfig --enableldap  --enableldapauth --ldapserver=ldap://natasha.alv.pub --disableldaptls  --enablemkhomedir --ldapbasedn="dc=alv,dc=pub" --update
checkLastCommand "已成功加入到natasha.alv.pub LDAP系统。" "错误，没有成功加入到LDAP"
}

main(){
installSoft
joinLDAP
}
main