"""
gameFunctions.py

This file contains functions that are essentially to regular gameplay, such as
the rolling of the dice, the moving of the robber, distribution of resources,
etc.
"""

import random
from board import *
from player import Player
from botFunctions import *

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
        if(mover.isBot == True):
            newHex = botMoveRobber()
            board.hexes[newHex].robber = True
            notPlaced = False
        else:
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
        if (board.vertices[vertex].empty == False and board.vertices[vertex].playerName != mover.name and getPlayerFromName(playerList, board.vertices[vertex].playerName) not in possibleVictims):
            possibleVictims.append(getPlayerFromName(playerList, board.vertices[vertex].playerName))

    if (len(possibleVictims) == 1):
        victim = possibleVictims[0]
    elif (len(possibleVictims) > 1):
        # Choose someone to steal from and set it to "victim"
        notChosen = True
        while (notChosen):
            print("Player " + mover.name + ", who would you like to steal from? ")
            name = None
            if(mover.isBot == True):
                name = botChooseWhoToRob()
            else:
                name = input()
                if (getPlayerFromName(playerList, name) not in possibleVictims):
                    print("Invalid user.")
                else:
                    for i in range(0, len(possibleVictims)):
                        if possibleVictims[i] == getPlayerFromName(playerList, name):
                            victim = possibleVictims[i]
    if (victim != None):
        # Put their resources in a list and take one at random
        resourceTheftList = []
        for resource in victim.resourceDict:
            for i in range(0, victim.resourceDict[resource]):
                resourceTheftList.append(resource)
        if (len(resourceTheftList) != 0):
            randomIndex = random.randint(0, len(resourceTheftList)-1)
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
