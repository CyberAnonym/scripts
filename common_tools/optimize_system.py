#coding:utf-8
import subprocess
subprocess.call('echo "set ts=4" >> /etc/vimrc',shell=True)
subprocess.call('echo "set expandtab" >> /etc/vimrc',shell=True)
subprocess.call('ecgi "export HISTTIMEFORMAT=\"%F %T  \"" >> /etc/profile',shell=True)