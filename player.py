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
        self.devCards = []
        self.settlementList = []
        self.citiesList = []
        self.roadsList = []
        self.activeKnights = 0
        self.largestArmy = False
        self.longestRoad = False

    def victorious(self):
        '''
        Checks if this player has won the game by summing up all of their
        victory points and checking if it has reached 10. Returns true if they
        have won, false if they haven't.
        '''

        totalPoints = 0
        totalPoints += len(self.settlementList)
        totalPoints += (len(self.citiesList) * 2)
        if (self.largestArmy):
            totalPoints += 2
        if (self.longestRoad):
            totalPoints += 2
        for i in self.devCards:
            if i == "Victory Point":
                totalPoints += 1
        if (totalPoints >= 10):
            return True
        return False
