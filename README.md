# LittleLittle

### 列表

- autoemail

### autoemail
实验室的机器总是有可能因为被人拔网线重启或者网络故障什么的导致IP变化，从而影响在上面的VPN服务，此脚本在于让机器自动在IP变化时将新IP发至校内邮箱，这样在宿舍也能知道新的IP了。

使用[Upstart](http://upstart.ubuntu.com/cookbook)进行启动控制，操作如下。

```
$ sudo mv autoemail.conf /etc/init
$ sudo initctl reload-configuration
$ sudo start autoemail
```

关闭的时候使用如下命令。

```
$ stop autoemail
```