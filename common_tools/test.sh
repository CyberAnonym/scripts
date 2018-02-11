#!/bin/bash

#定义确认命令是否执行成功的消息输出
checkLastCommand(){
if [ $? -eq 0 ];then
    echo $1
    else
    echo $2
fi
}
disableSelinux(){
sed -i 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config
checkLastCommand "selinux configuration file /etc/selinux/config has been configure to disabled"  "failed to change selinux configuration /etc/selinux/config"
setenforce 0
checkLastCommand "selinux linux has been disabled for this time." "failed to disable selinux"
}

disableFirewalld(){
systemctl stop firewalld
checkLastCommand "firewalld has been stoped" "failed to stop firewalld"
systemctl disable firewalld
checkLastCommand "firewald has been disabled" "failed to disable firewalld"
}

main(){
disableSelinux
disableFirewalld
}

main
