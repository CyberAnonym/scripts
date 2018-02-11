<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan'></a></p>
<p align=center><b>Common Tools</b></p>

## 这里将一些系统常用的功能写入脚本便于一次性执行。

1,[解决ssh缓慢问题](#解决ssh缓慢问题) </br>
2,[关闭firewalld和selinux](#关闭firewalld和selinux) </br>
3,[加入natasha的LDAP系统](#加入natasha的LDAP系统) </br>
4,[添加dc.alv.pub 的yum仓库](#添加dc.alv.pub的yum仓库) </br>
2,[添加dc.alv.pub 的yum仓库](#加入natasha的LDAP系统) </br>
2,[添加本地仓库](#添加dc alv pub本地仓库) </br>


---

执行方式： </br>
```
scriptUrl=
wget -q -O - $scriptUrl |bash
```
以上是wget的执行方式，或者用curl，如下示例： </br>
```
bash -c "$(curl -fsSL $scriptUrl)"
```



#### 解决ssh缓慢问题
---
```bash
bash -c "$(curl -fsSL https://github.com/AlvinWanCN/scripts/raw/master/common_tools/sshslowly.sh)"
```

---
#### 关闭firewalld和selinux
---
```bash
bash -c "$(curl -fsSL https://github.com/AlvinWanCN/scripts/raw/master/common_tools/disableSeAndFir.sh)"
```

---
#### 加入natasha的LDAP系统
---
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/scripts/master/common_tools/joinNatashaLDAP.sh)"
```

---
#### 添加dc alv pub本地仓库
---

```bash
python -c "$(curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/scripts/master/common_tools/pullLocalYum.py)"
```
