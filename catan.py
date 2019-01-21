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
        roll = diceRoll()
        handOutResources(board, playerList, roll)
        print()
        print(roll)
        for i in playerList:
            print(i.name)
            print(i.resourceDict)
        x = input("Press key to continue...")
