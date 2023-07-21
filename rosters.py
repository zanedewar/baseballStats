#https://gist.github.com/Jreyno40/947419b81644d4a0fc714866a0e81cde

# Quick Scraper to grab current roster of MLB players by team
# http://m.mlb.com/team_name_here/roster

# This script relies on the specific source code format of lines
# containing player names!

import requests
import pandas as pd

#Team codes

baseball = ['angels','astros','athletics','bluejays','braves','brewers','cardinals','cubs','dbacks','dodgers',
            'giants','guardians','mariners','marlins','mets','nationals','orioles','padres','phillies','pirates','rangers',
            'rays','redsox','reds','rockies','royals','tigers','twins','whitesox','yankees']

def getRosters():
    pages = []
    players = []

    for team in baseball:
        r = requests.get("http://mlb.com/" + team + "/roster")
        pages.append(r.text)

    for roster in pages:
        rost = []
        for line in roster.split("\n"):
            if "/player/" in line:
                ind = line.find('>')
                ind2 = line[ind:].find('<')
                rost.append(line[ind+1:(ind+ind2)])
        players.append(rost)
    df = pd.DataFrame(data = players)
    df = df.T
    df.columns = baseball
    return df
def getRoster(graphics):
    pages = []
    players = []

    
    r = requests.get("http://mlb.com/" + graphics.currTeam.lower() + "/roster")
    pages.append(r.text)

    for roster in pages:
        rost = []
        for line in roster.split("\n"):
            if "/player/" in line:
                ind = line.find('>')
                ind2 = line[ind:].find('<')
                rost.append(line[ind+1:(ind+ind2)])
        players.append(rost)

    print(players)

    for player1 in players:
        for i, p in enumerate(player1):
            graphics.rosterDF.loc[i, graphics.currTeam.lower()] = p
    
    return graphics.rosterDF
def init():
    empty = []
    
    for i in range(26):
        empty1 = []
        for j in range(30):
            empty1.append("")
        empty.append(empty1)
        df = pd.DataFrame(empty)
    df.columns = baseball
    print(df)
    return df