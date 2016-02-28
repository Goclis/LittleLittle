# LittleLittle

### 列表
- autoemail
- cleanproj
- toggle-hide-files
- notifygrade

### autoemail
实验室的机器总是有可能因为被人拔网线重启或者网络故障什么的导致IP变化，从而影响在上面的VPN服务，此脚本在于让机器自动在IP变化时将新IP发至校内邮箱，这样在宿舍也能知道新的IP了。

__邮箱账号密码__

程序通过读取配置文件来获取用来发送邮件的邮箱账号和密码，使用者自行在程序目录下创建`emailconf.py`文件，内容如下。

```
# -*- coding:utf-8 -*-

username = '你的邮箱账号'
password = '你的邮箱密码'
```

__程序启动控制__

使用[Upstart](http://upstart.ubuntu.com/cookbook)进行启动控制，项目中提供了`autoemail.conf`文件，需要自行配置一下文件中的路径（`/path`）后将其放至upstart的目录下，操作如下。

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

### toggle-hide-files
用于在OS X上控制在Finder中`显示/隐藏`隐藏文件的sh脚本。

使用前需要`chmod +x`并放于PATH下。

### notifygrade
如果信息门户上出了新课程的成绩时，邮件通知一下。

