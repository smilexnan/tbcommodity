import requests
from bs4 import BeautifulSoup
import re
import json
import time
import random
#获取店铺名，返回店铺url
class shop:
    def __init__(self,KEY):
        self.getUrl(KEY)
        self.get_keyurl()
        self.getimpkey()
        self.NUMBER = 1
        self.headers = {
            'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
            'accept - encoding': 'gzip, deflate, br',
            'accept - language': 'zh - CN, zh;q = 0.8',
            'cache - control': 'max - age = 0',
            'cookie': 'hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _uab_collina=150028339963458074968016; pnm_cku822=154UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockp3SnRPdk9wTHRBeiw%3D%7CU2xMHDJ7G2AHYg8hAS8XIw0tA18%2BWDRTLVd5L3k%3D%7CVGhXd1llXWBdY1hhWGdbY1ZuWWRGek9ySHFPdUl9QHtHekN3Q207%7CVWldfS0SMg4xESkJJ0kuVXEOIHYg%7CVmhIGCUFPAc7Gy4aIAA%2FCjMTLxEqETELMAUlGSccJwc9AjdhNw%3D%3D%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D; _umdata=2BA477700510A7DF9C391BFD9347B2077153A04BD87ABA180F1D733833DF630964E69493A354FC92CD43AD3E795C914C50CDEBC1B887336380FC3A04ED8E08F3; uc3=sg2=UoM8e6zkcmk99lbqZFF5iJdKdgmf4DyQYYTQ9B%2F%2FJ4g%3D&nk2=3q4e7T%2FUTM7ntO2H&id2=UUjTTLX%2FCvTmhQ%3D%3D&vt3=F8dBzWOfCgnVVVhQ%2BKE%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; uss=U7T1kHfC8%2FerPl651KiO59a4z9raDOn5iUuhe4w1fZ9JvKkE05anVIU98g%3D%3D; lgc=%5Cu8FDB%5Cu51FB%5Cu7684%5Cu80D6%5Cu561F%5Cu561F; tracknick=%5Cu8FDB%5Cu51FB%5Cu7684%5Cu80D6%5Cu561F%5Cu561F; mt=np=&ci=1_1; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; t=b5415a434bae60e121453909d51d6193; cookie2=3e69d5f7f101ed7d4571bc9dc22fb808; v=0; _tb_token_=654e9018e3ab; _m_h5_tk=9d369436064b16ff7c339d8addd97211_1500955436900; _m_h5_tk_enc=65113a6183a9926646abe77af2731f16; linezing_session=Z2P27g0I9wkT0Bd6CNkleMbi_1500953704823Trrl_11; cna=zd3gEXO0S0cCAbaWoPvB5Npc; isg=At7eZXwFC3_Z01-3v1XnE2RHL3TgN6NysG2UCIhgzSGLq3OF_CuTKTwD1YFc',
            # '_m_h5_tk=ad3abb61c345ca290b0f3cd012f8993c_1500204706449; _m_h5_tk_enc=c7990836ac70c2be5688b6494ab39588; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; v=0; _tb_token_=73e53bc3513e4; uc3=sg2=UoM8e6zkcmk99lbqZFF5iJdKdgmf4DyQYYTQ9B%2F%2FJ4g%3D&nk2=3q4e7T%2FUTM7ntO2H&id2=UUjTTLX%2FCvTmhQ%3D%3D&vt3=F8dBzWOfCgnVVVhQ%2BKE%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; existShop=MTUwMDQzODQzMw%3D%3D; uss=U7T1kHfC8%2FerPl651KiO59a4z9raDOn5iUuhe4w1fZ9JvKkE05anVIU98g%3D%3D; lgc=%5Cu8FDB%5Cu51FB%5Cu7684%5Cu80D6%5Cu561F%5Cu561F; tracknick=%5Cu8FDB%5Cu51FB%5Cu7684%5Cu80D6%5Cu561F%5Cu561F; cookie2=3c20680f06ed18cee187cf3b69e66508; sg=%E5%98%9F00; mt=np=&ci=1_1; cookie1=BxeGkJMW0kGHYe3%2Fuw4H%2BSpyVDPCaX6KSxHhThm0Tqc%3D; unb=2026806210; skt=2e7a0c8d7eeac547; t=b5415a434bae60e121453909d51d6193; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=%5Cu8FDB%5Cu51FB%5Cu7684%5Cu80D6%5Cu561F%5Cu561F; cookie17=UUjTTLX%2FCvTmhQ%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; whl=-1%260%260%261500438442886; cna=zd3gEXO0S0cCAbaWoPvB5Npc; uc1=cookie14=UoTcDzZq6mGO%2FQ%3D%3D&lng=zh_CN&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&existShop=false&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&tag=8&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0; isg=Avn5lN5BhIaYbFgmjFx4UicOCGUTruzTU_TTuRsudSCfohk0Y1b9iGfyUpCv',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }
    def getUrl(self,KEY):
        URL='https://shopsearch.taobao.com/search?app=shopsearch&q={}&imgfile=&commend=all&ssid=s5-e&search_type=shop&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170717&rele_field=wangwang'
        URL=URL.format(KEY)
        r=requests.get(URL,timeout=5)
        r.encoding='utf-8'
        soup=BeautifulSoup(r.text,'html.parser')
        soup=soup.select('script')[5].text
        soup=soup.strip()
        p=re.compile(r'g_page_config.*')
        m=p.match(soup)
        if m:
            m=m.group()
        pa=re.compile(r'{.*')
        ma=pa.findall(m)
        ma=ma[0]
        pb=re.compile(r';')
        mb=pb.sub('',ma)
        data=json.loads(mb)
        shopItem=data['mods']['shoplist']['data']['shopItems']
        self.shopUrl=shopItem[0]['shopUrl']
        return self.shopUrl

    #通过店铺url,获取foo文件需要的url值
    def get_keyurl(self):
        self.goodsurl='https:'+self.shopUrl+'/search.htm?orderType=&viewType=&keyword=&lowPrice=&highPrice='
        return self.goodsurl
    def getimpkey(self):
        r = requests.get(self.goodsurl, timeout=5)
        r.encoding = 'gbk'
        soup = BeautifulSoup(r.text, 'html.parser')
        impkey = soup.select('#J_ShopAsynSearchURL')[0]['value']
        # 用正则处理获取的url
        p = re.compile(r'mid=.*?&')
        self.mid = p.findall(impkey)
        # print(m)
        if self.mid:
            self.mid = self.mid[0]
        else:
            print('m为空')
        p = re.compile(r'wid=.*?&')
        self.wid = p.findall(impkey)
        if self.wid:
            self.wid = self.wid[0]
        else:
            print('n为空')

    def getneed(self, keyword, low, high):

        # proxylist = {
        #     '61.152.81.193:9100',
        #     '119.29.7.113:80',
        #     '139.215.214.61:8080',
        #     '222.249.233.238:9000',
        #     '218.241.234.48:8080',
        # }
        #
        # titlelist=[]
        # urllist=[]
        # shopurl=self.shopUrl
        # wid=self.wid
        # mid=self.mid
        #已经得到最后需要的网页，还需要解析网页，并做出翻页操作
        #翻页，获取下一页url，进行解析（拿到class="pagination"里的<a>标签，用切片取最后一个<a>,对a的class属性进行判断）
        def dealcontent(content):
            p = re.compile(r'//.*?\\')
            m = p.findall(content)
            m = m[0]
            m = 'https:'+m
            m = m.replace('\\', '')
            return m
        def getcontent(soup):
            p = re.compile(r'<dd\sclass=\'\\"detail.*?</dd>')
            m = p.findall(str(soup))
            leng = len(m)
            #print(leng)
            titlelist = []
            urllist = []
            try:
                for number in range(0, leng):
                    if m[number]:
                        # print(m[number])
                        n = m[number]
                        soup2 = BeautifulSoup(n, 'html.parser')
                        title = soup2.select('dd a')[0].text
                        url_ = soup2.select('dd a')[0]['href']
                        url_ = dealcontent(url_)
                        title = title.replace(' ', '')
                        titlelist.append(title)
                        urllist.append(url_)
                        #print(url_)
                        #print(title)
                return titlelist, urllist
            except:
                return False
        #getcontent(soup)#取出第一页需要的内容
        #取出下一页的url，进行判断，如果有'href'属性，则取出href属性值，再执行getcontent函数
        def getnextpageurl(soup):
            p = re.compile(r'<div\sclass=\'\\"pagination.*?</div>')
            m = p.findall(str(soup))
            #print(m)
            try:
                m = m[0]
                sou = BeautifulSoup(m,'html.parser')
                #print(sou)
                sou = sou.select('a')[-1:]
                sou = sou[0]['href']
                #print(sou)
                return True
            except:
                return False
        # def mainfunction(nextpageurl,title,url):
        #     try:
        #         r = requests.get(nextpageurl, timeout=5, headers=headers)
        #         r.encoding = 'gbk'
        #         soup = BeautifulSoup(r.content, 'html.parser')
        #         ontitle,onurl=getcontent(soup)#用两个列表接受一下数据
        #         title.extend(ontitle)
        #         url.extend(onurl)
        #         nextpageurl =getnextpageurl(soup)
        #         if nextpageurl==False:
        #             return title,url
        #         else:
        #             nextpageurl=dealcontent(nextpageurl)
        #             return mainfunction(nextpageurl)
        #     except:
        #         print('获取数据失败')
        def makenewurl(NUMBER):
            url = 'https:' + self.shopUrl + '/i/asynSearch.htm?' + self.mid + self.wid
            url_ = 'path=/search.htm&search=y&orderType=null&viewType=null&keyword=%s&lowPrice=%s&highPrice=%s&pageNo=%d' % (
            keyword, low, high,NUMBER)
            URL = url + url_
            print(URL)
            return URL
        def getsoup(url):
            try:
                #proxies = {'http': proxylist[random.randint(0, 4)]}
                print("开始")
                r = requests.get(url, headers=self.headers)
                print(r)
                #print(r.encoding)
                r.encoding = r.apparent_encoding
                #print(r.encoding)
                soup = BeautifulSoup(r.text, 'html.parser')
                return soup
            except:
                return False


        while True:
            URL = makenewurl(self.NUMBER)
            soup = getsoup(URL)
            if soup!=False:
                print(soup)
                if getcontent(soup)!=False:
                    tit, ur = getcontent(soup)
                    ##改动
                    # titlelist.extend(tit)
                    # urllist.extend(ur)
                    yield tit, ur
                    ##改动
                else:
                    print('解析网页失败')
                    return False
                if getnextpageurl(soup)==True:
                    self.NUMBER += 1
                    print(self.NUMBER)
                    time.sleep(random.uniform(1, 10))
                else:
                    print('已经是最后一页了')
                    return False
            else:
                print('获取数据失败')
                return False


        #得到的结果是列表形式，一个urllist，一个titlelist
        #导出时，使用这两个列表的值

#处理输入keyword的url编码
def deal_keyword(key):
    from urllib import parse
    q = key
    p = parse.quote(q, encoding='gbk')
    return p

# KEY = '比安奇小黄人'
# a = shop(KEY)
# key = ''
# key = deal_keyword(key)
# low = ''
# high = ''
# list = a.getneed(key, low, high)
#
# print(next(list))
# print('######################################################################################')
# print(next(list))
# while True:
#     try:
#         tit = next(list)
#         print(tit[0], tit[1])
#     except:
#         break


