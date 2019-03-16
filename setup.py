"""
setup.py
This file holds several functions that are used in the setup phase of the Catan
game. The setup phase consists of:
    (1) Finding out how many people are playing
    (2) Getting each player to place their first and second settlements before
        the first dice roll occurs.
"""

import random
from random import shuffle
from player import Player
from bot import Bot
from board import *
from botFunctions import *

def initializePlayers():
    '''
    Creates all the players and returns the list they are all in.
    '''

    players = input("How many people are playing? ")
    if(not players.isdigit()):
        print("Please enter a valid number.")
        exit()
    numPlayers = int(players)
    if (numPlayers > 4 or numPlayers < 2):
        print("There can only be 2-4 players.")
        exit()


    bots = input("How many bots are playing? ")
    if (not bots.isdigit()):
        print("Please enter a valid number.")
        exit()
    numBots = int(bots)
    if(numBots > numPlayers):
        print("Number of bots must be less than or equal to number of players.")
        exit()

    playerNames = ["A", "B", "C", "D"]
    playerList = []
    '''
    playerList.append(Player("A"))
    playerList.append(Player("B"))
    if (numPlayers >= 3):
        playerList.append(Player("C"))
    if (numPlayers >= 4):
        playerList.append(Player("D"))
    for position in range(0, numBots):
        playerList[position].isBot = True
    '''

    for i in range(0, numPlayers):
        if (i < numBots):
            playerList.append(Bot(playerNames[i]))
            print("bot made")
        else:
            playerList.append(Player(playerNames[i]))
            print("player made")


    return playerList


def initializeDevCards():
    '''
    Creates the deck of the development cards. There starts out with 25
    development cards, and cards will never re-enter the deck.
    '''

    devCards = ["Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Year of Plenty", "Year of Plenty", "Monopoly", "Monopoly", "Road Building", "Road Building", "Victory Point", "Victory Point", "Victory Point", "Victory Point", "Victory Point"]
    shuffle(devCards)
    return devCards


def createBoard():
    '''
    Creates the board, which is the same structure but has randomly generated
    content within.
    '''

    # A board is comprised of vertices and hexes. First we'll make the vertices.
    vertices = []
    for i in range(0, 54):
        vertices.append(Vertex())

    # Add the ports in the appropriate locations
    vertices[1].port = Port(2, "wood")
    vertices[4].port = Port(2, "wood")
    vertices[2].port = Port(3, "none")
    vertices[6].port = Port(3, "none")
    vertices[7].port = Port(2, "brick")
    vertices[11].port = Port(2, "brick")
    vertices[15].port = Port(2, "wheat")
    vertices[20].port = Port(2, "wheat")
    vertices[21].port = Port(3, "none")
    vertices[27].port = Port(3, "none")
    vertices[37].port = Port(2, "ore")
    vertices[42].port = Port(2, "ore")
    vertices[38].port = Port(3, "none")
    vertices[43].port = Port(3, "none")
    vertices[48].port = Port(2, "sheep")
    vertices[52].port = Port(2, "sheep")
    vertices[50].port = Port(3, "none")
    vertices[53].port = Port(3, "none")

    # Now create the hexes. First, shuffle the terrains.
    terrains = ["wheat", "wheat", "wheat", "wheat", "wood", "wood", "wood", "wood", "sheep", "sheep", "sheep", "sheep", "ore", "ore", "ore", "brick", "brick", "brick", "sand"]
    shuffle(terrains)

    # These will be the numbers associated with the hexes. These will always be
    # the same initial order.
    numbers = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

    # Assign each terrain a number. The desert will be 0.
    hexesOrdered = []
    sandAssigned = False
    for i in range(0, 19):
        if (terrains[i] == "sand"):
            sandAssigned = True
            hexesOrdered.append(Hex(terrains[i], 0))
        else:
            if (sandAssigned):
                hexesOrdered.append(Hex(terrains[i], numbers[i-1]))
            else:
                hexesOrdered.append(Hex(terrains[i], numbers[i]))

    # The catan numbers spiral around the board, so we'll have to hardcode that
    # spiral format into it.

    # List of possible curl orders
    hexCurlMatrix = [
        [0, 1, 2, 11, 12, 13, 3, 10, 17, 18, 14, 4, 9, 16, 15, 5, 8, 7, 6],
        [11, 0, 1, 10, 12, 13, 2, 9, 17, 18, 14, 3, 8, 16, 15, 4, 7, 6, 5],
        [10, 11, 0, 9, 17, 12, 1, 8, 16, 18, 13, 2, 7, 15, 14, 3, 6, 5, 4],
        [9, 10, 11, 8, 17, 12, 0, 7, 16, 18, 13, 1, 6, 15, 14, 2, 5, 4, 3],
        [8, 9, 10, 7, 16, 17, 11, 6, 15, 18, 12, 0, 5, 14, 13, 1, 4, 3, 2],
        [7, 8, 9, 6, 16, 17, 10, 5, 15, 18, 12, 11, 4, 14, 13, 0, 3, 2, 1],
        [6, 7, 8, 5, 15, 16, 9, 4, 14, 18, 17, 10, 3, 13, 12, 11, 2, 1, 0],
        [5, 6, 7, 4, 15, 16, 8, 3, 14, 18, 17, 9, 2, 13, 12, 10, 1, 0, 11],
        [4, 5, 6, 3, 14, 15, 7, 2, 13, 18, 16, 8, 1, 12, 17, 9, 0, 11, 10],
        [3, 4, 5, 2, 14, 15, 6, 1, 13, 18, 16, 7, 0, 12, 17, 8, 11, 10, 9],
        [2, 3, 4, 1, 13, 14, 5, 0, 12, 18, 15, 6, 11, 17, 16, 7, 10, 9, 8],
        [1, 2, 3, 0, 13, 14, 4, 11, 12, 18, 15, 5, 10, 17, 16, 6, 9, 8, 7]
    ]

    # Choose a random curl and format the board with it
    curlIndex = random.randint(0, 11)
    hexes = []
    for i in hexCurlMatrix[curlIndex]:
        hexes.append(hexesOrdered[i])

    return Board(vertices, hexes)


def placeFirstSettlements(board, playerList):
    '''
    This function is called when the players place the first settlements of the
    game, in which they place 2. The player who puts down the first settlement
    will also be the last, for fairness reasons.
    '''

    # Determine who goes first: rotation will still be A, B, C, D though
    startIndex = random.randint(0, 3)
    for i in range(0, startIndex):
        playerList.append(playerList[0])
        playerList.pop(0)

    for i in playerList:

        board.printBoard()

        # Get settlement
        firstVertex = 0
        notPlaced = True
        while(notPlaced):
            print("Player " + i.name + ", select the vertex where you want to place your first settlement: ")
            toPlace = None
            if (i.isBot == True):
                toPlace = botPlaceFirstSettlement()
                board.placeSettlement(toPlace, i)
                firstVertex = toPlace
                notPlaced = False
            else:
                toPlace = int(input())
                if (board.canPlaceSettlement(toPlace, i.name, True)):
                    # Legal placement
                    board.placeSettlement(toPlace, i)
                    firstVertex = toPlace
                    notPlaced = False
                else:
                    # Non legal placement
                    print("Please enter a valid vertex.")

        board.printBoard()

        # Get road
        notPlaced = True
        while(notPlaced):
            print("Your road will start at vertex " + str(firstVertex) + ". Which vertex do you want it to link to? ")
            toPlace = None
            if(i.isBot ==True):
                toPlace = botBuildFirstRoad()
                board.placeRoad(firstVertex, toPlace, i.name)
                notPlaced = False
            else:
                toPlace = int(input())
                if (board.canPlaceRoad(firstVertex, toPlace, i.name)):
                    # Legal placement
                    board.placeRoad(firstVertex, toPlace, i, playerList)
                    notPlaced = False
                else:
                    # Non legal placement
                    print("Please enter a valid vertex.")


    # To find out what initial resouces to the players should receive
    secondSettlements = []

    for i in range(len(playerList)-1, -1, -1):

        board.printBoard()

        # Get settlement
        firstVertex = 0
        notPlaced = True
        while(notPlaced):
            print("Player " + playerList[i].name + ", select the vertex where you want to place your second settlement: ")
            toPlace = None
            if(playerList[i].isBot == True):
                toPlace = botPlaceSecondSettlement()
                board.placeSettlement(toPlace, playerList[i])
                firstVertex = toPlace
                notPlaced = False
                secondSettlements.append((playerList[i], toPlace))
            else:
                toPlace = int(input())
                if (board.canPlaceSettlement(toPlace, playerList[i].name, True)):
                    # Legal placement
                    board.placeSettlement(toPlace, playerList[i])
                    firstVertex = toPlace
                    notPlaced = False
                    secondSettlements.append((playerList[i], toPlace))
                else:
                    # Non legal placement
                    print("Please enter a valid vertex.")

        board.printBoard()

        # Get road
        notPlaced = True
        while(notPlaced):
            print("Your road will start at vertex " + str(firstVertex) + ". Which vertex do you want it to link to? ")
            
            toPlace = None
            if(playerList[i].isBot == True):
                toPlace = botBuildSecondRoad()
                board.placeRoad(firstVertex, toPlace, playerList[i], playerList)
                notPlaced = False

            toPlace = int(input())
            if (board.canPlaceRoad(firstVertex, toPlace, playerList[i].name)):
                # Legal placement
                board.placeRoad(firstVertex, toPlace, playerList[i], playerList)
                notPlaced = False
            else:
                # Non legal placement
                print("Please enter a valid vertex.")


    # Hand out first resource
    for i in range(0, 19):
        # j represents the vertexs that is next to the hex i
        for j in board.hexRelationMatrix[i]:
            # k represents the tuple of (player, vertex)
            for k in secondSettlements:
                if j == k[1]:
                    # Hand out that resource
                    if (board.hexes[i].resourceType != "sand"):
                        k[0].resourceDict[board.hexes[i].resourceType] += 1