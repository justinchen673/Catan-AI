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

def botPlaceFirstSettlement(board, playerList, botName):
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

	# vertexRanks contains the rank (low is good) and the resources it gets
	vertexRanks = []
	for i in range(0, 54):
		vertexRanks.append([0, [], i])
	hexNum = 0
	for hex in board.hexes:
		for vertex in board.hexRelationMatrix[hexNum]:
			vertexRanks[vertex][0] += abs(7 - hex.number)
			vertexRanks[vertex][1].append((hex.resourceType, hex.number))
		hexNum += 1

	# for the first settlement:
	potentialFirsts = []
	for vertex in vertexRanks:
		if len(vertex[1]) == 1:
			vertex[0] += 14
		elif len(vertex[1]) == 2:
			vertex[0] += 7

		if (vertex[0] < 9 and board.canPlaceSettlement(vertex[2], botName, playerList)):
			potentialFirsts.append(vertex)

	oreWheatVertices = []
	woodBrickVertices = []
	straightNumVertices = []

	for vertex in potentialFirsts:
		#print(vertex)
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
	print("OREWHEAT", oreWheatVertices)
	print("WOODBRICK", woodBrickVertices)
	print("STRAIGHNUM", straightNumVertices)

	# Start selecting a vertex after narrowing down to the three strategies
	print()
	chosenVertex = None

	# Prioritize ore / wheat since it's the least likely
	if (len(oreWheatVertices) != 0):
		print("Picked ore / wheat")
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
		print("Picked wood / brick")
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
		print("Picked straight num")
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

def botBuildFirstRoad():
	return

def botTradeAcceptance():
	return
