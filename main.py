import bball
import pybaseball
import rosters
def main():
    print("hello1")
    name = getName()
    g = bball.GUI(name[0], name[1])
    print(g.df.BA[('Season Totals', 'Last 365 days')])
    currRoster = g.rostDic['mariners']
    for player in currRoster:
        print(player, end=", ")
    currPlayer = currRoster[0].split()
    g = bball.GUI(currPlayer[0], currPlayer[1])
    print(g.df.BA[('Season Totals', 'Last 365 days')])
    
def getName():
    return input("Type in the player's name: ").split()

if (__name__ == '__main__'):
    main()