#!/usr/bin/python
#coding:utf-8
import subprocess,os

subprocess.call('yum install gcc zlib zlib-devel libffi-devel -y')
os.chdir('/tmp')
subprocess.call('curl -fsSL https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz > python3.6.5.tar.xz')
subprocess.call('tar xf python3.6.5.tar.xz -C /usr/local/src/')
os.chdir('/usr/local/src/Python-3.6.5/')
subprocess.call('./configure --prefix=/usr/local/python3')
subprocess.call('make')
subprocess.call('make install')
subprocess.call('ln -s /usr/local/python3/bin/python3 /usr/bin/')
subprocess.call('python3 --version')