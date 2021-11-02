import requests
import json

#此脚本需要修改 5 个参数
#Cookie
#self.appid
#self.appsecret
#self.wecharid
#self.mobanid


#参数如何获取看github   https://github.com/miaoyongsen/butian_Real_time_push


class butian_main:
    def __init__(self):
        self.url = "https://www.butian.net/Home/Message/lists"      #获取所有消息列表的地址
        #请求头，带有cookie
        self.headers = {
            'Host': 'www.butian.net',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryFc6YsPCOcaeohRgd',
            'Referer': 'https://www.butian.net/Message',
            'Cookie': ''
        }
        #提交参数
        self.data = {
            'ajax':1,
            'id':0,
            'status':-1,
            'page':1
        }
        self.appid = ""
        self.appsecret = ""
        self.wecharid = ""  # 微信id
        self.mobanid = ""  # 模版id




    #md5生成，校验
    def md5_new(self,url_text):     #获取源码
        json_txt = json.loads(url_text)["data"]["list"]
        for i in json_txt:          #将响应包转换为列表
            jingjian_xiaoxi = str(i['id']) +i['type']+i['title']       #最新消息
            lishi_xiaoxi = self.read_lishi()                                    #历史消息
            if jingjian_xiaoxi not in lishi_xiaoxi:     #判断是否重复
                self.send_wechat("补天",jingjian_xiaoxi)
                self.write_lishi(jingjian_xiaoxi)       #写入新信息


    #读取历史记录
    def read_lishi(self):
        try:
            with open('id_lishi.txt','r') as f:     #历史消息
                ff = f.read()
            fff = ff.split('\n')
            return fff
        except:
            self.send_wechat("程序异常","读取id_lishi.txt失败")

    #写入历史记录
    def write_lishi(self,word_txt):
        try:
            with open('id_lishi.txt','a') as c:
                c.write(word_txt + '\n')
        except:
            self.send_wechat("程序异常","写入id_lishi.txt失败")

    #获取列表
    def list_seeion(self):
        try:
            #主要请求
            response = requests.post(self.url,headers=self.headers,data=self.data).text
            if 'status' in response and 'success' in response:
                self.md5_new(response)
            elif '请登录' in response and '错误提示' in response:
                self.send_wechat("请重新登录","补天cookie过期或者错误，请填写最新完整的cookie")
                print("error,请重新登录补天cookie过期或者错误，请填写最新完整的cookie")
            else:
                self.send_wechat("程序异常","无法访问补天,有可能服务器ip被ban。具体联系17602600908")
                print("error,程序异常无法访问补天,有可能服务器ip被ban。具体联系17602600908")
        except:
            print("error,发送模块有问题")

    #微信发送模块
    def send_wechat(self,title,content):        #两个参数，标题，内容
        urls = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + self.appid + '&secret=' + self.appsecret
        try:
            response = requests.get(urls).json()["access_token"]  # 获取token
            try:
                url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % response
                datas = {
                    "touser": self.wecharid,
                    "template_id": self.mobanid,
                    'data': {'title':{'value':title},'content':{'value':content}}}
                # 传递参数
                response_two = requests.post(url, headers={"Content-Type": "application/json;charset=utf-8"}, json=datas)
                print("success,成功调用微信发送模块")
            except:
                print("error,微信发送发送模块错误")
        except:
            print("error,微信发送获取token失败")


#butian_main().list_seeion()
butian_main().list_seeion()

