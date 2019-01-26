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
        newHex = int(input("Player " + mover.name + ", which hex would you like to move the robber to? Select a number 0 - 18, starting from the top left hex and moving right. "))
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


if __name__ == '__main__':
    playerList = initializePlayers()
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
                    bankTrade(currentPlayer)
            elif (command == "-e"):
                notDone = False
            else:
                print("Invalid command.")


        # Switch the current player
        if (currentPlayerIndex != len(playerList) - 1):
            currentPlayerIndex += 1
        else:
            currentPlayerIndex = 0
