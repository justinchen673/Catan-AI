"""
board.py

This file holds the representation of the board as well as any functions it may
need. It is comprised of the Vertex and Hex classes, which together along some
other structures makes up the Board class.
"""

class Vertex:
    '''
    This represents a single vertex on the board. Its number is designated by
    its position in the vertices array. Also, docks will always be on the same
    number vertices, so we don't code them in here.
    '''

    def __init__(self):
        self.empty = True
        self.playerName = ''
        self.city = False


class Hex:
    '''
    This represents a single hex on the board. Its number is designated by its
    position in the hexes array.
    '''

    def __init__(self, resourceType, number):
        self.resourceType = resourceType
        self.number = number
        # Robber always starts on the sand hex.
        if (resourceType == "sand"):
            self.robber = True
        else:
            self.robber = False


    def debugPrint(self):
        '''
        This should ONLY be used for degbugging purposes. This prints a non
        formatted display of the resource type and number on this hex.
        '''

        print(self.resourceType, self.number)


class Board:
    '''
    This is an object of the entire board.
    '''

    def __init__(self, vertices, hexes):
        # List of vertices
        self.vertices = vertices

        # List of hexes
        self.hexes = hexes

        # Roads is a dictionary: Key is a tuple of the vertices, value is name
        self.roads = {
            (0, 3): "//",
            (0, 4): "\\\\",
            (1, 4): "//",
            (1, 5): "\\\\",
            (2, 5): "//",
            (2, 6): "\\\\",
            (3, 7): "||",
            (4, 8): "||",
            (5, 9): "||",
            (6, 10): "||",
            (7, 11): "//",
            (7, 12): "\\\\",
            (8, 12): "//",
            (8, 13): "\\\\",
            (9, 13): "//",
            (9, 14): "\\\\",
            (10, 14): "//",
            (10, 15): "\\\\",
            (11, 16): "||",
            (12, 17): "||",
            (13, 18): "||",
            (14, 19): "||",
            (15, 20): "||",
            (16, 21): "//",
            (16, 22): "\\\\",
            (17, 22): "//",
            (17, 23): "\\\\",
            (18, 23): "//",
            (18, 24): "\\\\",
            (19, 24): "//",
            (19, 25): "\\\\",
            (20, 25): "//",
            (20, 26): "\\\\",
            (21, 27): "||",
            (22, 28): "||",
            (23, 29): "||",
            (24, 30): "||",
            (25, 31): "||",
            (26, 32): "||",
            (27, 33): "\\\\",
            (28, 33): "//",
            (28, 34): "\\\\",
            (29, 34): "//",
            (29, 35): "\\\\",
            (30, 35): "//",
            (30, 36): "\\\\",
            (31, 36): "//",
            (31, 37): "\\\\",
            (32, 37): "//",
            (33, 38): "||",
            (34, 39): "||",
            (35, 40): "||",
            (36, 41): "||",
            (37, 42): "||",
            (38, 43): "\\\\",
            (39, 43): "//",
            (39, 44): "\\\\",
            (40, 44): "//",
            (40, 45): "\\\\",
            (41, 45): "//",
            (41, 46): "\\\\",
            (42, 46): "//",
            (43, 47): "||",
            (44, 48): "||",
            (45, 49): "||",
            (46, 50): "||",
            (47, 51): "\\\\",
            (48, 51): "//",
            (48, 52): "\\\\",
            (49, 52): "//",
            (49, 53): "\\\\",
            (50, 53): "//"
        }

        # A matrix that tells what vertices each hex is linked to
        self.hexRelationMatrix = [
            [0, 3, 4, 7, 8, 12],
            [1, 4, 5, 8, 9, 13],
            [2, 5, 6, 9, 10, 14],
            [7, 11, 12, 16, 17, 22],
            [8, 12, 13, 17, 18, 23],
            [9, 13, 14, 18, 19, 24],
            [10, 14, 15, 19, 20, 25],
            [16, 21, 22, 27, 28, 33],
            [17, 22, 23, 28, 29, 34],
            [18, 23, 24, 29, 30, 35],
            [19, 24, 25, 30, 31, 36],
            [20, 25, 26, 31, 32, 37],
            [28, 33, 34, 38, 39, 43],
            [29, 34, 35, 39, 40, 44],
            [30, 35, 36, 40, 41, 45],
            [31, 36, 37, 41, 42, 46],
            [39, 43, 44, 47, 48, 51],
            [40, 44, 45, 48, 49, 52],
            [41, 45, 46, 49, 50, 53]
        ]

        # A matrix that tells what vertices each vertex is linked to
        self.vertexRelationMatrix = [
            [3, 4],
            [4, 5],
            [5, 6],
            [0, 7],
            [0, 1, 8],
            [1, 2, 9],
            [2, 10],
            [3, 11, 12],
            [4, 12, 13],
            [5, 13, 14],
            [6, 14, 15],
            [7, 16],
            [7, 8, 17],
            [8, 9, 18],
            [9, 10, 19],
            [10, 20],
            [11, 21, 22],
            [12, 22, 23],
            [13, 23, 24],
            [14, 24, 25],
            [15, 25, 26],
            [16, 27],
            [16, 17, 28],
            [17, 18, 29],
            [18, 19, 30],
            [19, 20, 31],
            [20, 32],
            [21, 33],
            [22, 33, 34],
            [23, 34, 35],
            [24, 35, 36],
            [25, 36, 37],
            [26, 37],
            [27, 28, 38],
            [28, 29, 39],
            [29, 30, 40],
            [30, 31, 41],
            [31, 32, 42],
            [33, 43],
            [34, 43, 44],
            [35, 44, 45],
            [36, 45, 46],
            [37, 46],
            [38, 39, 47],
            [39, 40, 48],
            [40, 41, 49],
            [41, 42, 50],
            [43, 51],
            [44, 51, 52],
            [45, 52, 53],
            [46, 55],
            [47, 48],
            [48, 49],
            [49, 50]
        ]


    def canPlaceSettlement(self, vertex, playerName, firstPlacement):
        '''
        Determines if a settlement can be placed at the vertex given the user.
        The boolean value firstPlacement determines whether this is the first
        placement, meaning that the game is in the setup phase.
        '''

        # Out of bounds vertex
        if (vertex < 0 or vertex > 53):
            return False

        # Something already there
        if not self.vertices[vertex].empty:
            return False

        # Something at an adjacent vertex
        for i in self.vertexRelationMatrix[vertex]:
            if not self.vertices[i].empty:
                return False

        # Checks if it's connected to a road if it isn't the first placement
        if not firstPlacement:
            for i in self.vertexRelationMatrix[vertex]:
                if (i > vertex):
                    if self.roads[(vertex, i)] == playerName + playerName:
                        return True
                else:
                    if self.roads[(i, vertex)] == playerName + playerName:
                        return True
            return False

        return True


    def placeSettlement(self, vertex, playerName):
        '''
        Adds a settlement to the board given the vertex and the player's name
        '''

        self.vertices[vertex].empty = False
        self.vertices[vertex].playerName = playerName


    def canPlaceRoad(self, vertex1, vertex2, playerName):
        '''
        Determines if a road can be placed between the two vertices given the
        user.
        '''

        # Checks if the vertices are next to each other
        if not vertex2 in self.vertexRelationMatrix[vertex1]:
            return False

        # Checks if there is already a road there
        if (vertex1 < vertex2):
            if self.roads[(vertex1, vertex2)] == "AA" or self.roads[(vertex1, vertex2)] == "BB" or self.roads[(vertex1, vertex2)] == "CC" or self.roads[(vertex1, vertex2)] == "DD":
                return False

        # Checks if there is a settlement of the same playerName at either
        # vertex
        if (not self.vertices[vertex1].empty) and (self.vertices[vertex1].playerName == playerName):
            return True
        if (not self.vertices[vertex2].empty) and (self.vertices[vertex2].playerName == playerName):
            return True

        # Checks if this connects a road already placed
        for i in self.vertexRelationMatrix[vertex1]:
            if (vertex1 < i):
                if self.roads[(vertex1, i)] == playerName + playerName:
                    return True
            else:
                if self.roads[(i, vertex1)] == playerName + playerName:
                    return True
        for i in self.vertexRelationMatrix[vertex2]:
            if (vertex2 < i):
                if self.roads[(vertex2, i)] == playerName + playerName:
                    return True
            else:
                if self.roads[(i, vertex2)] == playerName + playerName:
                    return True

        return False


    def placeRoad(self, vertex1, vertex2, playerName):
        '''
        Adds a road to the board given the 2 vertices it is between and the
        player's name
        '''

        if (vertex1 < vertex2):
            self.roads[(vertex1, vertex2)] = playerName + playerName
        else:
            self.roads[(vertex2, vertex1)] = playerName + playerName


    def formatHex(self,resource):
        '''
        Helper function for formatting when printing.
        '''

        # Counts extra space if word has an odd length.
        extra_space = 0
        # 18 total spaces between lines in hex
        spaces = 18 - len(str(resource))
        left_space = int(spaces/2)
        right_space = int(spaces/2)
        if spaces%2 == 1:
            extra_space = 1
        return_val = left_space*" " + str(resource) + right_space*" " + extra_space*" "
        return return_val


    def printBoard(self):
        '''
        Prints the board
        '''

        # Resource list contains all formatted strings of resourceTypes.
        resource_list = []
        # Number list contains all formatted strings of numbers.
        number_list = []
        for i in self.hexes:
            temp_str = self.formatHex(i.resourceType)
            resource_list.append(temp_str)
            temp_str2 = self.formatHex(i.number)
            number_list.append(temp_str2)

        print("                              00                  01                  02")
        print("                            //  \\\\              //  \\\\              //  \\\\")
        print("                          //      \\\\          //      \\\\          //      \\\\")
        print("                        //          \\\\      //          \\\\      //          \\\\")
        print("                      //              \\\\  //              \\\\  //              \\\\ ")
        print("                    03                  04                  05                  06")
        print("                    ||" +resource_list[0]+ "||" +resource_list[1]+ "||" +resource_list[2]+ "||")
        print("                    ||" +number_list[0]+ "||" +number_list[1]+ "||" +number_list[2]+ "||")
        print("                    ||                  ||                  ||                  ||")
        print("                    07                  08                  09                  10")
        print("                  //  \\\\              //  \\\\              //  \\\\              //  \\\\  ")
        print("                //      \\\\          //      \\\\          //      \\\\          //      \\\\  ")
        print("              //          \\\\      //          \\\\      //          \\\\      //          \\\\ ")
        print("            //              \\\\  //              \\\\  //              \\\\  //              \\\\ ")
        print("          11                  12                  13                  14                  15")
        print("          ||"+resource_list[3]+"||"+resource_list[4]+"||"+resource_list[5]+"||"+resource_list[6]+"||")
        print("          ||" +number_list[3]+ "||" +number_list[4]+ "||" +number_list[5]+ "||"+number_list[6]+"||")
        print("          ||                  ||                  ||                  ||                  ||")
        print("          16                  17                  18                  19                  20")
        print("        //  \\\\               //  \\\\             //  \\\\              //  \\\\              //  \\\\")
        print("      //      \\\\           //      \\\\         //      \\\\          //      \\\\          //      \\\\")
        print("    //          \\\\      //          \\\\      //          \\\\      //          \\\\      //          \\\\")
        print("  //              \\\\  //              \\\\  //              \\\\  //              \\\\  //              \\\\")
        print("21                  22                  23                  24                  25                  26")
        print("||"+resource_list[7]+"||"+resource_list[8]+"||"+resource_list[9]+"||"+resource_list[10]+"||"+resource_list[11]+"||")
        print("||" +number_list[7]+ "||" +number_list[8]+ "||" +number_list[9]+ "||" +number_list[10]+ "||" +number_list[11]+ "||")
        print("||                  ||                  ||                  ||                  ||                  ||")
        print("27                  28                  29                  30                  31                  32")
        print("  \\\\              //  \\\\              //  \\\\              //  \\\\              //  \\\\              //")
        print("    \\\\          //      \\\\          //      \\\\          //      \\\\          //      \\\\          //")
        print("      \\\\      //          \\\\      //          \\\\      //          \\\\      //          \\\\      //")
        print("        \\\\  //              \\\\  //              \\\\  //              \\\\  //              \\\\  //")
        print("          33                  34                  35                  36                  37")
        print("          ||"+resource_list[12]+"||"+resource_list[13]+"||"+resource_list[14]+"||"+resource_list[15]+"||")
        print("          ||" +number_list[12]+ "||" +number_list[13]+ "||" +number_list[14]+ "||"+number_list[15]+"||")
        print("          ||                  ||                  ||                  ||                  ||")
        print("          38                  39                  40                  41                  42")
        print("            \\\\               //  \\\\             //  \\\\              //  \\\\              //")
        print("              \\\\           //      \\\\         //      \\\\          //      \\\\          //")
        print("                \\\\      //          \\\\      //          \\\\      //          \\\\      //")
        print("                  \\\\  //              \\\\  //              \\\\  //              \\\\  //")
        print("                    43                  44                  45                  46")
        print("                    ||" +resource_list[16]+ "||" +resource_list[17]+ "||" +resource_list[18]+ "||")
        print("                    ||" +number_list[16]+ "||" +number_list[17]+ "||" +number_list[18]+ "||")
        print("                    ||                  ||                  ||                  ||")
        print("                    47                  48                  49                  50")
        print("                      \\\\              //  \\\\              //  \\\\              //")
        print("                        \\\\          //      \\\\          //      \\\\          //")
        print("                          \\\\      //          \\\\      //          \\\\      //")
        print("                            \\\\  //              \\\\  //              \\\\  //")
        print("                              51                  52                  53")
