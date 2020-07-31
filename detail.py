# -*- coding: utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# 爬取每个英雄队友的英雄和对手的英雄



from lxml import etree
import urllib.request #引入urllib库
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# hero = 'pudge'
# friend_url = 'http://www.dotamax.com/hero/detail/match_up_comb/' + hero + '/?ladder=y&skill=vh'
# ene_url = 'http://www.dotamax.com/hero/detail/match_up_anti/' + hero + '/?ladder=y&skill=vh'



def friend(hero):
    friend_url = 'http://www.dotamax.com/hero/detail/match_up_comb/' + hero + '/?ladder=y&skill=vh'
    req = urllib.request.Request(url = friend_url,headers = headers)  #发出请求并且接收返回文本对象
    res = urllib.request.urlopen(req) #调用read()进行读取
    html = res.read().decode('utf-8')
    data=open("./data1.html",'w+',encoding='utf-8') 
    print(html,file=data)
    data.close()

    html = etree.parse('./data1.html',etree.HTMLParser())
    # html = etree.HTML('./data.html')
    result = html.xpath('//div[2]//div[3]//div[1]//div[2]//table//tbody//tr//td[1]//span/text()')
    name = html.xpath('//html//body//div[2]//div[3]//div[1]//div[2]//table//tbody/tr//td[1]//a/@href')
    win = html.xpath('//html//body//div[2]//div[3]//div[1]//div[2]//table//tbody//tr//td[3]//div[1]/text()')
    rate = html.xpath('//html//body//div[2]//div[3]//div[1]//div[2]//table//tbody//tr//td[4]//div[1]/text()')
    # print(result)
    path = './friend/' + hero + '.txt'
    data=open(path,'w+',encoding='utf-8') 
    for i in range(len(result)):
        # href="/hero/detail/pugna"
        sttr = name[i].replace('/hero/detail/','')
        print(result[i],sttr,win[i],rate[i],file = data)
    data.close()




def ene(hero):
    ene_url = 'http://www.dotamax.com/hero/detail/match_up_anti/' + hero + '/?ladder=y&skill=vh'
    req = urllib.request.Request(url = ene_url,headers = headers)  #发出请求并且接收返回文本对象
    res = urllib.request.urlopen(req) #调用read()进行读取
    html = res.read().decode('utf-8')
    data=open("./data2.html",'w+',encoding='utf-8') 
    print(html,file=data)
    data.close()

    html = etree.parse('./data2.html',etree.HTMLParser())
    # html = etree.HTML('./data.html')
    result = html.xpath('//div[2]//div[3]//div[1]//div[2]//table//tbody//tr//td[1]//span/text()')
    name = html.xpath('//html//body//div[2]//div[3]//div[1]//div[2]//table//tbody/tr//td[1]//a/@href')
    win = html.xpath('//html//body//div[2]//div[3]//div[1]//div[2]//table//tbody//tr//td[3]//div[1]/text()')
    rate = html.xpath('//html//body//div[2]//div[3]//div[1]//div[2]//table//tbody//tr//td[4]//div[1]/text()')
    # print(result)
    path = './ene/' + hero + '.txt'
    data=open(path,'w+',encoding='utf-8') 
    for i in range(len(result)):
        # href="/hero/detail/pugna"
        sttr = name[i].replace('/hero/detail/','')
        print(result[i],sttr,win[i],rate[i],file = data)
    data.close()

if __name__ == '__main__':
    hero = 'nyx_assassin'
    ene(hero)
    friend(hero)