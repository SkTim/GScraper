#lhy
#2014.11

import json
import htmlscraper

proxys = []

htmlScraper = htmlscraper.HtmlScraper("http://www.360kb.com/kb/2_122.html")
htmlScraper.scrap()
proxys.extend(htmlScraper.host_scrap())
json.dump(proxys,open("hosts.json",'w'))
