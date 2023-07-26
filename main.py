import bball
import pybaseball
import rosters
def main():
    print("hello1")
    
    name = getName()
    print("Hello2")
    g = bball.GUI(name[0], name[1])
    print("Hello3")
    
    currRoster = g.rostDic['astros']
    
    
    
def getName():
    #return ("spencer strider").split()
    return ("ty france").split()
    return input("Type in the player's name: ").split()

if (__name__ == '__main__'):
    main()