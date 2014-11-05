#lhy
#2014.11

import json
import htmlscraper

proxys = []

htmlScraper = htmlscraper.HtmlScraper("http://www.proxy360.cn/default.aspx")
htmlScraper.scrap()
proxys.extend(htmlScraper.proxy_scrap())
json.dump(proxys,open("proxys.json",'w'))
