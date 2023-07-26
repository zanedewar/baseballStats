import tkinter
import pybaseball
import pandas
import rosters
from tkinter import ttk
import statsapi
#import graphics
batterIndex = ["WAR", "AB", "H", "HR", "BA", "R", 
               "RBI", "SB", "OBP", "SLG", "OPS", "OPS+"]

pitcherIndex = ["WAR", "W", "L", "ERA", "G", 
                "GS", "SV", "IP", "SO", "WHIP"]
class GUI:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.ID = GUI.getID(first, last)
        self.fields = {}
        
        print("self.id[0]: %s" % self.ID[0])
        print("Hello4")
        self.statSetting2023 = True
        self.currBatter = True
        self.genStats()
        
        print("Hello5")
        #print(self.df.BA[('Season Totals', 'Last 365 days')])
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
        self.createGraphics()
        
        self.g.mainloop()
        print(self.rosterDF)
        
    def getID(first, last):
        return pybaseball.playerid_lookup(last,first,fuzzy=True).key_bbref
    
    def changeTeam(self, *args):
        self.currTeam = self.teamVar.get()
        self.roster = rosters.getRoster(self)
        
        self.player['values'] = self.getPlayers()
        self.g.update()
        
        print(self.currTeam)

    def initGraphics(self):
        self.teamVar = tkinter.StringVar()
        self.teamVar.set(self.currTeam)
        
        self.team = ttk.Combobox(self.g, textvariable = self.teamVar)
        self.team['state'] = 'readonly'
        self.team['values'] = rosters.baseball
        
        label = ttk.Label(text="Team: ")
        label.pack(fill=tkinter.Y,padx=5,pady=5)
        self.team.pack(fill=tkinter.Y)
        
        self.team.bind('<<ComboboxSelected>>', self.changeTeam)
        self.createPlayers()
        self.player.pack()
        
    

    def updateGraphics(self):
        return
    
    def createPlayers(self):
        self.playerVar = tkinter.StringVar()
        self.player = ttk.Combobox(self.g, textvariable = self.playerVar)
        self.player['state'] = 'readonly'
        
        currPlayers = self.getPlayers()
        print(currPlayers)
        
        self.player['values'] = currPlayers
        self.label = ttk.Label(text="Player: ")
        
        self.label.pack(fill=tkinter.Y, padx=5,pady=5)
        self.player.pack(fill=tkinter.Y)
        self.player.bind('<<ComboboxSelected>>', self.changePlayer)
        self.g.update()
    
    def createGraphics(self):
        self.fields = {}
        currIndex = batterIndex if self.currBatter else pitcherIndex
        for f in currIndex:
            self.fields[f] = tkinter.Text(self.g)
        
        currStats = self.stats2023 if self.statSetting2023 else self.statsCareer
        for i, field in enumerate(self.fields.values()):
            field.pack()
            field.insert(tkinter.END, currStats[i])
            field.config(state=tkinter.DISABLED)
            print(field)
            print(type(field))
        print(len(self.fields.values()))
        self.g.update()
    
    def getPlayers(self):
        currPlayers = []
        if(self.currTeam != ''):
            for p in self.rostDic[self.currTeam.lower()]:
                print("p: %s" % p)
                if type(p) == str:
                    currPlayers.append(p)
        return currPlayers
    
    def changePlayer(self, *args):
        currPlayer = self.playerVar.get().split()
        if(currPlayer != ""):
            self.first = currPlayer[0]
            self.last = currPlayer[1]
        '''print("CurrPlayer: %s" % currPlayer)
        print(self.first, self.last, sep=" ")'''
        self.ID = GUI.getID(self.first, self.last)
        #print(self.ID[0])
        self.genStats()
        '''print(self.stats2023)
        print(self.statsCareer)'''
        currStats = self.stats2023 if self.statSetting2023 else self.statsCareer
        #print("currStats: %s" % currStats)
        for i, field in enumerate(self.fields.values()):
            print(currStats[i])
            field.config(state=tkinter.NORMAL)
            field.delete('1.0', tkinter.END)
            field.insert('1.0', currStats[i])
            field.config(state=tkinter.DISABLED)
        self.g.update()

    
    def genStats(self):
        self.stats = rosters.getData(self)
        print("self.stats: %s" % self.stats)
        self.stats2023 = self.stats[::2]
        self.statsCareer = self.stats[1::2]
        self.df = pybaseball.get_splits(self.ID[0], pitching_splits=not(self.currBatter))

        


print("hello")