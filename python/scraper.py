#encoding:utf-8

from urllib import urlretrieve
import urllib2
import re
import time
import pickle

outHandle = open("urls",'wb')#写入二进制文件
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
url_list = []
host = "http://finance.sina.com.cn/"
url = host
req = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(req)
the_page = response.read()#抓取网页源代码

iter = re.finditer('''<a.*href="([^<>"']*)".*>([^<>"']*)</a></li>''',the_page)
for it in iter:
    url_list.append([it.group(1),it.group(2)])#数据格式:[url,title]

pickle.dump(url_list,outHandle)#把url_list写入文件
outHandle.close()
