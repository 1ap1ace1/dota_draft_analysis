# -*- coding: utf-8 -*-
import sys
import logging
import detail
# reload(sys)
# sys.setdefaultencoding('utf8')

from lxml import etree
import urllib.request #引入urllib库
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

req = urllib.request.Request(url = "http://dotamax.com/hero/rate/?skill=vh&ladder=y",headers = headers)  #发出请求并且接收返回文本对象
res = urllib.request.urlopen(req) #调用read()进行读取
html = res.read().decode('utf-8')
data=open("./data.html",'w+',encoding='utf-8') 
print(html,file=data)
data.close()


html = etree.parse('./data.html',etree.HTMLParser())
# html = etree.HTML('./data.html')
result = html.xpath('//div[2]//div[3]//div[1]//div[2]//table//tbody//tr//td[1]//span/text()')
name = html.xpath('//html//body//div[2]//div[3]//div[1]//div[2]//table//tbody/tr/@onclick')
win = html.xpath('//html//body//div[2]//div[3]//div[1]//div[2]//table//tbody//tr//td[2]//div[1]/text()')
rate = html.xpath('//html//body//div[2]//div[3]//div[1]//div[2]//table//tbody//tr//td[3]//div[1]/text()')
# print(result)
data=open("./hero.txt",'w+',encoding='utf-8') 
summ = 0
for i in range(len(result)):
    sttr = name[i].replace('DoNav(\'/hero/detail/','').replace('\')','')
    num = rate[i].replace(',','')
    try:
        print(result[i],sttr,win[i],num,file = data)
        # detail.ene(sttr)
        # detail.friend(sttr)
        logging.info(sttr+' finished!')
        summ = summ +1
    except:
        logging.error(sttr)
data.close()
logging.info('finished! Done ' + str(summ) + '/' + str(len(result)))
