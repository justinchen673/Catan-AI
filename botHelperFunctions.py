################################################################################
# FOR PLACING SETTLEMENTS
################################################################################

def getRollProbabilities():
    return {
        0: 0,
        2: .02778,
        3: .05556,
        4: .08336,
        5: .11111,
        6: .13889,
        7: .16667,
        8: .13889,
        9: .11111,
        10: .08336,
        11: .05556,
        12: .02778
    }

def obtainVertexRanks(board):
    vertexRanks = []
    for i in range(0, 54):
        vertexRanks.append([0, [], i])
    hexNum = 0
    for hex in board.hexes:
        for vertex in board.hexRelationMatrix[hexNum]:
            vertexRanks[vertex][0] += abs(7 - hex.number)
            vertexRanks[vertex][1].append((hex.resourceType, hex.number))
        hexNum += 1
    return vertexRanks
