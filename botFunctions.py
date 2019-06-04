from board import *
from botHelperFunctions import *
import random

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

	# vertexRanks contains the rank (low is good) and the resources it gets.
	# Rank is based on the likelihood of getting a resource from that vertex on
	# any given dice roll
	vertexRanks = obtainVertexRanks(board)

	# Narrows down the list of good placement vertices
	potentialFirsts = obtainPotentialFirsts(vertexRanks, board, bot.name, 9)

	# Categorize vertices as these 3 categories
	oreWheatVertices = []
	woodBrickVertices = []
	straightNumVertices = []

	categorizeVertices(oreWheatVertices, woodBrickVertices, straightNumVertices, potentialFirsts, 9)

	# Start selecting a vertex after narrowing down to the three strategies
	# Prioritize ore / wheat since it's the least likely
	if (len(oreWheatVertices) != 0):
		# Set bot strategy as ore/wheat
		bot.oreWheat = True
		# If multiple exist, use the best one.
		chosenVertex = bestVertex(oreWheatVertices)
		return chosenVertex[0][2]
	elif (len(woodBrickVertices) != 0):
		# Set bot strategy as wood/brick
		bot.woodBrick = True
		# If multiple exist, use the best one.
		chosenVertex = bestVertex(woodBrickVertices)
		return chosenVertex[0][2]
	else:
		chosenVertex = None
		# Set bot strategy as numerical
		bot.straightNum = True
		# Last resort, use straight numerical advantage
		for vertex in straightNumVertices:
			if chosenVertex == None:
				chosenVertex = vertex
			elif (vertex[0] < chosenVertex[0]):
				chosenVertex = vertex
		return chosenVertex[2]


def botPlaceSecondSettlement(board, bot):
	'''
	Works the same way as botPlaceFirstSettlement, except some of the max ranks
	are different and the logic after sorting vertices accounts for less
	available spots.
	'''

	vertexRanks = obtainVertexRanks(board)

	potentialFirsts = obtainPotentialFirsts(vertexRanks, board, bot.name, 13)

	oreWheatVertices = []
	woodBrickVertices = []
	straightNumVertices = []

	categorizeVertices(oreWheatVertices, woodBrickVertices, straightNumVertices, potentialFirsts, 13)

	if (bot.oreWheat == True and len(oreWheatVertices) != 0) or (len(woodBrickVertices) == 0 and len(straightNumVertices) == 0):
		chosenVertex = bestVertex(oreWheatVertices)
		return chosenVertex[0][2]
	elif (bot.woodBrick == True and len(woodBrickVertices) != 0) or (len(straightNumVertices) == 0):
		chosenVertex = bestVertex(woodBrickVertices)
		return chosenVertex[0][2]
	else:
		chosenVertex = None
		for vertex in straightNumVertices:
			if chosenVertex == None:
				chosenVertex = vertex
			elif (vertex[0] < chosenVertex[0]):
				chosenVertex = vertex
		return chosenVertex[2]

def botBuildRoad():
	return

def botBuildSecondRoad(board, firstVertex):
	'''
	Places down the second road.

	FOR NOW THIS IS JUST A RANDOM SELECTED ROAD, DO SOMETHING BETTER LATER
	'''
	possibleVertices = board.vertexRelationMatrix[firstVertex]
	return possibleVertices[random.randint(0, len(possibleVertices) - 1)]

def botBuildFirstRoad(board, firstVertex):
	'''
	Places down the first road.

	FOR NOW THIS IS JUST A RANDOM SELECTED ROAD, DO SOMETHING BETTER LATER
	'''
	possibleVertices = board.vertexRelationMatrix[firstVertex]
	return possibleVertices[random.randint(0, len(possibleVertices) - 1)]

def botTradeAcceptance():
	return
