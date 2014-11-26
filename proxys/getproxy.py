#lhy
#2014.11

import json
import htmlscraper

proxys = []
urlList = ["http://www.proxy360.cn/default.aspx","http://www.proxy360.cn/Region/America","http://www.proxy360.cn/Region/Brazil","http://www.proxy360.cn/Region/Japan","http://www.proxy360.cn/Region/Taiwan"]

for i in range(len(urlList)):
    htmlScraper = htmlscraper.HtmlScraper(urlList[i])
    htmlScraper.scrap()
    proxys.extend(htmlScraper.proxy_scrap())
json.dump(proxys,open("proxys.json",'w'))
