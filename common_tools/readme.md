<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan'></a></p>

## 这里将一些系统常用的功能写入脚本便于一次性执行。
---

执行方式： </br>
```
scriptUrl=
wget -q -O - $scriptUrl |bash</br>
```
以上是wget的执行方式，或者用curl，如下示例： </br>
```
bash -c "$(curl -fsSL $scriptUrl)"
```



#### 1 解决ssh缓慢问题
---
```bash
bash -c "$(curl -fsSL https://github.com/AlvinWanCN/scripts/raw/master/common_tools/sshslowly.sh)"
```

---
#### 2 关闭firewalld和selinux
---
```bash
bash -c "$(curl -fsSL https://github.com/AlvinWanCN/scripts/raw/master/common_tools/disableSeAndFir.sh)"
```
