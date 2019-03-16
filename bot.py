from player import *

class Bot(Player):

	def __init__(self,name):
		Player.__init__(self, name)

		self.winStrategy = None
        self.devCardsPlayed = {
            "Knight": 0,
            "Year of Plenty": 0,
            "Monopoly": 0,
            "Victory Point": 0,
            "Road Building": 0
        }

        devCards = ["Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Year of Plenty", "Year of Plenty", "Monopoly", "Monopoly", "Road Building", "Road Building", "Victory Point", "Victory Point", "Victory Point", "Victory Point", "Victory Point"]
    
        self.devCardDeckSize = 25
        self.numCardsOut = 0



    def removeUsed(self, card):
    	devCards.remove(card)
    	devCardDeckSize -= 1

    def checkDevCardProb(self):
         


    def devCardSanityCheck(self):
    	cards = self.numCardsOut + self.devCardDeckSize
    	if cards != 25:
    		return False

    	return True