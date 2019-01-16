class Player:
    '''
    This is a single Player of the game.
    '''

    def __init__(self, name):
        self.name = name
        self.wheatCount = 0
        self.sheepCount = 0
        self.brickCount = 0
        self.oreCount = 0
        self.woodCount = 0
        self.totalResources = 0
        self.devCards = []
        self.settlementList = []
        self.citiesList = []
        self.roadsList = []
        self.activeKnights = 0
        self.largestArmy = False
        self.longestRoad = False
