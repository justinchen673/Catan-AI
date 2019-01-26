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
from board import *

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
    playerList = []
    playerList.append(Player("A"))
    playerList.append(Player("B"))
    if (numPlayers >= 3):
        playerList.append(Player("C"))
    if (numPlayers >= 4):
        playerList.append(Player("D"))

    return playerList


def createBoard():
    '''
    Creates the board, which is the same structure but has randomly generated
    content within.
    '''

    # A board is comprised of vertices and hexes. First we'll make the vertices.
    vertices = []
    for i in range(0, 54):
        vertices.append(Vertex())

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
    # TODO: Make the first hex not necessarily start at the upper left corner
    hexes = []
    hexes.append(hexesOrdered[0])
    hexes.append(hexesOrdered[1])
    hexes.append(hexesOrdered[2])
    hexes.append(hexesOrdered[11])
    hexes.append(hexesOrdered[12])
    hexes.append(hexesOrdered[13])
    hexes.append(hexesOrdered[3])
    hexes.append(hexesOrdered[10])
    hexes.append(hexesOrdered[17])
    hexes.append(hexesOrdered[18])
    hexes.append(hexesOrdered[14])
    hexes.append(hexesOrdered[4])
    hexes.append(hexesOrdered[9])
    hexes.append(hexesOrdered[16])
    hexes.append(hexesOrdered[15])
    hexes.append(hexesOrdered[5])
    hexes.append(hexesOrdered[8])
    hexes.append(hexesOrdered[7])
    hexes.append(hexesOrdered[6])

    return Board(vertices, hexes)


def placeFirstSettlements(board, playerList):
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
            toPlace = int(input("Player " + i.name + ", select the vertex where you want to place your first settlement: "))
            if (board.canPlaceSettlement(toPlace, i.name, True)):
                # Legal placement
                board.placeSettlement(toPlace, i.name)
                firstVertex = toPlace
                notPlaced = False
            else:
                # Non legal placement
                print("Please enter a valid vertex.")

        board.printBoard()

        # Get road
        notPlaced = True
        while(notPlaced):
            toPlace = int(input("Your road will start at vertex " + str(firstVertex) + ". Which vertex do you want it to link to? "))
            if (board.canPlaceRoad(firstVertex, toPlace, i.name)):
                # Legal placement
                board.placeRoad(firstVertex, toPlace, i.name)
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
            toPlace = int(input("Player " + playerList[i].name + ", select the vertex where you want to place your second settlement: "))
            if (board.canPlaceSettlement(toPlace, playerList[i].name, True)):
                # Legal placement
                board.placeSettlement(toPlace, playerList[i].name)
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
            toPlace = int(input("Your road will start at vertex " + str(firstVertex) + ". Which vertex do you want it to link to? "))
            if (board.canPlaceRoad(firstVertex, toPlace, playerList[i].name)):
                # Legal placement
                board.placeRoad(firstVertex, toPlace, playerList[i].name)
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
