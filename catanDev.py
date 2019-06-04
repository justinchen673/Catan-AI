import csv
from setup import *
from board import *
from developmentCardActions import *
from buildFunctions import *
from gameFunctions import *
from tradeFunctions import *
from player import Player
from botFunctions import *

if __name__ == '__main__':

	#for newBoardLoop in range(0, 5000):
	playerList = []
	playerList.append(Player("A"))
	playerList.append(Player("B"))
	playerList.append(Player("C"))
	playerList.append(Player("D"))
	playerList[0].isBot = True
	playerList[1].isBot = True
	playerList[2].isBot = True
	playerList[3].isBot = True
	board = createBoard()

	board.placeSettlement(botPlaceFirstSettlement(board, playerList[0]), playerList[0])
	board.placeSettlement(botPlaceFirstSettlement(board, playerList[1]), playerList[1])
	board.placeSettlement(botPlaceFirstSettlement(board, playerList[2]), playerList[2])
	board.placeSettlement(botPlaceFirstSettlement(board, playerList[3]), playerList[3])
	board.placeSettlement(botPlaceSecondSettlement(board, playerList[3]), playerList[3])
	board.placeSettlement(botPlaceSecondSettlement(board, playerList[2]), playerList[2])
	board.placeSettlement(botPlaceSecondSettlement(board, playerList[1]), playerList[1])
	board.placeSettlement(botPlaceSecondSettlement(board, playerList[0]), playerList[0])
	board.printBoard()
	print()
	'''
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
		if (vertex[0] < 9 and board.canPlaceSettlement(vertex[2], "A", True)):
			potentialFirsts.append(vertex)

	#print(potentialFirsts)
	#print()

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


		print("OREWHEAT: ", oreWheatVertices)
		print("WOODBRICK:", woodBrickVertices)
		print("STRAIGHTNUM:", straightNumVertices)
		print()
		'''






	'''
	PLACEMENT GUIDE:
		Ore / Wheat:
			Plentiful ore and wheat, ore more so than wheat
			2:1 ore or wheat port nearby, or 3:1
			Opponents leave those open
		Wood / Brick:
			Plentiful wood and brick
			2:1 wood brick port nearby, very important
		If not, go for balance / straight numerical advantage.
		If highly rare resource, go for that
	'''
