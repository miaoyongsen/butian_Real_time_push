# 补天漏洞实时推送
通过微信公众号推送补天漏洞消息

首先在配置方面，一共有5个参数需要白帽子自己填写，都在butian.py中标记出来了。
这里就说一下如何获取这5个参数。

1、Cookie 
  这个就需要登陆补天，登陆后复制cookie。不要删减，就直接复制然后粘贴到 butian.py 的指定位置
  一般来说cookie都是半个月内都不会掉。（最近一次更换还是2个月前）
  
  
接下来的4个参数需要白帽子自己登陆 https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login  

2、self.appid
  这个参数你登陆后就可以看到
3、self.appsecret
  这个参数你登陆后就可以看到
![截屏2021-11-02 下午7 29 38](https://user-images.githubusercontent.com/45072216/139838753-5a80db2c-dd01-413a-a11a-128b1ae377ba.png)

然后往下滑有一个测试号二维码，用接受微信扫描，然后关注公众号。就可以获取第四个参数self.wecharid

![截屏2021-11-02 下午7 34 45](https://user-images.githubusercontent.com/45072216/139839227-23647418-a32a-448e-87ff-9c63c91ae4e9.png)

4、self.mobanid
如下图
第二步的标题随便填写
第三步的内容填写

{{title.DATA}}
{{content.DATA}}

然后我们就可以获取到self.mobanid参数了
![截屏2021-11-02 下午7 41 05](https://user-images.githubusercontent.com/45072216/139839907-e933c125-a0f6-4024-85db-9e754277e7f5.png)


我们将五个参数依次填写到butian.py中的指定位置就可以了。


然后千删除id_lishi.txt



对了，最重要的，就是这个脚本需要配合linux的命令实现每隔一段时间运行一次，具体哪个命令百度吧，，着急下班明天写
