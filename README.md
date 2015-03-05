# LittleLittle

### 列表

- autoemail
- cleanproj

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

### cleanproj
没法走网络，每次换地方开发的时候只能把整个VS解决方案拷贝走，但是由于包含了一大堆的Debug及Release文件，使得文件夹变大拷贝起来比较慢，而VS的清除解决方案扫的又不够干净，就写个脚本，放在解决方案的根目录即可。

没弄命令行参数，硬编码清除`Debug`、`Release`、`ipch`也就够了。