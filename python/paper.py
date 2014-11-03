#lhy
#2014.10

class Paper:
    def __init__(self):
        self.title = ""
        self.authors = []
        self.year = ""
        self.public_location = ""
        self.citation = ""
        self.index = ""
        self.arnetid = ""

    def setInfo(self,title,year,public_location,citation,index,arnetid):
        self.title = title
        self.year = year
        self.public_location = public_location
        self.citation = citation
        self.index = index
        self.arnetid = arnetid

    def setAuthors(self,authors):
        self.authors = authors

