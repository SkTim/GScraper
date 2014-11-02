#lhy
#2014.10

import json
import re

class FileProcess:
    def __init__(self):
        self.inHandle = open(r'/home/hongyin/pdf_scraper/acm_output.txt')
        self.in_list = []
        self.paper = {}
        self.res_list = []

    def load_file(self):
        self.in_list = self.inHandle.readlines()
        paper_string = ""
        for i in range(len(self.in_list)):
            if self.in_list[i] == '\n':
                iter = re.finditer('''#\*([^\n]*).\n''',paper_string)
                for it in iter:
                    self.paper["title"] = it.group(1)
                iter = re.finditer('''#@([^\n]*)\n''',paper_string)
                for it in iter:
                    self.paper["authors"] = it.group(1)
                iter = re.finditer('''#year([^\n]*)\n''',paper_string)
                for it in iter:
                    self.paper["year"] = it.group(1)
                iter = re.finditer('''#conf([^\n]*)\n''',paper_string)
                for it in iter:
                    self.paper["public_location"] = it.group(1)
                iter = re.finditer('''#citation([^\n]*)\n''',paper_string)
                for it in iter:
                    self.paper["citation"] = it.group(1)
                iter = re.finditer('''#index([^\n]*)\n''',paper_string)
                for it in iter:
                    self.paper["index"] = it.group(1)
                iter = re.finditer('''#arnetid([^\n]*)\n''',paper_string)
                for it in iter:
                    self.paper["arnetid"] = it.group(1)
                self.res_list.append(self.paper)
                self.paper = {}
                paper_string = ""
                continue
            paper_string += self.in_list[i]
