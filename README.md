# design-pattens-of-python
design-pattens-of-python

### 设计模式
### 


配置openvpn
```
来源：https://forums.centos.org/viewtopic.php?t=62337
You simply create a config for a connection.
Let say you have defined connection "foo", i.e. have config file "/etc/openvpn/foo.conf".
Then you start:
systemctl start  openvpn@foo.service
However, if on GUI, then you can use NetworManager's applet to define a connection and start it too.
That approach does in fact store config for the connection into somewhere else than /etc/openvpn.
1。安装openvpn
sudo apt-get install openvpn
2。将openvpn配置文件chenfu.ovpn 改为 chenfu.conf 放到/etc/openvpn/路径下
3。systemctl start openvpn@chenfu.service 启动 此时ping 下看看
4。systemctl enable openvpn@chenfu.service 开机自启动

```