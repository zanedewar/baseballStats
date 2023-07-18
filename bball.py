import tkinter
import pybaseball
import pandas
import rosters
from tkinter import ttk
rostDic = {}
class GUI:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.ID = GUI.getID(first, last)
        self.df = pybaseball.get_splits(self.ID[0])
        self.g = tkinter.Tk()
        self.roster = rosters.getRosters()
        self.rostDic = {'angels': self.roster.angels, 'astros': self.roster.astros,'athletics': self.roster.athletics,'bluejays': self.roster.bluejays,'braves': self.roster.braves,
                        'brewers': self.roster.brewers,'cardinals': self.roster.cardinals,'cubs': self.roster.cubs,'diamondbacks': self.roster.diamondbacks,'dodgers': self.roster.dodgers,
                        'giants': self.roster.giants,'guardians': self.roster.guardians,'mariners': self.roster.mariners,'marlins': self.roster.marlins,'mets': self.roster.mets,'nationals': self.roster.nationals,
                        'orioles': self.roster.orioles,'padres': self.roster.padres,'phillies': self.roster.phillies,'pirates': self.roster.pirates,'rangers':self.roster.rangers,
                        'rays': self.roster.rays,'redsox':self.roster.redsox,'reds': self.roster.reds,'rockies': self.roster.rockies,'royals': self.roster.royals,
                        'tigers':self.roster.tigers,'twins':self.roster.twins,'whitesox': self.roster.whitesox,'yankees': self.roster.yankees}
        self.currTeam = 'Mariners'
        self.initGraphics()
        
    def getID(first, last):
        return pybaseball.playerid_lookup(last,first,fuzzy=True).key_bbref
    def initGraphics(self):
        teamVar = tkinter.StringVar()
        playerVar = tkinter.StringVar()
        team = ttk.Combobox(self.g, textvariable = teamVar)
        player = ttk.Combobox(self.g, textvariable = playerVar)
        team['values'] = rosters.baseball
        player['values'] = self.rostDic[self.currTeam.lower()]
        team.pack()
        player.pack()
        self.g.mainloop()
        #hello a
print("hello")