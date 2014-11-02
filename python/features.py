#lhy
#2014.10

import pickle
import paper
import fileprocess
import textprocess
import collections

class Features:
    def __init__(self):
        self.featureItems = {}

    def init_featureItems(self):
        fileProcess = fileprocess.FileProcess()
        fileProcess.load_file()
        titleWords = {}
        authors = {}
        years = {}
        public_locations = {}
        for i in range(len(fileProcess.res_list)):
            textProcess = textprocess.TextProcess(fileProcess.res_list[i]["title"])
            textProcess.clearPoint()
            textProcess.clearSpace()
            title = textProcess.text
            words_list = title.split(' ')
            for j in range(len(words_list)):
                if words_list[j] in titleWords:
                    titleWords[words_list[j]] += 1
                else:
                    titleWords[words_list[j]] = 1
            paper_authors = fileProcess.res_list[i]["authors"].split(',')
            for j in range(len(paper_authors)):
                names = paper_authors[j].split(' ')
                for k in range(len(names)):
                    if names[k] != '' and names[k] != ' ':
                        if paper_authors[j] in authors:
                            authors[paper_authors[j]] += 1
                        else:
                            authors[paper_authors[j]] = 1
            year = fileProcess.res_list[i]["year"]
            if year in years:
                years[year] += 1
            else:
                years[year] = 1
            public_location = fileProcess.res_list[i]["public_location"]
            if public_location in public_locations:
                public_locations[public_location] += 1
            else:
                public_locations[public_location] = 1
        titleWords["vector"] = titleWords.keys()
        authors["vector"] = authors.keys()
        public_locations["vector"] = public_locations.keys()
        years["vector"] = years.keys()
        outHandle1 = open("/home/hongyin/pdf_scraper/features/" + "titles",'wb')
        outHandle2 = open("/home/hongyin/pdf_scraper/features/" + "authors",'wb')
        outHandle3 = open("/home/hongyin/pdf_scraper/features/" + "public_locations",'wb')
        outHandle4 = open("/home/hongyin/pdf_scraper/features/" + "years",'wb')
        pickle.dump(titleWords,outHandle1)
        pickle.dump(authors,outHandle2)
        pickle.dump(public_locations,outHandle3)
        pickle.dump(years,outHandle4)

    def load_file(self):
        inHandle1 = open("/home/hongyin/pdf_scraper/features/" + "titles",'rb')
        inHandle2 = open("/home/hongyin/pdf_scraper/features/" + "authors",'rb')
        inHandle3 = open("/home/hongyin/pdf_scraper/features/" + "public_locations",'rb')
        inHandle4 = open("/home/hongyin/pdf_scraper/features/" + "years",'rb')
        titleWords = pickle.load(inHandle1)
        authors = pickle.load(inHandle2)
        public_location = pickle.load(inHandle3)
        years = pickle.load(inHandle4)
        self.featureItems = {"titles":titleWords,"authors":authors,"location":public_location,"years":years}
        print "Features Library Already Built"

    def make_vector(self,d,l):
        vector = []
        for i in range(len(l)):
            if l[i] in d:
                vector.append(d[l[i]])
            else:
                vector.append(0)
        return vector

    def make_feature(self,featureDict):
        title = featureDict["title"]
        text = featureDict["text"]
        titleWords = title.split(' ')
        textWords = text.split(' ')
        featureList = titleWords + textWords
        wordDict = collections.Counter(featureList)
        titleVector = self.make_vector(wordDict,self.featureItems["titles"]["vector"])
        authorVector = self.make_vector(wordDict,self.featureItems["authors"]["vector"])
        featureVector = titleVector + authorVector
        return featureVector
