"""
buildFunctions.py

This file supports all of the 'building' functions, the options being cities,
settlements, roads, and development cards. Each function either gives the player
the requested item and takes away their resources, or stops the action if the
player doesn't have the necessary resources.
"""

from board import *
from player import Player

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


def buildRoad(board, player, playerList):
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
        board.placeRoad(vertex1, vertex2, player, playerList)
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
