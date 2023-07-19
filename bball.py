import tkinter
import pybaseball
import pandas
import rosters
from tkinter import ttk
class GUI:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.ID = GUI.getID(first, last)
        print("self.id[0]: %s" % self.ID[0])
        self.df = pybaseball.get_splits(self.ID[0])
        self.rosterDF = rosters.init()
        self.g = tkinter.Tk()
        self.currTeam = 'astros'
        self.roster = rosters.getRoster(self)
        #self.rostDic = {'mariners': self.rosterDF.loc['mariners']}
        #self.rostDic = {'mariners' : self.rosterDF.mariners}
        print(self.rosterDF)
        #print(self.rostDic)
        self.rostDic = {'angels': self.rosterDF.angels, 'astros': self.rosterDF.astros,'athletics': self.rosterDF.athletics,'bluejays': self.rosterDF.bluejays,'braves': self.rosterDF.braves,
                        'brewers': self.rosterDF.brewers,'cardinals': self.rosterDF.cardinals,'cubs': self.rosterDF.cubs,'diamondbacks': self.rosterDF.diamondbacks,'dodgers': self.rosterDF.dodgers,
                        'giants': self.rosterDF.giants,'guardians': self.rosterDF.guardians,'mariners': self.rosterDF.mariners,'marlins': self.rosterDF.marlins,'mets': self.rosterDF.mets,'nationals': self.roster.nationals,
                        'orioles': self.rosterDF.orioles,'padres': self.rosterDF.padres,'phillies': self.rosterDF.phillies,'pirates': self.rosterDF.pirates,'rangers':self.rosterDF.rangers,
                        'rays': self.rosterDF.rays,'redsox':self.rosterDF.redsox,'reds': self.rosterDF.reds,'rockies': self.rosterDF.rockies,'royals': self.rosterDF.royals,
                        'tigers':self.rosterDF.tigers,'twins':self.rosterDF.twins,'whitesox': self.rosterDF.whitesox,'yankees': self.rosterDF.yankees}
        
        self.initGraphics()
        self.currTeam = 'angels'
        self.roster = rosters.getRoster(self)
        print(self.rosterDF)
        
    def getID(first, last):
        return pybaseball.playerid_lookup(last,first,fuzzy=True).key_bbref
    def initGraphics(self):
        teamVar = tkinter.StringVar()
        playerVar = tkinter.StringVar()
        team = ttk.Combobox(self.g, textvariable = teamVar)
        player = ttk.Combobox(self.g, textvariable = playerVar)
        team['values'] = rosters.baseball
        currPlayers = []
        for p in self.rostDic[self.currTeam.lower()]:
            if type(p) == str:
                currPlayers.append(p)
        player['values'] = currPlayers
        team.pack()
        player.pack()
        self.g.mainloop()
        #hello a
    '''def genDic(self):
        dic = { self.currTeam.lower() : self.roster.currTeam.lower()}
        return dic'''
print("hello")