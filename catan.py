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


if __name__ == '__main__':
    playerList = initializePlayers()
    board = createBoard()
    board.printBoard()

    # Setup Phase
    placeFirstSettlements(board, playerList)

    # Game Phase
    currentPlayer = 0
    while(not playerList[currentPlayer].victorious()):
        board.printBoard()

        # Roll the dice and resolve consequences of the dice roll
        roll = diceRoll()
        print()
        print("A " + str(roll) + " was rolled.")
        if (roll == 7):
            # Player moves robber
            moveRobber(board, playerList[currentPlayer])
        else:
            handOutResources(board, playerList, roll)

        # Begin the action phase for the current player
        

        # Switch the current player
        if (currentPlayer != len(playerList) - 1):
            currentPlayer += 1
        else:
            currentPlayer = 0

        # For debugging
        x = input("Press key to continue...")
