#lhy
#2014.10

import json

class StateKeeper:
    def __init__(self):
        self.now_id = ""
        self.urlList = []
        self.grade = []
        self.library = {}
        self.paperStates = []

    def init_stateKeeper(self):
        self.now_id == "1"
        self.urlList = []
        self.grade = [0,0]
        self.library = {}
        self.paperStates = [0] * 2244018
        state = [self.now_id,self.urlList,self.grade,self.library,self.paperSates]
        json.dump(state,open("/home/hongyin/pdf_scraper/statekeeper/state.json",'wb'))

    def set_id(self,now_id):
        self.now_id = now_id
        self.urlList = []

    def set_grade(self,grade):
        self.grade = grade

    def set_library(self,paper_id,key,value):
        self.library[paper_id][key] = value

    def set_state(self,paper_id,state):
        self.paperState[paper_id] = state

    def save_state(self):
        state = [self.now_id,self.urlList,self.grade,self.library,self.paperStates]
        json.dump(state,open("/home/hongyin/pdf_scraper/statekeeper/state.json",'wb'))

    def set_urlList(self,urlList):
        self.urlList = urlList
