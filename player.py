"""
player.py

This file holds the representation of the Player object, which contains
information regarding each player, such as their cards, points, and any titles
they may hold.
"""

class Player:
    '''
    This is a single Player of the game.
    '''

    def __init__(self, name):
        self.name = name
        self.resourceDict = {
            "wheat": 0,
            "sheep": 0,
            "brick": 0,
            "ore": 0,
            "wood": 0
        }
        self.totalResources = 0
        self.devCardDict = {
            "Knight": 0,
            "Year of Plenty": 0,
            "Monopoly": 0,
            "Victory Point": 0,
            "Road Building": 0
        }
        self.points = 0
        self.activeKnights = 0
        self.longestRoadLength = 0
        self.largestArmy = False
        self.longestRoad = False
        self.isBot = False


    def printHand(self):
        '''
        Prints out what the player has in their hand at the moment. This happens
        at the start of each turn.
        '''

        print("Current Hand:")
        print("\tResources:")
        print("\t\tWheat: " + str(self.resourceDict["wheat"]) + "\tSheep: " + str(self.resourceDict["sheep"]) + "\tBrick: " + str(self.resourceDict["brick"]))
        print("\t\tOre: " + str(self.resourceDict["ore"]) + "\t\tWood: " + str(self.resourceDict["wood"]))
        print("\tDevelopment Cards:")
        print("\t\tKnights: " + str(self.devCardDict["Knight"]) + "\tMonopoly: " + str(self.devCardDict["Monopoly"]) + "\tYear of Plenty: " + str(self.devCardDict["Year of Plenty"]))
        print("\t\tVictory Points: " + str(self.devCardDict["Victory Point"]) + "\t\tRoad Building: " + str(self.devCardDict["Road Building"]))
        print("\tStatus:")
        print("\t\tLongest Road: " + str(self.longestRoad) + "\t\tLargest Army: " + str(self.largestArmy))


    def numResources(self):
        '''
        Returns how many resources this player has.
        '''

        num = 0
        for resource in self.resourceDict:
            num += self.resourceDict[resource]

        return num


    def victorious(self):
        '''
        Checks if this player has won the game by summing up all of their
        victory points and checking if it has reached 10. Returns true if they
        have won, false if they haven't.
        '''

        totalPoints = self.points
        if (self.largestArmy):
            totalPoints += 2
        if (self.longestRoad):
            totalPoints += 2
        totalPoints += self.devCardDict["Victory Point"]
        if (totalPoints >= 10):
            return True
        return False
