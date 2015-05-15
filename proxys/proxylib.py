#encoding:utf-8
#lhy
#2014.11

import json
import urllib2

import threading

class ProxyLib(threading.Thread):
    def __init__(self,a,b):
        self.good_proxys = []
        self.good_hosts = []
        self.a = a
        self.b = b
        threading.Thread.__init__(self)

    def load_proxys(self):
        return json.load(open(r'proxys.json'))

    def load_hosts(self):
        return json.load(open(r'hosts.json'))

    def test_proxy(self,a,b):
        all_proxys = self.load_proxys()
        #self.good_hosts = self.load_hosts()
        cookies = urllib2.HTTPCookieProcessor()
        for i in range(a,b):
            proxy = r"http://%s:%s" %(all_proxys[i][0],all_proxys[i][1])
            print proxy
            proxyHandler = urllib2.ProxyHandler({"http":r"http://%s:%s" %(all_proxys[i][0].encode("utf-8"),all_proxys[i][1].encode("utf-8"))})
            opener = urllib2.build_opener(cookies,proxyHandler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')]
            urllib2.install_opener(opener)
            #for j in range(len(self.good_hosts)):
            try:
                req = urllib2.urlopen("http://www.rmrb.info/read.php?tid=1368888",timeout = 10)
                html = req.read()
                print html
                if "人民日报" in html:
                    print "Good Proxy"
                    self.good_proxys.append([all_proxys[i],self.good_hosts[j]])
                    break
            except:
                continue
            print i

    def test_hosts(self):
        all_hosts = self.load_hosts()
        for i in range(len(all_hosts)):
            host = "http://" + all_hosts[i]
            try:
                req = urllib2.urlopen(host + "/search?q=neural+network&hl=en-US&gws_rd=ssl",timeout = 10)
                html = req.read()
                if "google" in html:
                    print "Good Host"
                    self.good_hosts.append(host)
            except:
                continue

    def run(self):
        #self.test_hosts()
        #if self.a == 0:
        #    json.dump(self.good_hosts,open("good_hosts.json",'wb'))
        self.test_proxy(self.a,self.b)

    def to_json(self):
        proxys = json.dumps(self.good_proxys)
        self.outHandle.write(proxys)
