# 这里将一些系统常用的功能写入脚本便于一次性执行。
---

执行方式： </br>
scriptUrl=</br>
wget -q -O - $sciptUrl |bash</br>
以上是wget的执行方式，或者用curl，如下示例： </br>
bash -c "$(curl -fsSL $scriptUrl)"
