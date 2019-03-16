from player import *
from itertools import combinations

class Bot(Player):

    def __init__(self,name):
        Player.__init__(self,name)

        self.winStrategy = None

        #all dev cards that have been played, including yours
        self.devCardsPlayed = {
            "Knight": 0,
            "Year of Plenty": 0,
            "Monopoly": 0,
            "Victory Point": 0,
            "Road Building": 0
        }

        
    
        self.devCardDeckSize = 25
        #all dev cards that have been bought, including ones that haven't been played yet
        self.numCardsOut = 0



    def removeUsed(self, card):
    	devCards.remove(card)
    	devCardDeckSize -= 1

    def cardPickedUp(self):
        self.numCardsOut += 1

    def findPossibleDevCardsinDeck (self):
        possibleDevCards = ["Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Year of Plenty", "Year of Plenty", "Monopoly", "Monopoly", "Road Building", "Road Building", "Victory Point", "Victory Point", "Victory Point", "Victory Point", "Victory Point"]
        for key in devCardsPlayed:
            for i in range(0, devCardsPlayed[key]):
                possibleDevCards.remove(key)

        for key in devCardDict:
            for i in range(0, devCardDict[key]):
                possibleDevCards.remove(key)

        return possibleDevCards


    def findNumUnknownDevCards(self, possDevCards):
        numCardsPlayed = 25 -  len(possDevCards)
        return numCardsOut - numCardsPlayed


    def findCombosofDevCardsUnplayed(self):
        possDevCards = self.findPossibleDevCardsinDeck()
        numUnknownCards = self.findNumUnknownDevCards(possDevCards)

        unknownCombos = combinations(possDevCards, numUnknownCards)

        return unknownCombos

    def calcProbOfDevCard(self, x):
        possDevCards = self.findPossibleDevCardsinDeck()
        unknownCombos = self.findCombosofDevCardsUnplayed()
        numCombos = len(unknownCombos)
        allProbs = list()

        for tup in unknownCombos:
            p = possDevCards
            for val in tup:
                p.remove(val)

            smallDeckDict = {"Knight": 0, "Year of Plenty": 0, "Monopoly": 0, "Victory Point": 0, "Road Building": 0} 
            for i in p:
                smallDeckDict[i] += 1

            probXP = (smallDeckDict[x]/ len(p)) *(1/numCombos)
            allProbs.append(probXP)

        totalProb = 0
        for prob in allProbs:
            totalProb += prob

        return totalProb


    def checkDevCardProb(self):
         
        return true

    def devCardSanityCheck(self):
    	cards = self.numCardsOut + self.devCardDeckSize
    	if cards != 25:
    		return False

    	return True