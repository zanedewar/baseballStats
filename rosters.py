#https://gist.github.com/Jreyno40/947419b81644d4a0fc714866a0e81cde

# Quick Scraper to grab current roster of MLB players by team
# http://m.mlb.com/team_name_here/roster

# This script relies on the specific source code format of lines
# containing player names!

import requests
import pandas as pd

#Team codes

baseball = ['angels','astros','athletics','bluejays','braves','brewers','cardinals','cubs','diamondbacks','dodgers',
            'giants','guardians','mariners','marlins','mets','nationals','orioles','padres','phillies','pirates','rangers',
            'rays','redsox','reds','rockies','royals','tigers','twins','whitesox','yankees']
#baseball = ['angels']

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