#lhy
#2014.10

import re

class TextProcess:
    def __init__(self,text):
        self.text = text

    def clearPoint(self):
        pointList = [',','.',';',':','?','\n']
        for i in range(len(self.text)):
            if self.text[i] in pointList:
                self.editString(' ',i)

    def clearHtml(self):
        string = ""
        iter = re.finditer('''>([^<>]*)<''',self.text)
        for it in iter:
            string += ' ' + it.group(1)
        self.text = string

    def getTitle(self):
        flag = 0
        for i in range(len(self.text)):
            if flag == 0:
                if self.text[i] == '<':
                    if self.text[i + 1] == 'b' and self.text[i + 2] == '>':
                        flag = 1
                    if self.text[i + 1] == '/' and self.text[i + 2] == 'b' and self.text[i + 3] == '>':
                        flag = 1
                    self.editString(' ',i)
            if flag == 1:
                if self.text[i] == '>':
                    flag = 0
                self.editString(' ',i)

    def clearSpace(self):
        l = self.text.split(' ')
        string = ""
        #for i in range(len(l)):
        #    if l[i] == '':
        #        del(l[i])
        for i in range(len(l)):
            string += l[i]
            if l[i] != '':
                string += ' '
        self.text = string
        self.text = string.strip(' ')

    def editString(self,char,index):
        string = ""
        s_list = list(self.text)
        s_list[index] = char
        for i in range(len(s_list)):
            string += s_list[i]
        self.text = string
