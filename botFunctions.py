def calculateStrategyCost(bot, board):
	rollProbabilities = {
		2: 0.02778,
		3: 0.05556,
		4: 0.08336,
		5: 0.11111,
		6: 0.13889,
		8: 0.13889,
		9: 0.11111,
		10: 0.08336,
		11: 0.05556,
		12: 0.02778
	}

	expectedResourcesPerRoll = {
		"wheat": 0,
		"sheep": 0,
		"brick": 0,
		"ore": 0,
		"wood": 0
	}

	for i in range(0, 19):
		currentHex = board.hexes[i]
		if (currentHex.resourceType == "sand"):
			continue
		for j in board.hexRelationMatrix[i]:
			if board.vertices[j].playerName == bot.name:
				if (board.vertices[j].city):
					expectedResourcesPerRoll[currentHex.resourceType] += rollProbabilities[currentHex.number] * 2
				else:
					expectedResourcesPerRoll[currentHex.resourceType] += rollProbabilities[currentHex.number]

	print(expectedResourcesPerRoll)
	rollsNeeded = {
		"wheat": 0,
		"sheep": 0,
		"brick": 0,
		"ore": 0,
		"wood": 0
	}
	expectedResourceCount = {
		"wheat": 0,
		"sheep": 0,
		"brick": 0,
		"ore": 0,
		"wood": 0
	}
	for win in bot.winList:
		minRolls = float('inf')
		for resource in rollsNeeded:
			if (expectedResourcesPerRoll[resource] != 0):
				rollsNeeded[resource] = win.resourceDict[resource] / expectedResourcesPerRoll[resource]
				if (rollsNeeded[resource] < minRolls):
					minRolls = rollsNeeded[resource]
			else:
				rollsNeeded[resource] = -1
		for resource in expectedResourceCount:
			expectedResourceNum = minRolls * expectedResourcesPerRoll[resource]
		print(expectedResourceCount)



	return

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

def botPlaceFirstSettlement():
	return

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

	
