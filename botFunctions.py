from board import *

def botHalveHand():
	return

def botGameTurn():
	return

def botTrade():
	return

def botBuild():
	return

def botBuyDevCard():
	return

def botUseDevCard():
	return

def botMoveRobber():
	return

def botChooseWhoToRob():
	return

def botPlaceSettlement():
	return

def botPlaceFirstSettlement(board, bot):
	'''
	Places the first settlement.
	1. Lists the vertices by how good the surrounding numbers.
	2. Narrows it down to a certain threshold (arbitrary but tested).
	3. Categorizes the vertices into 3 separate strategies: If there's lots of
	   ore / wheat, it goes that strategy, same for wood / brick. If it fits
	   neither, it's categorized as a straight numerical advantage.
	4. The bot will go with ore/wheat or wood/brick if any exist. If not, it'll
	   go for a straight numerical advantage.
	'''

	# chances that a certain number will be rolled on any given dice roll
	probabilityDict = {
		0: 0,
		2: .02778,
		3: .05556,
		4: .08336,
		5: .11111,
		6: .13889,
		7: .16667,
		8: .13889,
		9: .11111,
		10: .08336,
		11: .05556,
		12: .02778
	}

	# vertexRanks contains the rank (low is good) and the resources it gets.
	# Rank is based on the likelihood of getting a resource from that vertex on
	# any given dice roll
	vertexRanks = []
	for i in range(0, 54):
		vertexRanks.append([0, [], i])
	hexNum = 0
	for hex in board.hexes:
		for vertex in board.hexRelationMatrix[hexNum]:
			vertexRanks[vertex][0] += abs(7 - hex.number)
			vertexRanks[vertex][1].append((hex.resourceType, hex.number))
		hexNum += 1

	# Narrows down the list of good placement vertices
	potentialFirsts = []
	for vertex in vertexRanks:
		if len(vertex[1]) == 1:
			vertex[0] += 14
		elif len(vertex[1]) == 2:
			vertex[0] += 7

		if (vertex[0] < 9 and board.canPlaceSettlement(vertex[2], bot.name, True)):
			potentialFirsts.append(vertex)

	# Categorize vertices as these 3 categories
	oreWheatVertices = []
	woodBrickVertices = []
	straightNumVertices = []

	for vertex in potentialFirsts:
		resourceDict = {
			"wheat": 0,
			"sheep": 0,
			"brick": 0,
			"ore": 0,
			"wood": 0
		}
		for resource in vertex[1]:
			resourceDict[resource[0]] += probabilityDict[resource[1]]
		if (resourceDict["wheat"] > 0.08 and resourceDict["ore"] > 0.11):
			# This will occur about 10% of the time
			oreWheatVertices.append((vertex, resourceDict["wheat"] + resourceDict["ore"]))
		elif (resourceDict["wood"] > 0.08 and resourceDict["brick"] > 0.08):
			# This will occur about 13% of the time
			woodBrickVertices.append((vertex, resourceDict["wood"] + resourceDict["brick"]))
		elif (vertex[0] <= 7):
			straightNumVertices.append(vertex)

	# Start selecting a vertex after narrowing down to the three strategies
	chosenVertex = None

	# Prioritize ore / wheat since it's the least likely
	if (len(oreWheatVertices) != 0):
		# Set bot strategy as ore/wheat
		bot.oreWheat = True
		# If multiple exist, use the best one.
		for vertex in oreWheatVertices:
			if chosenVertex == None:
				chosenVertex = vertex
			elif chosenVertex[1] < vertex[1]:
				chosenVertex = vertex
			elif chosenVertex[1] == vertex[1]:
				if (vertex[0][0] < chosenVertex[0][0]):
					chosenVertex = vertex
		return chosenVertex[0][2]
	elif (len(woodBrickVertices) != 0):
		# Set bot strategy as wood/brick
		bot.woodBrick = True
		# If multiple exist, use the best one.
		for vertex in woodBrickVertices:
			if chosenVertex == None:
				chosenVertex = vertex
			elif chosenVertex[1] < vertex[1]:
				chosenVertex = vertex
			elif chosenVertex[1] == vertex[1]:
				if (vertex[0][0] < chosenVertex[0][0]):
					chosenVertex = vertex
		return chosenVertex[0][2]
	else:
		# Set bot strategy as numerical
		bot.straightNum = True
		# Last resort, use straight numerical advantage
		for vertex in straightNumVertices:
			if chosenVertex == None:
				chosenVertex = vertex
			elif (vertex[0] < chosenVertex[0]):
				chosenVertex = vertex
		return chosenVertex[2]


def botPlaceSecondSettlement():
	return

def botBuildRoad():
	return

def botBuildSecondRoad():
	return

def botBuildFirstRoad(board, bot, firstVertex):
	
	return

def botTradeAcceptance():
	return
