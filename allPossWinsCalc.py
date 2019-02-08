
from winType import *

'''
[devVic, army, road, settlements, cities]
'''
def findPossibleWins():

	devVic = [0,1,2,3,4,5]
	largeArmy = [0,2]
	longRoad = [0,2]
	setts = [0,1,2,3,4,5]
	cits = [0,2,4,6,8]
	winCombo = []

	for i in devVic:
		for j in largeArmy:
			for k in longRoad:
				for l in setts:
					for m in cits:
						aWin = [i,j,k,l,m]
						vicPts = sum(aWin)
						if vicPts < 10 or vicPts > 12:
							continue
						if vicPts == 12 and (k == 0 or l == 0 ):
							continue
						if vicPts == 11 and (j == 0 and k == 0):
							continue
						if l==0 and m < 4:
							continue
						if l==1 and m <2:
							continue
						winCombo.append(aWin)
	return winCombo


'''

'''
def findMinRoads(strat):
	minRoads = 0
	numCits = int(strat[4]/2)
	if strat[3] + numCits> 7:
		print(strat, "HUH?????????")
	if strat[2] == 0:
		if strat[3] + numCits == 2:
			minRoads = 2
		if strat[3] + numCits == 3:
			minRoads = 3
		if strat[3] + numCits == 4:
			minRoads = 4
		if strat[3] + numCits == 5:
			minRoads = 5
		if strat[3] + numCits == 6:
			minRoads = 6
		if strat[3] + numCits == 7:
			minRoads = 8

	if strat[2] == 2:
		if strat[3] + numCits == 2:
			minRoads = 5
		if strat[3] + numCits == 3:
			minRoads = 5
		if strat[3] + numCits == 4:
			minRoads = 6
		if strat[3] + numCits == 5:
			minRoads = 7
		if strat[3] + numCits == 6:
			minRoads = 8
		if strat[3] + numCits == 7:
			minRoads = 9

	return minRoads

'''

'''
def createWin(strategy, minRds, rBuilding, counter):
	w = Win()
	w.setWinType(strategy[0], strategy[1], strategy[2], strategy[3], strategy[4])
	w.setRoads(minRds, rBuilding)
	w.setNumber(counter)

	return w


'''

'''	
def createWinList():
	pointCombinations = findPossibleWins()
	minRds = 0
	counter = 0
	wins = []
	for strategy in pointCombinations:
		minRds = findMinRoads(strategy)
		counter = counter + 1
		w1 = createWin(strategy, minRds, 0, counter)
		wins.append(w1)
		if minRds == 4 or minRds == 5:
			counter = counter + 1

			w2 = createWin(strategy, minRds, 1, counter )
			wins.append(w2) 
		if minRds >= 6:
			counter = counter + 1
			w3 = createWin(strategy, minRds, 2, counter )
			wins.append(w3)
	return wins

'''

'''
def calcCosts(winLt):
	for i in winLt:
		i.calcResourceCost()
		i.calcTotalCost()
		if not i.sanityCheck():
			print("HUHHHH!!!!!!!!!!!")

	return winLt


def sortWins(winLt):
	winLt.sort()
	return winLt

'''

'''
def printWin(aWin):
	print()
	print("Number:\t\t", aWin.number)
	print("______________________________________")
	print("Victory Points:\t", aWin.totalVicPts)
	print("Dev Cards:\t", aWin.devCardDict)
	print("Settlements:\t", aWin.numSettlements)
	print("Cities:\t\t", aWin.numCities)
	print("Roads:\t\t", aWin.minRoadsNeeded)
	print("Resource Cards:\t", aWin.resourceDict)
	print("Cost:\t\t", aWin.totalCost)

'''

'''
winList = createWinList()
for i in winList:
	print(i)
print(len(winList))
winList = calcCosts(winList)
winList = sortWins(winList)
for i in winList:
	print(i)
printWin(winList[0])

