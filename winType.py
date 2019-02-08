class Win:

	'''
	This class defines a type of win the game. This is the list of be parsed when running
	the AI in order to find the win that is most probable for the player. The 
	characteristics of the class are similar to that of the  player class
	'''

	def __init__(self):

		self.devCardDict = {
			"knight": 0,
            "victoryPoint": 0,
            "roadBuilding": 0
		}

		self.numSettlements = 0
		self.numCities = 0
		self.largestArmy = False

		self.longestRoad = False
		self.minRoadsNeeded = 0

		self.totalVicPts = 0

		self.resourceDict = {
			"wheat": 0,
            "sheep": 0,
            "brick": 0,
            "ore": 0,
            "wood": 0
		}
		self.totalCost = 0

		self.number = 0

	'''
	'''
	def __str__(self):
		return  str(self.number)

	'''
	defines the type of win/ what the player uses to win the game. 
	uses an input of similar dummy dictionaries and bools from the main AI function
	'''
	def setWinType(self, vicPts, army , road ,setts, cits):
		if army == 2:
			self.devCardDict["knight"] = 3
			self.largestArmy = True

		if road == 2:
			self.longestRoad = True

		self.devCardDict["victoryPoint"] = vicPts

		self.numSettlements = setts
		self.numCities = int(cits/2)

		self.totalVicPts = vicPts + army + road +setts + cits

	'''
	
	'''
	def setRoads(self, minR, rBuilding):
		self.minRoadsNeeded = minR
		self.devCardDict["roadBuilding"] = rBuilding

	'''

	'''

	def setNumber(self, counter):
		self.number = counter

	'''
	calculate the total resouces requied to accomplish that particular winning strategy
	returns the dictionary of the resources
	'''	
	def calcResourceCost(self):
		devSum = self.devCardDict["knight"] + self.devCardDict["victoryPoint"] + self.devCardDict["roadBuilding"]

		for i in range(0, devSum):
			self.resourceDict["sheep"] = self.resourceDict["sheep"] + 1
			self.resourceDict["ore"] = self.resourceDict["ore"] + 1
			self.resourceDict["wheat"] = self.resourceDict["wheat"] + 1
	
		for i in range(0, self.numSettlements + self.numCities - 2):
			self.resourceDict["sheep"] = self.resourceDict["sheep"] + 1
			self.resourceDict["wood"] = self.resourceDict["wood"] + 1
			self.resourceDict["brick"] = self.resourceDict["brick"] + 1
			self.resourceDict["wheat"] = self.resourceDict["wheat"] + 1

		for i in range(0, self.numCities):
			self.resourceDict["ore"] = self.resourceDict["ore"] + 3
			self.resourceDict["wheat"] = self.resourceDict["wheat"] + 2

		for i in range(0, self.minRoadsNeeded - (2*self.devCardDict["roadBuilding"]) -2):
			self.resourceDict["wood"] = self.resourceDict["wood"] + 1
			self.resourceDict["brick"] = self.resourceDict["brick"] + 1

		return self.resourceDict

	'''
	calculates the total cost by summing the resource cards required for the victory
	'''	
	def calcTotalCost(self):
		for key,val in self.resourceDict.items():
			self.totalCost = self.totalCost + val
		'''
		for i in range(0, self.devCardDict["knight"]):
			self.totalCost = self.totalCost -1
		'''

		return self.totalCost

	'''
	calculates the victory points in this particular solution
	'''
	def vicPoints(self):
		self.totalVicPts = self.devCardDict["victoryPoint"]  + self.numSettlements 
		self.totalVicPts = self.totalVicPts + (2* self.numCities)
		if self.longestRoad == True:
			self.totalVicPts = self.totalVicPts + 2
		if self.largestArmy == True:
			self.totalVicPts = self.totalVicPts + 2


	'''
	makes sure that victory points are greater than 10
	'''
	def sanityCheck(self):
		if (self.totalVicPts >=10):
			return True
		return False

	'''	
	'''
	def __lt__(self, other):
		return self.totalCost < other.totalCost



