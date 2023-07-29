#https://gist.github.com/Jreyno40/947419b81644d4a0fc714866a0e81cde

# Quick Scraper to grab current roster of MLB players by team
# http://m.mlb.com/team_name_here/roster

# This script relies on the specific source code format of lines
# containing player names!

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession


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

def getData(self):
    
    url = "https://www.baseball-reference.com/players/%s/%s.shtml" % (self.last.lower()[0], self.ID[0])
    print(url)
    r = requests.get(url)
    
    #Renders w/ JavaScript and then scrapes html to get stats
    sesh = HTMLSession()
    s = sesh.get(url)
    s.html.render()
    
    html = s.content.decode("utf-8")
    soup = bs(html, 'html.parser')
    spans = soup.find_all("p")
    
    nums = []
    for span in spans:
        span = str(span)
        ind = span.find(">")
        end = span[ind:].find("<")
        
        span = span[ind+1:end+ind]
        print("span: %s" % span)
        if(checkNum(span)):
            print("good")
            nums.append(span)
    print(nums)
    sesh.close()
    return nums
    
def checkNum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False