import csv
from setup import *
from board import *
from developmentCardActions import *
from buildFunctions import *
from gameFunctions import *
from tradeFunctions import *
from player import Player
from botFunctions import *

if __name__ == '__main__':

    probabilityDict = {
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

    '''
    total = 0

    woodBrick = 0
    oreWheat = 0

    resourceDictProb = {
        "wheat": 0,
        "sheep": 0,
        "brick": 0,
        "ore": 0,
        "wood": 0,
    }

    with open('ranks.csv', 'wt') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, 300):
            board = createBoard()
            vertexRanks = []
            for i in range(0, 54):
                vertexRanks.append([0, []])
            hexNum = 0
            for hex in board.hexes:
                for vertex in board.hexRelationMatrix[hexNum]:
                    vertexRanks[vertex][0] += abs(7 - hex.number)
                    vertexRanks[vertex][1].append((hex.resourceType, hex.number))
                hexNum += 1
            potentialFirsts = []
            for vertex in vertexRanks:
                if len(vertex[1]) == 1:
                    vertex[0] += 14
                elif len(vertex[1]) == 2:
                    vertex[0] += 7
                if (vertex[0] < 9):
                    potentialFirsts.append(vertex)

            for vertex in potentialFirsts:
                total += 1
                resourceDict = {
                    "wheat": 0,
                    "sheep": 0,
                    "brick": 0,
                    "ore": 0,
                    "wood": 0
                }
                for resource in vertex[1]:
                    resourceDict[resource[0]] += probabilityDict[resource[1]]

                for resource in resourceDict:
                    if (resourceDict[resource] > 0.138):
                        resourceDictProb[resource] += 1
                if (resourceDict["wheat"] > 0 and resourceDict["ore"] > 0):
                    oreWheat += 1
                if (resourceDict["wood"] > 0.08 and resourceDict["brick"] > 0.08):
                    print(vertex)
                    woodBrick += 1
                #print(resourceDict)
                    #filewriter.writerow([resourceDict["wheat"], resourceDict["sheep"], resourceDict["brick"],resourceDict["ore"],resourceDict["wood"],resourceDict["sand"]])

        print("TOTAL: ", total)
        for resource in resourceDictProb:
            print(resource, resourceDictProb[resource] / total)
        print("OREWHEAT", oreWheat / total)
        print("WOODBRICK", woodBrick / total)

    '''


    board = createBoard()
    board.printBoard()
    # vertexRanks contains the rank (low is good) and the resources it gets
    vertexRanks = []
    for i in range(0, 54):
        vertexRanks.append([0, [], i])
    hexNum = 0
    for hex in board.hexes:
        for vertex in board.hexRelationMatrix[hexNum]:
            vertexRanks[vertex][0] += abs(7 - hex.number)
            vertexRanks[vertex][1].append((hex.resourceType, hex.number))
        hexNum += 1
    vertexCount = 0
    for vertex in vertexRanks:
        if len(vertex[1]) == 1:
            vertex[0] += 14
        elif len(vertex[1]) == 2:
            vertex[0] += 7
        '''
        # These vertices don't produce well enough and have no ports;
        if (vertex[0] > 10 and board.vertices[vertexCount].port == None):
            print(vertexCount, vertex[0], "BAD")
        else:
            print(vertexCount, vertex)
        '''
        vertexCount += 1

    #print("\n\n\n\n\n\n\n\n")

    # for the first settlement:
    potentialFirsts = []
    for vertex in vertexRanks:
        if (vertex[0] < 9):
            potentialFirsts.append(vertex)
    #print("\n\n\n\n\n\n\n\n")

    oreWheatVertices = []
    woodBrickVertices = []
    straightNumVertices = []

    for vertex in potentialFirsts:
        #print(vertex)
        resourceDict = {
            "wheat": 0,
            "sheep": 0,
            "brick": 0,
            "ore": 0,
            "wood": 0
        }
        for resource in vertex[1]:
            resourceDict[resource[0]] += probabilityDict[resource[1]]
        if (resourceDict["wheat"] > 0.08 and resourceDict["ore"] > 0.11):
            # This will occur about 10% of the time
            oreWheatVertices.append((vertex, resourceDict["wheat"] + resourceDict["ore"]))
        elif (resourceDict["wood"] > 0.08 and resourceDict["brick"] > 0.08):
            # This will occur about 13% of the time
            woodBrickVertices.append((vertex, resourceDict["wood"] + resourceDict["brick"]))
        elif (vertex[0] <= 7):
            straightNumVertices.append(vertex)
    print("OREWHEAT", oreWheatVertices)
    print("WOODBRICK", woodBrickVertices)
    print("STRAIGHNUM", straightNumVertices)

    # Start selecting a vertex after narrowing down to the three strategies
    print()
    chosenVertex = None

    # Prioritize ore / wheat since it's the least likely
    if (len(oreWheatVertices) != 0):
        print("Picked ore / wheat")
        for vertex in oreWheatVertices:
            if chosenVertex == None:
                chosenVertex = vertex
            elif chosenVertex[1] < vertex[1]:
                chosenVertex = vertex
            elif chosenVertex[1] == vertex[1]:
                if (vertex[0][0] < chosenVertex[0][0]):
                    chosenVertex = vertex
    elif (len(woodBrickVertices) != 0):
        print("Picked wood / brick")
        for vertex in woodBrickVertices:
            if chosenVertex == None:
                chosenVertex = vertex
            elif chosenVertex[1] < vertex[1]:
                chosenVertex = vertex
            elif chosenVertex[1] == vertex[1]:
                if (vertex[0][0] < chosenVertex[0][0]):
                    chosenVertex = vertex
    else:
        print("Picked straight num")
        for vertex in straightNumVertices:
            if chosenVertex == None:
                chosenVertex = vertex
            elif (vertex[0] < chosenVertex[0]):
                chosenVertex = vertex
    print("Chosen: ", chosenVertex)




    '''
    PLACEMENT GUIDE:
        Ore / Wheat:
            Plentiful ore and wheat, ore more so than wheat
            2:1 ore or wheat port nearby, or 3:1
            Opponents leave those open
        Wood / Brick:
            Plentiful wood and brick
            2:1 wood brick port nearby, very important
        If not, go for balance / straight numerical advantage.
        If highly rare resource, go for that
    '''
