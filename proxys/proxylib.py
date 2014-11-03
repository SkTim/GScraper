#lhy
#2014.11

import json
import urllib2
import threading

class ProxyLib(threading.Thread):
    def __init__(self,a,b):
        self.good_proxys = []
        self.a = a
        self.b = b
        threading.Thread.__init__(self)

    def load_file(self):
        return json.load(open(r'proxys.json'))

    def test_proxy(self,a,b):
        all_proxys = self.load_file()
        cookies = urllib2.HTTPCookieProcessor()
        for i in range(a,b):
            #proxy = r"http://%s:%s" %(all_proxys[i][0],all_proxys[i][1])
            proxy = "http://" + all_proxys[i]
            print proxy
            #proxyHandler = urllib2.ProxyHandler({"http":r"http://%s:%s" %(all_proxys[i][0].encode("utf-8"),all_proxys[i][1].encode("utf-8"))})
            #opener = urllib2.build_opener(cookies,proxyHandler)
            #opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')]
            #urllib2.install_opener(opener)
            try:
                req = urllib2.urlopen(proxy,timeout = 10)
                html = req.read()
                #print html
                if "google" in html:
                    print "Good Proxy"
                    self.good_proxys.append(all_proxys[i])
            except:
                continue
            print i

    def run(self):
        self.test_proxy(self.a,self.b)

    def to_json(self):
        proxys = json.dumps(self.good_proxys)
        self.outHandle.write(proxys)
