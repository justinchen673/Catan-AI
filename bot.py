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
'''
    this function finds all the cards that can may possibly be in the deck
    it does this by removing only the cards that you know are not in the deck
    i.e cards that you have or cards that other players have played, this does
    NOT include cards that other players have picked but not played yet
'''
    def findPossibleDevCardsinDeck (self):
        possibleDevCards = ["Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Year of Plenty", "Year of Plenty", "Monopoly", "Monopoly", "Road Building", "Road Building", "Victory Point", "Victory Point", "Victory Point", "Victory Point", "Victory Point"]
        #removes all devcards that have been played
        for key in self.devCardsPlayed:
            for i in range(0, devCardsPlayed[key]):
                possibleDevCards.remove(key)
        #removes all devcards that you have, but not played yet
        for key in self.devCardDict:
            for i in range(0, self.devCardDict[key]):
                possibleDevCards.remove(key)

        return possibleDevCards

'''
    essentially finds the cards that other players have picked up but not played
    yet
'''
    def findNumUnknownDevCards(self, possDevCards):
        numCardsPlayed = 25 -  len(possDevCards)
        return self.numCardsOut - numCardsPlayed

'''
    finds all the possible decks as a whole accounting for cards that have been
    picked up by others but are still unplayed you don't know

    return the permutations AND the combinations since the number of permuations
    is relevant to how often that solution might be occur
'''
    def findCombosofDevCardsUnplayed(self):
        possDevCards = self.findPossibleDevCardsinDeck()
        numUnknownCards = self.findNumUnknownDevCards(possDevCards)

        unknownPerms = permuations(possDevCards, numUnknownCards)
        unknownCombos = combinations(possDevCards, numUnknownCards)

        return unknownPerms, unknownCombos

'''
    finds the number of repeats of that each combination has using the permutations
    and the python set notation which is order independent to find out how often
    a posible deck occurs.
'''
    def findUniqueCombos (self, perms, combos):

        uniqueCombos = list()

        for i in combos:
            counter = 0
            set1 =set(i)
            for j in perms:
                set2 = set(j)
                same = set1 & set2
                if(same == set1 && same == set2):
                    counter += 1
            lst = [i,counter]
            uniqueCombos.append(lst)

        return uniqueCombos
                
'''
    calculates the probability of picking up a certain dev card given a specific
    deck and how often that deck occurs
'''
    def calcProbOfDevCard(self, x):
        possDevCards = self.findPossibleDevCardsinDeck()
        unknownPerms, unknownCombos = self.findCombosofDevCardsUnplayed()
        uniqueCombos = self.findUniqueCombos(unknownPerms, unknownCombos)
        numCombos = len(unknownPerms)
        allProbs = list()

        #finds the number of the particular unknown combo 
        for tup in unknownCombos:
            p = possDevCards
            numOfCombo = uniqueCombos[unknownCombos.index(i)]
            #removes the unknown combo from the deck
            for val in tup:
                p.remove(val)

            #remakes the deck
            smallDeckDict = {"Knight": 0, "Year of Plenty": 0, "Monopoly": 0, "Victory Point": 0, "Road Building": 0} 
            for i in p:
                smallDeckDict[i] += 1

            #calculate the probability of drawing a specific card
            probXP = (smallDeckDict[x]/ len(p)) * (numOfCombo/numCombos)
            allProbs.append(probXP)

        #sums up the probabilities for all the decks 
        totalProb = 0
        for prob in allProbs:
            totalProb += prob

        return totalProb


    def checkDevCardProb(self):
        
        return True

    def devCardSanityCheck(self):
    	cards = self.numCardsOut + self.devCardDeckSize
    	if cards != 25:
    		return False

    	return True