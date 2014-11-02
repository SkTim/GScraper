#lhy
#2014.11

import json
import urllib2

class ProxyLib:
    def __init__(self):
        self.good_proxys = []

    def load_file(self):
        return json.load(open(r'proxys.json'))

    def test_proxy(self):
        all_proxys = self.load_file()
        cookies = urllib2.HTTPCookieProcessor()
        for i in range(len(all_proxys)):
            proxy = r"http://%s:%s" %(all_proxys[i][0],all_proxys[i][1])
            print proxy
            proxyHandler = urllib2.ProxyHandler({"http":r"http://%s:%s" %(all_proxys[i][0].encode("utf-8"),all_proxys[i][1].encode("utf-8"))})
            opener = urllib2.build_opener(cookies,proxyHandler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')]
            urllib2.install_opener(opener)
            try:
                req = urllib2.urlopen("http://www.tmd123.com",timeout = 10)
                #req = urllib.urlopen("http://www.tmd123.com",proxies = {"http":proxy})
                html = req.read()
                if "youtube" in html:
                    self.good_proxys.append(all_proxys[i])
            except:
                continue
            print i

    def to_json(self):
        proxys = json.dumps(self.good_proxys)
        self.outHandle.write(proxys)
