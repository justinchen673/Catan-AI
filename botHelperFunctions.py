################################################################################
# FOR PLACING SETTLEMENTS
################################################################################

def getRollProbabilities():
	'''
	A dictionary that contains the chances that a certain number will be rolled
	on any given dice roll.
	'''

	return {
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


def obtainVertexRanks(board):
	'''
	This returns an array of the vertex ranks, which are comprised of 3
	components. The first
	'''

	vertexRanks = []
	for i in range(0, 54):
		vertexRanks.append([0, [], i])
	hexNum = 0
	for hex in board.hexes:
		for vertex in board.hexRelationMatrix[hexNum]:
			vertexRanks[vertex][0] += abs(7 - hex.number)
			vertexRanks[vertex][1].append((hex.resourceType, hex.number))
		hexNum += 1
	return vertexRanks


def obtainPotentialFirsts(vertexRanks, board, botName, maxRank):
	'''
	Gets a list of vertices that are viable for placement. This means it must
	be legal, and to narrow it down, the rank must not be higher than the
	parameter maxRank to eliminate clearly bad placements.
	'''

	potentialFirsts = []
	for vertex in vertexRanks:
		if len(vertex[1]) == 1:
			vertex[0] += 14
		elif len(vertex[1]) == 2:
			vertex[0] += 7

		if (vertex[0] < maxRank and board.canPlaceSettlement(vertex[2], botName, True)):
			potentialFirsts.append(vertex)
	return potentialFirsts


def categorizeVertices(oreWheatVertices, woodBrickVertices, straightNumVertices, potentialFirsts, maxRank):
	'''
	Categorizes vertices as adhering to either the ore / wheat strategy, the
	wood / brick strategy, or a straight numerical advantage strategy.
	'''

	probabilityDict = getRollProbabilities()

	for vertex in potentialFirsts:
		resourceDict = {
			"wheat": 0,
			"sheep": 0,
			"brick": 0,
			"ore": 0,
			"wood": 0,
			"sand": 0
		}
		for resource in vertex[1]:
			resourceDict[resource[0]] += probabilityDict[resource[1]]
		if (resourceDict["wheat"] > 0.08 and resourceDict["ore"] > 0.11):
			# This will occur about 10% of the time
			oreWheatVertices.append((vertex, resourceDict["wheat"] + resourceDict["ore"]))
		elif (resourceDict["wood"] > 0.08 and resourceDict["brick"] > 0.08):
			# This will occur about 13% of the time
			woodBrickVertices.append((vertex, resourceDict["wood"] + resourceDict["brick"]))
		elif (vertex[0] < maxRank):
			straightNumVertices.append(vertex)


def bestVertex(vertexList):
	'''
	Given a list of vertices that all fit a particular strategy, this function
	picks the best one.
	'''
	
	chosenVertex = None
	for vertex in vertexList:
		if chosenVertex == None:
			chosenVertex = vertex
		elif chosenVertex[1] < vertex[1]:
			chosenVertex = vertex
		elif chosenVertex[1] == vertex[1]:
			if (vertex[0][0] < chosenVertex[0][0]):
				chosenVertex = vertex
	return chosenVertex
