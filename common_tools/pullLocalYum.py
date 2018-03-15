#coding:utf-8
import os,re,shutil

def backupOriginRepo():
    originDIR='/etc/yum.repos.d/'
    backDIR='/etc/yum.repos.d/backup'
    if os.path.exists(backDIR):
        pass
    else:
        os.mkdir(backDIR)
    files=os.listdir('/etc/yum.repos.d')
    for file in files:
        if re.findall(r'^Cent',file):
            shutil.move(os.path.join(originDIR,file),os.path.join(backDIR,file))
def getRepo():
    systemVersion=re.findall(r'\d',os.popen('cat /etc/redhat-release').read())[0]
    repoUrl='https://github.com/AlvinWanCN/TechnologyCenter/raw/master/linux/software/yum.repos.d/centos%s.dc.alv.pub.repo'%systemVersion
    os.system('curl -fsSL %s > /etc/yum.repos.d/centos%s.dc.alv.pub.repo'%(repoUrl,systemVersion))
    os.system('yum repolist')
def main():
    backupOriginRepo()
    getRepo()
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Detected error.")
        print(e)
