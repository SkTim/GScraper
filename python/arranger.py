#lhy
#2015.5

import cPickle
import htmlscraper

class Arranger:
	def __init__(self,thread_num,url,route):
		self.range = [860157,1368888]
		self.thread_num = thread_num
		self.url = url
		self.route = route

	def scrap(self):
		url_num = (self.range[1] - self.range[0] + 1) / self.thread_num
		index_list = []
		begin = self.range[0]
		for i in range(self.thread_num):
			if i != self.thread_num - 1:
				index_list.append([begin,begin + url_num - 1])
				begin += url_num
			else:
				index_list.append([begin,self.range[1]])
		job_list = []
		for i in range(self.thread_num):
			htmlScraper = htmlscraper.HtmlScraper("http://www.rmrb.info/read.php?tid=",index_list[i],self.route)
			job_list.append(htmlScraper)
		for i in range(len(job_list)):
			job_list[i].start()
		for i in range(len(job_list)):
			job_list[i].join()
		date_dict = {}
		for i in range(len(job_list)):
			for (key,value) in job_list[i].index.items():
				date_dict[key] = value
		cPickle.dump(date_dict,open(self.route + "index",'wb'))