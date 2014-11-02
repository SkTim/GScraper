#lhy
#2014.10

import time
import httplib
import fileprocess
import htmlscraper
import paper
import statekeeper
import textprocess
import resultcaculator
import features

import json
import collections

class Search:
    def __init__(self):
        self.now_paper = {}
        self.fileProcess = fileprocess.FileProcess()
        self.stateKeeper = statekeeper.StateKeeper()
        #self.resultCaculator = resultcaculator.ResultCaculator()
        self.paperFeatures = features.Features()
        self.global_id = 0
        self.pdfList = {"pdfList":{},"search":{},"urls":{},"result":{}}

    def init_library(self):
        self.fileProcess.load_file()
        self.paperFeatures.init_featureItems()
        self.paperFeatures.load_file()

    def load_library(self):
        self.paperFeature.load_file()

    def set_state(self):
        self.stateKeeper = statekeeper.StateKeeper()
        self.pdfList["urls"] = {}
        self.pdfList["result"] = {"accurancy":0.0,"recall":0.0}

    def search_paper(self):
        url = "http://search.tmd123.com/search?q="
        l = list(self.now_paper["title"])
        for i in range(len(l)):
            if l[i] == ' ':
                l[i] = '%20'
            url += l[i]
        searchList = [url + "&gws_rd=ssl",url + "&gws_rd=ssl&start=10"]
        for i in range(len(searchList)):
            htmlScraper = htmlscraper.HtmlScraper(searchList[i])
            htmlScraper.scrap()
            htmlScraper.google_scrap()
            for (key,value) in htmlScraper.res_items.items():
                print "key = " + key
                if key in self.pdfList["urls"] or "wikipedia" in key:
                    continue
                if "pdf" in key or ".ps" in key or ("researchgate" in key and "links" in key):
                    pdfScraper = htmlscraper.HtmlScraper(key)
                    try:
                        pdfScraper.pdf_scrap(self.now_paper["arnetid"],self.global_id)
                    except:
                        print "Can't download pdf arnetid: " + str(self.now_paper["arnetid"]) + " href = " + key
                        continue
                    pdf_feature = self.paperFeatures.make_feature({"title":value[0],"text":value[1]})
                    self.pdfList["pdfList"][self.global_id] = [self.global_id,self.now_paper["arnetid"],value[0],pdf_feature]
                    if self.now_paper["title"] == value[0]:
                        self.pdfList["search"][self.now_paper["arnetid"]] = self.global_id
                        self.pdfList["result"]["accurancy"] += 1
                    self.pdfList["urls"][key] = 1
                    self.pdfList["result"]["recall"] += 1
                    json.dump(self.pdfList["pdfList"][self.global_id],open("/home/hongyin/pdf_scraper/library/" + str(self.global_id) + ".json",'wb'))
                    print self.global_id
                    self.global_id += 1
                else:
                    webScraper = htmlscraper.HtmlScraper(key)
                    webScraper.scrap()
                    webScraper.get_website()
                    if webScraper.res_items["state"] == 1:
                        pdfScraper = textprocess.TextProcess(webScraper.res_items["url"][0][0])
                        try:
                            pdfScraper.pdf_scrap(self.now_paper["arnetid"],self.global_id)
                        except:
                            print "Can't download pdf arnetid: " + str(self.now_paper["arnetid"]) + " href = " + key
                            continue
                        pdf_feature = self.paperFeatures.make_feature({"title":key,"text":webScraper.res_items["url"][1]})
                        self.pdfList["pdfList"][self.global_id] = [self.global_id,self.now_paper["arnetid"],value[0],pdf_feature]
                        if self.now_paper["title"] == value[0]:
                            self.pdfList["search"][self.now_paper["arnetid"]] = self.global_id
                            self.pdfList["result"]["accurancy"] += 1
                        self.pdfList["urls"][key] = 1
                        self.pdfList["result"]["recall"] += 1
                        json.dump(self.pdfList["pdfList"][self.global_id],open("/home/hongyin/pdf_scraper/library/" + str(self.global_id) + ".json",'wb'))
                        print self.global_id
                        self.global_id += 1

    def start_search(self):
        for i in range(len(self.fileProcess.res_list)):
            #try:
            self.now_paper = self.fileProcess.res_list[i]
            self.search_paper()
            #except:
            #    json.dump(self.pdfList,open("/home/hongyin/pdf_scraper/statekeeper/pdflist.json",'wb'))
