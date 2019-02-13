import random
from setup import *
from board import *
from developmentCardActions import *
from player import Player

def diceRoll():
    '''
    Simulates rolling a pair of dice that are numbered 1-6 each. Returns a
    number 2-12 at varying frequencies.
    '''

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


def getPlayerFromName(playerList, playerName):
    '''
    Simple function that returns the player (in the playerList) based on name.
    '''

    for i in playerList:
        if i.name == playerName:
            return i
    return None


def moveRobber(board, mover, playerList):
    '''
    Allows the player to move the robber to any hex they want. Mover represents
    the player who gets to move the robber.
    '''

    # Find out where the robber currently is
    currentHex = 0
    for i in range(0, 19):
        if (board.hexes[i].robber):
            currentHex = i
            board.hexes[i].robber = False
            break

    # Take input for the new location
    notPlaced = True
    newHex = 0
    while (notPlaced):
        newHex = input("Player " + mover.name + ", which hex would you like to move the robber to? Select a number 0 - 18, starting from the top left hex and moving right. ")
        if (not newHex.isdigit()):
            print("Invalid number.")
            continue
        newHex = int(newHex)
        if (newHex == currentHex):
            print("The robber is already there. Select a different hex.")
        elif (newHex < 0 or newHex > 18):
            print("Please enter a hex between 0 and 18.")
        else:
            board.hexes[newHex].robber = True
            notPlaced = False

    # Give the player a resource from a neighboring player
    adjacentVertices = board.hexRelationMatrix[newHex]
    victim = None
    possibleVictims = []
    # Add the people next to the robber to the possible victims list
    for vertex in adjacentVertices:
        if (board.vertices[vertex].empty == False and board.vertices[vertex].playerName != mover.name and board.vertices[vertex].playerName not in possibleVictims):
            possibleVictims.append(getPlayerFromName(playerList, board.vertices[vertex].playerName))

    if (len(possibleVictims) == 1):
        victim = possibleVictims[0]
    elif (len(possibleVictims) > 1):
        # Choose someone to steal from and set it to "victim"
        notChosen = True
        while (notChosen):
            name = input("Player " + mover.name + ", who would you like to steal from? ")
            if (name not in possibleVictims):
                print("Invalid user.")
            else:
                for i in range(0, len(possibleVictims)):
                    if possibleVictims[i] == name:
                        victim = possibleVictims[i]

    if (victim != None):
        # Put their resources in a list and take one at random
        resourceTheftList = []
        for resource in victim.resourceDict:
            for i in range(0, victim.resourceDict[resource]):
                resourceTheftList.append(resource)
        if (len(resourceTheftList) != 0):
            randomIndex = random.randint(0, len(resourceTheftList))
            victim.resourceDict[resourceTheftList[randomIndex]] -= 1
            mover.resourceDict[resourceTheftList[randomIndex]] += 1
            print("Successfully stole " + resourceTheftList[randomIndex])

    board.printBoard()


def halveHand(player, originalNumResources):
    '''
    Asks the player to remove cards from their hand until they're under half of
    what they originally had. Called when a seven is rolled and a player has
    more than 7 cards.
    '''

    print("Player " + player.name + ":")
    targetNum = originalNumResources / 2
    while (True):
        player.printHand()
        print("Please enter the name of the resource you would like to throw away.")
        toDiscard = input()
        if (toDiscard not in player.resourceDict):
            print("Invalid resource.")
        elif (player.resourceDict[toDiscard] == 0):
            print("You don't have any " + toDiscard + ".")
        else:
            player.resourceDict[toDiscard] -= 1
            if (player.numResources() <= targetNum):
                return




def handOutResources(board, playerList, roll):
    '''
    Based on the dice roll, hands out all of the resources. 7 will NOT be an
    input, as that calls for the robber.
    '''

    for i in range(0, 19):
        currentHex = board.hexes[i]
        # If the roll is the number on the board and there's no robber there
        if (roll == currentHex.number and currentHex.robber == False):
            for j in board.hexRelationMatrix[i]:
                # j is the vertex number that can get resources
                if board.vertices[j].empty == False:
                    # That player gets a resource
                    if (board.vertices[j].city):
                        getPlayerFromName(playerList, board.vertices[j].playerName).resourceDict[currentHex.resourceType] += 2
                    else:
                        getPlayerFromName(playerList, board.vertices[j].playerName).resourceDict[currentHex.resourceType] += 1


def printHelp():
    '''
    Outputs a list of commands that a user can call during their turn.
    '''

    print("\t-t is for trading, either with a player or with the bank.")
    print("\t-b is for building.")
    print("\t-d is for using a development card.")
    print("\t-e is for ending your turn.")


def bankTrade(board, player):
    '''
    Allows a user to trade with the bank. The player can always do a 4-1
    exchange, but depending on their ports they may be able to do 3-1 or 2-1
    trades as well.
    '''

    print("\tHere are all possible trades you can do with the bank:")

    wheatReq = 4
    sheepReq = 4
    brickReq = 4
    oreReq = 4
    woodReq = 4

    # Check for ports
    for vertex in board.vertices:
        if vertex.playerName == player.name and vertex.port != None:
            print("yeet")
            # There is a port
            if vertex.port.number == 3:
                # This is a wild card, so change the default ones
                if wheatReq == 4:
                    wheatReq = 3
                if sheepReq == 4:
                    sheepReq = 3
                if brickReq == 4:
                    brickReq = 3
                if oreReq == 4:
                    oreReq = 3
                if woodReq == 4:
                    woodReq = 3
            else:
                # This is a specific resource port
                if (vertex.port.resourceType == "wheat"):
                    wheatReq = 2
                if (vertex.port.resourceType == "sheep"):
                    sheepReq = 2
                if (vertex.port.resourceType == "brick"):
                    brickReq = 2
                if (vertex.port.resourceType == "ore"):
                    oreReq = 2
                if (vertex.port.resourceType == "wood"):
                    woodReq = 2


    # NEED TO IMPLEMENT PORTS: WILL STILL KEEP FORMAT THOUGH
    print("\t" + str(wheatReq) + " wheat -> 1 ?")
    print("\t" + str(sheepReq) + " sheep -> 1 ?")
    print("\t" + str(brickReq) + " brick -> 1 ?")
    print("\t" + str(oreReq) + " ore   -> 1 ?")
    print("\t" + str(woodReq) + " wood  -> 1 ?")

    # Get the resource to be traded in
    print("\tWhat resource are you trading in? Type in the full resource name.")
    tradeIn = input("\t")
    tradeQuantity = 0
    if (tradeIn == "wheat"):
        if player.resourceDict["wheat"] < wheatReq:
            print("\tYou don't have enough wheat.")
            return
        else:
            tradeQuantity = wheatReq
    elif (tradeIn == "sheep"):
        if player.resourceDict["sheep"] < sheepReq:
            print("\tYou don't have enough sheep.")
            return
        else:
            tradeQuantity = sheepReq
    elif (tradeIn == "brick"):
        if player.resourceDict["brick"] < brickReq:
            print("\tYou don't have enough brick.")
            return
        else:
            tradeQuantity = brickReq
    elif (tradeIn == "ore"):
        if player.resourceDict["ore"] < oreReq:
            print("\tYou don't have enough ore.")
            return
        else:
            tradeQuantity = oreReq
    elif (tradeIn == "wood"):
        if player.resourceDict["wood"] < woodReq:
            print("\tYou don't have enough wood.")
            return
        else:
            tradeQuantity = woodReq
    else:
        print("\tInvalid resource.")
        return

    print("\tWhat resource are you trading " + tradeIn + " for?")
    tradeFor = input("\t")
    if not tradeFor in player.resourceDict:
        print("\tInvalid resource.")
    else:
        # The actual trade itelf
        player.resourceDict[tradeIn] -= tradeQuantity
        player.resourceDict[tradeFor] += 1
        print("\tTrade successful!")
        print()
        player.printHand()


def playerTrade(player1, player2):
    '''
    Allows two players to trade with each other. player1 will be the player
    whose turn it currently is.
    '''

    # Get the resource and number to be traded from the first player
    print("\tPlayer " + player1.name + ", what resource are you trading in? Type in the full resource name.")
    resource1 = input("\t")
    if not resource1 in player1.resourceDict:
        print("\tInvalid resource.")
        return

    print("\tHow many " + resource1 + " are you trading?")
    quantity1 = input("\t")
    if (not quantity1.isdigit()):
        print("\tInvalid number.")
        return
    quantity1 = int(quantity1)
    if (quantity1 > player1.resourceDict[resource1] or quantity1 < 1):
        print("\tYou don't have enough " + resource1 + ".")
        return

    # Get the resource and number to be traded from the second player
    print("\tPlayer " + player2.name + ", what resource are you trading in? Type in the full resource name.")
    resource2 = input("\t")
    if not resource2 in player2.resourceDict:
        print("\tInvalid resource.")
        return

    print("\tHow many " + resource2 + " are you trading?")
    quantity2 = input("\t")
    if (not quantity2.isdigit()):
        print("\tInvalid number.")
        return
    quantity2 = int(quantity2)
    if (quantity2 > player2.resourceDict[resource2] or quantity2 < 1):
        print("\tYou don't have enough " + resource2 + ".")
        return

    # If it reaches this point, the trade has no barriers and can go through
    player1.resourceDict[resource1] -= quantity1
    player1.resourceDict[resource2] += quantity2
    player2.resourceDict[resource1] += quantity1
    player2.resourceDict[resource2] -= quantity2
    print("\tTrade successful!")
    print()
    player1.printHand()


def buildCity(board, player):
    '''
    Asks the player to build a city on top of one of their currently existing
    settlements.
    '''

    # Checks if the player has the resources needed to build a city
    if (player.resourceDict["wheat"] < 2 or player.resourceDict["ore"] < 3):
        print("\tYou don't have the necessary resources to build a city.")
        return

    settlementVertices = []
    for i in range(0, len(board.vertices)):
        if (board.vertices[i].playerName == player.name and board.vertices[i].city == False):
            # This means there is a settlement on vertex i
            settlementVertices.append(i)

    # Ensures there's a settlement to put the city on
    if (len(settlementVertices) == 0):
        print("\tYou have no settlements to put cities on.")
        return

    board.printBoard()
    print()
    print("\tWhich settlement would you like to place it on? Pick the settlement number, starting from top left (and starting from 0).")
    settlementNum = input("\t")
    if (not settlementNum.isdigit()):
        print("\tInvalid number.")
        return
    settlementNum = int(settlementNum)
    if (settlementNum < 0 or settlementNum >= len(settlementVertices)):
        print("\tInvalid number.")
        return

    board.vertices[settlementVertices[settlementNum]].city = True
    player.resourceDict["wheat"] -= 2
    player.resourceDict["ore"] -= 3
    player.points += 1
    board.printBoard()


def buildSettlement(board, player):
    '''
    Asks the player to build a settlement at a vertex and ensures that the move
    is legal.
    '''

    # Checks if the player has the resources needed to build a settlement
    if (player.resourceDict["wheat"] < 1 or player.resourceDict["wood"] < 1 or player.resourceDict["sheep"] < 1 or player.resourceDict["brick"] < 1):
        print("\tYou don't have the necessary resources to build a settlement.")
        return

    board.printBoard()
    print()
    print("\tWhich vertex would you like to place it on? Pick the vertex number, starting from top left (and starting from 0).")
    vertex = input("\t")
    if (not vertex.isdigit()):
        print("\tInvalid number.")
        return
    vertex = int(vertex)

    # Determines if you can place a settlement on the inputted vertex. False
    # means that this isn't the first settlement of the game.
    if (board.canPlaceSettlement(vertex, player.name, False)):
        board.placeSettlement(vertex, player)
        board.printBoard()

        player.resourceDict["wheat"] -= 1
        player.resourceDict["wood"] -= 1
        player.resourceDict["sheep"] -= 1
        player.resourceDict["brick"] -= 1
    else:
        print("\tIllegal settlement placement.")


def buildRoad(board, player):
    '''
    Asks the player to build a road between to vertices and ensures that the
    move is legal.
    '''

    # Checks if the player has the resources needed to build a road
    if (player.resourceDict["wood"] < 1 or player.resourceDict["brick"] < 1):
        print("\tYou don't have the necessary resources to build a road.")
        return

    # Get the two vertices the road should connect.
    board.printBoard()
    print()
    print("\tEnter the number of the first vertex it will connect to.")
    vertex1 = input("\t")
    if (not vertex1.isdigit()):
        print("\tInvalid number.")
        return
    vertex1 = int(vertex1)

    print("\tEnter the number of the second vertex it will connect to.")
    vertex2 = input("\t")
    if (not vertex2.isdigit()):
        print("\tInvalid number.")
        return
    vertex2 = int(vertex2)

    # Attempt to place it
    if (board.canPlaceRoad(vertex1, vertex2, player.name)):
        board.placeRoad(vertex1, vertex2, player.name)
        board.printBoard()

        player.resourceDict["wood"] -= 1
        player.resourceDict["brick"] -= 1
    else:
        print("\tIllegal road placement.")


def buildDevCard(player, devCardDeck):
    '''
    Gives the player a development card off of the deck, and returns the string
    containing the name of the development card. That's for tracking which cards
    were obtained during the current turn (which the player cannot immediately
    use).
    '''

    # Checks if the player has the resources needed to build a road
    if (player.resourceDict["ore"] < 1 or player.resourceDict["sheep"] < 1 or player.resourceDict["wheat"] < 1):
        print("\tYou don't have the necessary resources to get a development card.")
        return None

    # Ensures there are still development cards
    if (len(devCardDeck) == 0):
        print("\tNo more development cards remain.")
        return None

    newCard = devCardDeck.pop()
    player.devCardDict[newCard] += 1
    player.resourceDict["ore"] -= 1
    player.resourceDict["sheep"] -= 1
    player.resourceDict["wheat"] -= 1

    print()
    player.printHand()

    return newCard



if __name__ == '__main__':
    playerList = initializePlayers()
    devCardDeck = initializeDevCards()
    board = createBoard()

    # Setup Phase
    placeFirstSettlements(board, playerList)

    # Game Phase
    currentPlayerIndex = 0
    while(not playerList[currentPlayerIndex].victorious()):

        currentPlayer = playerList[currentPlayerIndex]

        board.printBoard()

        # Roll the dice and resolve consequences of the dice roll
        roll = diceRoll()
        print()
        print("A " + str(roll) + " was rolled.")
        if (roll == 7):
            # Player moves robber
            moveRobber(board, currentPlayer, playerList)
            for player in playerList:
                if player.numResources() > 7:
                    halveHand(player, player.numResources())
        else:
            handOutResources(board, playerList, roll)

        # Begin the action phase for the current player
        print("Player " + currentPlayer.name + ":")
        currentPlayer.printHand()
        # Keep track of what development cards the player obtains in their turn. They can't immediately use them.
        obtainedDevCards = {
            "Knight": 0,
            "Year of Plenty": 0,
            "Monopoly": 0,
            "Road Building": 0,
            "Victory Point": 0
        }
        # Allow commands
        notDone = True
        usedDevCard = False
        while(notDone):
            print()
            print("What would you like to do? Type a command, or -h for a list of commands.")
            command = input()
            if (command == "-h"):
                printHelp()
            elif (command == "-t"):
                print("\tWho would you like to trade with? Enter the player's name or type \"bank\" if you would like to trade with the bank.")
                trader = input("\t")
                trader = trader.capitalize()
                if (trader == currentPlayer.name):
                    print("\tYou can't trade with yourself.")
                elif (trader == "Bank"):
                    # Trade with the bank
                    bankTrade(board, currentPlayer)
                elif (getPlayerFromName(playerList, trader) != None):
                    # Trade with another player
                    playerTrade(currentPlayer, getPlayerFromName(playerList, trader))
                else:
                    print("\tInvalid command.")
            elif (command == "-b"):
                print("\tWhat would you like to build? Type -c for a city, -s for a settlement, -r for a road, or -d for a development card.")
                toBuild = input("\t")
                if (toBuild == "-c"):
                    buildCity(board, currentPlayer)
                elif (toBuild == "-s"):
                    buildSettlement(board, currentPlayer)
                elif (toBuild == "-r"):
                    buildRoad(board, currentPlayer)
                elif (toBuild == "-d"):
                    result = buildDevCard(currentPlayer, devCardDeck)
                    if (result != None):
                        obtainedDevCards[result] += 1
                else:
                    print("\tInvalid command.")
            elif (command == '-d'):
                if (usedDevCard):
                    print("\tYou may only use 1 development card per turn.")
                else:
                    usedDevCard = True
                    print("\tWhich development card would you like to use? Type -k to use a knight, -y to use Year of Plenty, -m to use monopoly, or -r to use road building.")
                    toUse = input("\t")
                    if (toUse == "-k"):
                        # Ensures they have a knight, and that they didn't just get it this turn.
                        if (currentPlayer.devCardDict["Knight"] - obtainedDevCards["Knight"] - 1 >= 0):
                            moveKnight(board, currentPlayer, playerList)
                        else:
                            print("\tYou can't use a knight.")
                    elif (toUse == "-y"):
                        if (currentPlayer.devCardDict["Year of Plenty"] - obtainedDevCards["Year of Plenty"] - 1 >= 0):
                            yearOfPlenty(currentPlayer)
                        else:
                            print("You can't use year of plenty.")
                    elif (toUse == "-m"):
                        if (currentPlayer.devCardDict["Monopoly"] - obtainedDevCards["Monopoly"] - 1 >= 0):
                            monopoly(playerList, currentPlayer)
                        else:
                            print("You can't use monopoly.")
                    elif (toUse == "-r"):
                        if (currentPlayer.devCardDict["Road Building"] - obtainedDevCards["Road Building"] - 1 >= 0):
                            roadBuilding(board, currentPlayer)
                        else:
                            print("You can't use road building.")
                    else:
                        print("\tInvalid command.")
                        usedDevCard = False
            elif (command == "-e"):
                usedDevCard = False
                obtainedDevCards["Knight"] = 0
                obtainedDevCards["Year of Plenty"] = 0
                obtainedDevCards["Monopoly"] = 0
                obtainedDevCards["Road Building"] = 0
                obtainedDevCards["Victory Point"] = 0
                notDone = False
            elif (command == "dev"):
                # DELETE WHEN DONE: ONLY FOR DEVELOPMENT
                currentPlayer.resourceDict["wheat"] = 10
                currentPlayer.resourceDict["ore"] = 10
                currentPlayer.resourceDict["sheep"] = 10
            else:
                print("Invalid command.")


        # Switch the current player
        if (currentPlayerIndex != len(playerList) - 1):
            currentPlayerIndex += 1
        else:
            currentPlayerIndex = 0
