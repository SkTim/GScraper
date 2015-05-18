#encoding:utf-8
#lhy
#2014.10

import urllib2
import re
import textprocess
import os
import threading

class HtmlScraper(threading.Thread):
    def __init__(self,url,_range,route):
        self.url = url
        self.the_page = ""
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent':self.user_agent}
        self.res_html = ""
        self.search_item = []
        self.index = {}
        self.range = _range
        self.route = route
        threading.Thread.__init__(self)

    def run(self):
        self.scrap()

    def scrap(self):
        for i in range(self.range[0],self.range[1] + 1):
            req = urllib2.Request(self.url + str(i),headers = self.headers)
            response = urllib2.urlopen(req)
            self.the_page = response.read()
            outHandle = open(self.route + str(i),'w')
            outHandle.write(self.news_scrap(self.the_page))
            date = self.date_scrap(self.the_page)
            self.index[i] = date

    def date_scrap(self,web_page):
        date = ""
        iter = re.finditer('''<title>[|*?]|([^-|\s]*?) - 人民日报1946-2003 </title>''',web_page.decode("gbk").encode("utf8"))
        for it in iter:
            date = it.group(1)
        return date

    def news_scrap(self,web_page):
        news = ""
        iter = re.finditer('''<div class="tpc_content" id="read_tpc">([^|]*?)</div>''',web_page.decode("gbk").encode("utf8"))
        for it in iter:
            news = it.group(1)
        #print news
        return news

    def google_scrap(self):
        #iter = re.finditer('''<!--sMSL-->([\s\S]*)<!--sMSR-->''',self.the_page)
        #for it in iter:
        #    self.res_html = it.group(1)
        iter = re.finditer('''<p>([\s\S]*?)</p>''',self.the_page)
        for it in iter:
            self.search_item.append(it.group(1))
        for i in range(len(self.search_item)):
            href = ""
            title = ""
            iter = re.finditer('''<a.href="/url\?q=[^"]*">([\s\S]*?)</a>[\s\S]*?<a.href="/search\?q=related:([^"]*)&amp;hl=">''',self.search_item[i])
            #iter = re.finditer('''<a.href="[^"]*">([^"]*)</a>[\s\S]*?<a.href="/search?q=related:([^"]*)&amp;hl=">''',self.search_item[i])
            for it in iter:
                href = it.group(2)
                if href == '':
                    break
                title = it.group(1)
                textProcess = textprocess.TextProcess(title)
                textProcess.getTitle()
                textProcess.clearPoint()
                textProcess.clearSpace()
                self.html_titles[href] = textProcess.text
            if href == '':
                continue
            textProcess = textprocess.TextProcess(self.search_item[i])
            textProcess.clearHtml()
            textProcess.clearPoint()
            textProcess.clearSpace()
            text = textProcess.text
            self.res_items[href] = [self.html_titles[href],text]
        print self.html_titles

    def pdf_scrap(self,arnetid,global_id):
        urlretrieve(self.url,"/home/hongyin/pdf_scraper/library/" + str(global_id) +".pdf")

    def get_website(self):
        first_url = []
        flag = 0
        iter = re.finditer('''href="([^"]*)"[^<>]*>([^<>]*)<''',self.the_page)
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
        textProcess = textprocess.TextProcess(self.the_page)
        textProcess.clearHtml()
        textProcess.clearPoint()
        textProcess.clearSpace()
        self.res_html = textProcess.text
        if flag == 0:
            self.res_items["state"] = 0
            self.res_items["url"] = textProcess.text
        if flag == 1:
            self.res_items["state"] = 1
            self.res_items["url"] = [first_url,self.res_html]
