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
