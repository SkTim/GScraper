#lhy
#2014.11

import json
import proxylib

proxy_list = json.load(open(r'proxys.json'))
proxy_length = len(proxy_list)
proxyLibList = []
good_proxys = []

for i in range(20):
    proxyLib = proxylib.ProxyLib(i * int(proxy_length / 20),(i + 1) * int(proxy_length / 20))
    proxyLibList.append(proxyLib)

for i in range(len(proxyLibList)):
    proxyLibList[i].start()

for i in range(len(proxyLibList)):
    proxyLibList[i].join()

for i in range(len(proxyLibList)):
    good_proxys.extend(proxyLibList[i].good_proxys)

json.dump(good_proxys,open("good_proxys.json",'wb'))
