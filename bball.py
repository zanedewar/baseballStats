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
        
        print(self.rosterDF)
        self.rostDic = {'angels': self.rosterDF.angels, 'astros': self.rosterDF.astros,'athletics': self.rosterDF.athletics,'bluejays': self.rosterDF.bluejays,'braves': self.rosterDF.braves,
                        'brewers': self.rosterDF.brewers,'cardinals': self.rosterDF.cardinals,'cubs': self.rosterDF.cubs,'dbacks': self.rosterDF.dbacks,'dodgers': self.rosterDF.dodgers,
                        'giants': self.rosterDF.giants,'guardians': self.rosterDF.guardians,'mariners': self.rosterDF.mariners,'marlins': self.rosterDF.marlins,'mets': self.rosterDF.mets,'nationals': self.roster.nationals,
                        'orioles': self.rosterDF.orioles,'padres': self.rosterDF.padres,'phillies': self.rosterDF.phillies,'pirates': self.rosterDF.pirates,'rangers':self.rosterDF.rangers,
                        'rays': self.rosterDF.rays,'redsox':self.rosterDF.redsox,'reds': self.rosterDF.reds,'rockies': self.rosterDF.rockies,'royals': self.rosterDF.royals,
                        'tigers':self.rosterDF.tigers,'twins':self.rosterDF.twins,'whitesox': self.rosterDF.whitesox,'yankees': self.rosterDF.yankees}
        
        self.initGraphics()
        self.g.mainloop()
        print(self.rosterDF)
        
    def getID(first, last):
        return pybaseball.playerid_lookup(last,first,fuzzy=True).key_bbref
    
    def changeTeam(self, *args):
        self.currTeam = self.teamVar.get()
        self.roster = rosters.getRoster(self)
        
        self.player.destroy()
        self.label.destroy()
        
        self.createPlayers()
        print(self.currTeam)

    def initGraphics(self):
        self.teamVar = tkinter.StringVar()
        self.teamVar.set(self.currTeam)
        
        self.team = ttk.Combobox(self.g, textvariable = self.teamVar)
        self.team['state'] = 'readonly'

        
        self.team['values'] = rosters.baseball
        
        label = ttk.Label(text="Team: ")
        label.pack(fill=tkinter.X,padx=5,pady=5)
        self.team.pack()
        self.team.bind('<<ComboboxSelected>>', self.changeTeam)
        
        self.createPlayers()
        self.player.pack()
        
    

    def updateGraphics(self):
        return
    
    def createPlayers(self):
        self.playerVar = tkinter.StringVar()
        self.player = ttk.Combobox(self.g, textvariable = self.playerVar)
        self.player['state'] = 'readonly'
        
        currPlayers = []
        if(self.currTeam != ''):
            for p in self.rostDic[self.currTeam.lower()]:
                print("p: %s" % p)
                if type(p) == str:
                    currPlayers.append(p)
        print(currPlayers)
        
        self.player['values'] = currPlayers
        self.label = ttk.Label(text="Player: ")
        
        self.label.pack(fill=tkinter.X, padx=5,pady=5)
        self.player.pack()
        self.g.update()


print("hello")