class Win:

	'''
	This class defines a type of win the game. This is the list of be parsed when running
	the AI in order to find the win that is most probable for the player. The 
	characteristics of the class are similar to that of the  player class
	'''

	def __init__(self):

		#I haven't included  monoplies and year of plenty since they are very variable
		#and their use changes based on the iterations of the game
		self.devCardDict = {
			"knight": 0,
            "victoryPoint": 0,
            "roadBuilding": 0
		}

		#amount of resources required to get that victory
		self.resourceDict = {
			"wheat": 0,
            "sheep": 0,
            "brick": 0,
            "ore": 0,
            "wood": 0
		}

		#number of Settlements and Cities required in that win
		self.numSettlements = 0
		self.numCities = 0

		#bool based on whether or not a win required largest Arny
		self.largestArmy = False

		#bool based on whether or not win requires longest road as well as minimum roads
		#needed to win
		self.longestRoad = False
		self.minRoadsNeeded = 0

		#total victory points in this win
		self.totalVicPts = 0
		self.totalCost = 0

		#a number to help keep track of this exact win
		self.number = 0

	'''
	when you print the string you will get the number
	'''
	def __str__(self):
		return  str(self.number)

	'''
	defines the type of win/ what the player uses to win the game. 
	uses an input of similar dummy dictionaries and bools from the main AI function
	'''
	def setWinType(self, vicPts, army , road ,setts, cits):
		#if army has 2 vic points, then the win requires largest army
		if army == 2:
			self.devCardDict["knight"] = 3
			self.largestArmy = True

		#if win has 2 vic points, then the win requires longest road
		if road == 2:
			self.longestRoad = True

		#copies over the number of dev card victory points
		self.devCardDict["victoryPoint"] = vicPts

		#number of Settlements and cities in the win, cities divided by two, since they
		#are worth double
		self.numSettlements = setts
		self.numCities = int(cits/2)

		#set total victory points in this win
		self.totalVicPts = vicPts + army + road +setts + cits

	'''
	sets the information for roads
	including minimum roads needed and how many road building cards were uesd
	'''
	def setRoads(self, minR, rBuilding):
		self.minRoadsNeeded = minR
		self.devCardDict["roadBuilding"] = rBuilding

	'''
	sets the arbitary counter , just to help access and debugging in the future
	'''
	def setNumber(self, counter):
		self.number = counter

	'''
	calculate the total resouces requied to accomplish that particular winning strategy
	returns the dictionary of the resources
	'''	
	def calcResourceCost(self):

		#sum of all dev cards required in the win
		devSum = self.devCardDict["knight"] + self.devCardDict["victoryPoint"] + self.devCardDict["roadBuilding"]

		#adds neccesarry resources for all the dev cards
		for i in range(0, devSum):
			self.resourceDict["sheep"] = self.resourceDict["sheep"] + 1
			self.resourceDict["ore"] = self.resourceDict["ore"] + 1
			self.resourceDict["wheat"] = self.resourceDict["wheat"] + 1
		
		#add the neccesarry resource for all the settlements plus the cities minus 2
		#this is because all cities were settlements once
		#also we start with 2 settlements that are free
		for i in range(0, self.numSettlements + self.numCities - 2):
			self.resourceDict["sheep"] = self.resourceDict["sheep"] + 1
			self.resourceDict["wood"] = self.resourceDict["wood"] + 1
			self.resourceDict["brick"] = self.resourceDict["brick"] + 1
			self.resourceDict["wheat"] = self.resourceDict["wheat"] + 1

		#add neccesarry resources for all the Cities
		for i in range(0, self.numCities):
			self.resourceDict["ore"] = self.resourceDict["ore"] + 3
			self.resourceDict["wheat"] = self.resourceDict["wheat"] + 2

		#add neccessary resources for all roads built
		#minus road building since we accounted for that earlier
		#minus the 2 roads we started with
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
	sets the less than symbol for comparisons and sorting	
	'''
	def __lt__(self, other):
		return self.totalCost < other.totalCost



