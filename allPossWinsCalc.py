
from winType import *

'''
win combo =[devVic, army, road, settlements, cities]
'''

'''
This function find all the possible combinations of points for the game,
however it does not include everything, specifically,HOW the roads are obtained
	- ie, roadbuilding vs simple buying

It returns a 2-d list of size 143 
Each item inside the big list is the combination of points that lead to victory

'''
def findPossibleWins():
	#all the possibilities of victory points (from dev cards) that may be obtained
	devVic = [0,1,2,3,4,5]
	#you either have largest army or not
	largeArmy = [0,2]
	#you either have longest road or not
	longRoad = [0,2]
	#max number of settlements
	setts = [0,1,2,3,4,5]
	#max vic points from cities
	cits = [0,2,4,6,8]
	winCombo = []

	for i in devVic:
		for j in largeArmy:
			for k in longRoad:
				for l in setts:
					for m in cits:
						aWin = [i,j,k,l,m]
						vicPts = sum(aWin)
						#not possible to have more than 12, since by then you would 
						#have already won and the game would be over
						if vicPts < 10 or vicPts > 12:
							continue
						#if 12 vic points,you have to have longest road and a settlement
						#for more info look at the first webite in aiPrototype.txt
						if vicPts == 12 and (k == 0 or l == 0 ):
							continue
						#if 11 vic points you have to get longest road or largest army
						#for more info look at the first webite in aiPrototype.txt
						if vicPts == 11 and (j == 0 and k == 0):
							continue
						#if you have no settlement you must have atleast 2 cities
						if l==0 and m < 4:
							continue
						#if you have only 1 settlement you must have at least 1 ciy
						if l==1 and m <2:
							continue
						winCombo.append(aWin)
	return winCombo


'''
This function finds the minimum number of roads required to build that number of 
settlements and cities

The minroad changes depending on whether or not there is a longest road
'''
def findMinRoads(strat):
	minRoads = 0
	#you have to divideby 2 since the cities are stored as the number of victory points
	#they are worth
	numCits = int(strat[4]/2)

	#no more than 7 settlements + cities in any of the solutions,
	#since max 5 settlements + 2 cities = 9 vic points, after that must 
	#convert a settlement to a city, resulting in 10
	if strat[3] + numCits> 7:
		print(strat, "HUH?????????")

	#min road required without longest road
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

	#min roads required with longest road
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
creates an object of the Win class and then returns it
assgins in a number as well as all other relevant information that defines it
'''
def createWin(strategy, minRds, rBuilding, counter):
	w = Win()
	w.setWinType(strategy[0], strategy[1], strategy[2], strategy[3], strategy[4])
	w.setRoads(minRds, rBuilding)
	w.setNumber(counter)

	return w


'''
create all the possible basic win type, this time including the different costs incurred 
by whether or not a road building card is used

after accounting for this there are 348 different types of wins
'''	
def createWinList():
	pointCombinations = findPossibleWins()
	minRds = 0
	counter = 0
	wins = []

	for strategy in pointCombinations:
		minRds = findMinRoads(strategy)
		#for all strategies, first include a win with 0 road building cards
		counter = counter + 1
		w1 = createWin(strategy, minRds, 0, counter)
		wins.append(w1)
		#next if there are more than 4 roads in the game, include a win with 1 rb card
		if minRds >= 4:
			counter = counter + 1
			w2 = createWin(strategy, minRds, 1, counter )
			wins.append(w2) 
		#last if there are more than 6 roads in the game, include a win with 2 rb cards
		if minRds >= 6:
			counter = counter + 1
			w3 = createWin(strategy, minRds, 2, counter )
			wins.append(w3)

	return wins

'''
calculates the number and type of resource each different type of victory costs
'''
def calcCosts(winLt):
	for i in winLt:
		i.calcResourceCost()
		i.calcTotalCost()
		if not i.sanityCheck():
			print("HUHHHH!!!!!!!!!!!")

	return winLt

'''
sort the list of wins from minimum cost to maximum
'''
def sortWins(winLt):
	winLt.sort()
	return winLt

'''
simple print function to help visualize each win
'''
def printWin(aWin):
	print()
	print("Number:\t\t", aWin.number)
	print("Victory Points:\t", aWin.totalVicPts)
	print("Dev Cards:\t", aWin.devCardDict)
	print("Settlements:\t", aWin.numSettlements)
	print("Cities:\t\t", aWin.numCities)
	print("Roads:\t\t", aWin.minRoadsNeeded)
	print("Resource Cards:\t", aWin.resourceDict)
	print("Cost:\t\t", aWin.totalCost)

	return True

'''
main, create and complies all above functions into a usable win list
'''
def doEverything():
	winList = createWinList()
	print(len(winList))
	winList = calcCosts(winList)
	winList = sortWins(winList)

	return winList


'''
returns a list of all the wins that require 'num' number of settlements 
there are no wins with more than 5 settlements
	returns false and an empty list if they try to do this
'''
def findSettlements(wl, num):
	l = []
	if(num > 5):
		return False, l
	for i in wl:
		if i.numSettlements == num:
			l.append(i)
	return True, l

'''
returns a list of all the wins that require 'num' number of cities
there are no wins with more than 4 cities
	returns false and an empty list if they try to do this
'''
def findCities(wl,num):
	l = []
	if(num > 4):
		return False, l
	for i in wl:
		if i.numCities == num:
			l.append(i)
	return True, l

'''
returns a list of all the wins that require 'num' number of victory point cards 
there are no wins with more than 5 victory point cards since only 5 in the deck
	returns false and an empty list if they try to do this
'''
def findDevVicPoints(wl,num):
	l = []
	if(num >5):
		return False, l
	for i in wl:
		if i.devCardDict["devCardDict"] == num:
			l.append(i)
	return True, l

'''
returns a list of all the wins that require 'num' number of knights 
there are no wins with more than 3 knights, atleast in the current version of the game
	returns false and an empty list of they try to do this
'''
def findKnights(wl,num):
	l = []
	if(num >3):
		return False, l
	for i in wl:
		if i.devCardDict["knights"] == num:
			l.append(i)
	return True, l

'''
returns a list of all the wins that require 'num' number of road building dev cards 
there are no wins with more than 2 cards (the game only comes with 2)
	returns false and an empty list if they try to do this
'''
def findRoadBuilding(wl,num):
	l = []
	if(num >2):
		return False, l
	for i in wl:
		if i.devCardDict["roadBuilding"] == num:
			l.append(i)
	return True, l

'''
returns a list of all the wins that require 'num' number of minimum roads to win 
there are no wins with more than 9 min roads or less than 2 (you start with 2)
	returns false and an empty list if they try to do this
'''
def findMinimumRoads(wl, num):
	l = []
	if(num > 9 or num < 2):
		return False, l
	for i in wl:
		if i.minRoadsNeeded == num:
			l.append(i)
	return True, l

'''
returns a list of all the wins that require 'num' number totall victory points to win 
there are no wins with more than 12 pts or less than 10
	returns false and an empty list if they try to do this
'''
def findTotalVicPoints(wl,num):
	l = []
	if(num > 12 or num < 10):
		return False, l
	for i in wl:
		if i.totalVicPts == num:
			l.append(i)
	return True, l


winList = doEverything()
for i in winList:
	print(i)
printWin(winList[0])

'''
#example of the find functions
works,wl1 = findTotalVicPoints(winList,12)
print(len(wl1))
for i in wl1:
	printWin(i)

'''
print(len(winList))

