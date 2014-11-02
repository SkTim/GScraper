#lhy
#2014.11

import json
import htmlscraper

htmlScraper = htmlscraper.HtmlScraper("http://www.proxy360.cn/default.aspx")
htmlScraper.scrap()
proxys = htmlScraper.proxy_scrap()
json.dump(proxys,open("proxys.json",'w'))
