from random import shuffle
from player import Player
from board import *

# Creates all the players and returns the list they are all in.
def initializePlayers():
    numPlayers = input("How many people are playing? ")
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



# Creates the board, which is the same structure but has randomly generated
# content within.
def createBoard():
    # A board is comprised of vertices and hexes. First we'll make the vertices.
    vertices = []
    for i in range(0, 54):
        vertices.append(Vertex())

    # Now create the hexes. First, shuffle the terrains.
    terrains = ["wheat", "wheat", "wheat", "wheat", "wood", "wood", "wood", "wood", "sheep", "sheep", "sheep", "sheep", "ore", "ore", "ore", "brick", "brick", "brick", "sand"]
    shuffle(terrains)
    



if __name__ == '__main__':
    playerList = initializePlayers()
    board = createBoard()
