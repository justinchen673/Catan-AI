import random
from setup import *
from player import Player
from board import *

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


def moveRobber(board, mover):
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
    board.printBoard()


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


def bankTrade(player):
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
        board.placeSettlement(vertex, player.name)
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
    Gives the player a development card off of the deck.
    '''

    # Checks if the player has the resources needed to build a road
    if (player.resourceDict["ore"] < 1 or player.resourceDict["sheep"] < 1 or player.resourceDict["wheat"] < 1):
        print("\tYou don't have the necessary resources to get a development card.")
        return

    # Ensures there are still development cards
    if (len(devCardDeck) == 0):
        print("\tNo more development cards remain.")
        return

    player.devCardDict[devCardDeck.pop()] += 1
    player.resourceDict["ore"] -= 1
    player.resourceDict["sheep"] -= 1
    player.resourceDict["wheat"] -= 1
    print(devCardDeck)



if __name__ == '__main__':
    playerList = initializePlayers()
    devCardDeck = initializeDevCards()
    print(len(devCardDeck))
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
            moveRobber(board, currentPlayer)
        else:
            handOutResources(board, playerList, roll)

        # Begin the action phase for the current player
        print("Player " + currentPlayer.name + ":")
        currentPlayer.printHand()
        # Allow commands
        notDone = True
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
                    bankTrade(currentPlayer)
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
                    buildDevCard(currentPlayer, devCardDeck)
                else:
                    print("\tInvalid command.")
            elif (command == "-e"):
                notDone = False
            else:
                print("Invalid command.")


        # Switch the current player
        if (currentPlayerIndex != len(playerList) - 1):
            currentPlayerIndex += 1
        else:
            currentPlayerIndex = 0
