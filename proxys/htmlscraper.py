#lhy
#2014.10

from urllib import urlretrieve
import urllib2
import re
import textprocess
import os

class HtmlScraper:
    def __init__(self,url):
        self.url = url
        self.the_page = ""
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent':self.user_agent}
        self.res_html = ""
        self.search_item = []
        self.html_titles = {}
        self.res_items = {}

    def scrap(self):
        req = urllib2.Request(self.url,headers = self.headers)
        response = urllib2.urlopen(req)
        self.the_page = response.read()
        print self.url

    def google_scrap(self):
        #iter = re.finditer('''<!--sMSL-->([\s\S]*)<!--sMSR-->''',self.the_page)
        #for it in iter:
        #    self.res_html = it.group(1)
        iter = re.finditer('''<p>([\s\S]*?)</p>''',self.the_page)
        for it in iter:
            self.search_item.append(it.group(1))
        for i in range(len(self.search_item)):
            herf = ""
            title = ""
            iter = re.finditer('''<a href="[^"]*">([^"]*)</a>[\s\S]*?<a href="/search?q=related:([^"]*)&amp;hl=">''',self.search_item[i])
            for it in iter:
                herf = it.group(2)
                title = it.group(1)
                textProcess = textprocess.TextProcess(title)
                textProcess.getTitle()
                textProcess.clearPoint()
                textProcess.clearSpace()
                self.html_titles[herf] = textProcess.text
            textProcess = textprocess.TextProcess(self.search_item[i])
            textProcess.clearHtml()
            textProcess.clearPoint()
            textProcess.clearSpace()
            text = textProcess.text
            self.res_items[herf] = [self.html_titles[herf],text]

    def pdf_scrap(self,arnetid,global_id):
        urlretrieve(self.url,"/home/hongyin/pdf_scraper/library/" + str(global_id) +".pdf")
    
    def proxy_scrap(self):
        proxy = {}
        iter = re.finditer('''([^<>\n#]*)&nbsp;&nbsp;''',self.the_page)
        for it in iter:
            if it.group(1) not in proxy:
                proxy[it.group(1)] = 1
        return proxy

    def get_website(self):
        first_url = []
        flag = 0
        iter = re.finditer('''herf="([^"]*)"[^<>]*>([^<>]*)<''',self.the_page)
        for it in iter:
            herf = it.group(1)
            textProcess = textprocess.TextProcess(it.group(2))
            textProcess.clearHtml()
            textProcess.clearPoint()
            textProcess.clearSpace()
            self.html_titles[herf] = textProcess.text
            if flag == 0 and "pdf" in herf:
                flag = 1
                first_url = [herf,textProcess.text]
        textProcess = textProcess.TextProcess(self.the_page)
        textProcess.clearHtml()
        textProcess.clearPoint()
        textProcess.clearSpace()
        self.res_html = textProcess.text
        if flag == 0:
            self.res_items["state"] = 0
            self.res_items["url"] = self.textProcess.text
        if flag == 1:
            self.res_items["state"] = 1
            self.res_items["url"] = [first_url,self.res_html]
