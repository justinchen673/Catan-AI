"""
catan.py

This file mostly just holds the main function, which enters the game loop. This
is the file that you will run when starting the game.
"""

from setup import *
from board import *
from developmentCardActions import *
from buildFunctions import *
from gameFunctions import *
from tradeFunctions import *
from player import Player

def printHelp():
    '''
    Outputs a list of commands that a user can call during their turn.
    '''

    print("\t-t is for trading, either with a player or with the bank.")
    print("\t-b is for building.")
    print("\t-d is for using a development card.")
    print("\t-e is for ending your turn.")


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
                            useKnight(board, currentPlayer, playerList)
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
