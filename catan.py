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



if __name__ == '__main__':
    playerList = initializePlayers()
    board = createBoard()
    board.printBoard()
