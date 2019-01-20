class Vertex:
    '''
    This represents a single vertex on the board. Its number is designated by
    its position in the vertices array. Also, docks will always be on the same
    number vertices, so we don't code them in here.
    '''

    # Default constructor: All vertices start out the same
    def __init__(self):
        self.empty = True
        self.playerName = ''
        self.city = False

class Hex:
    '''
    This represents a single hex on the board. Its number is designated by its
    position in the hexes array.
    '''

    # Pass in the resource type and number upon creation. Robber will always
    # start on the sand hex.
    def __init__(self, resourceType, number):
        self.resourceType = resourceType
        self.number = number
        if (resourceType == "sand"):
            self.robber = True
        else:
            self.robber = False

    # Prints the resource type and the number. This should ONLY be used for
    # debugging purposes.
    def debugPrint(self):
        print(self.resourceType, self.number)

class Board:
    '''
    This is an object of the entire board.
    '''

    # Pass in the list of vertices and hexes.
    def __init__(self, vertices, hexes):
        # List of vertices
        self.vertices = vertices

        # List of hexes
        self.hexes = hexes

        # Roads is a dictionary: Key is a tuple of the vertices, value is name
        self.roads = {
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
                if (vertex, i) in self.roads and self.roads[(vertex, i)] == playerName:
                    return True
                if (i, vertex) in self.roads and self.roads[(i, vertex)] == playerName:
                    return True
            return False

        return True


    def formatHex(self,resource):
        extra_space = 0             # Counts extra space if word has an odd length.
        spaces = 18 - len(str(resource)) # 18 total spaces between lines in hex
        left_space = int(spaces/2)
        right_space = int(spaces/2)
        if spaces%2 == 1:
            extra_space = 1
        return_val = left_space*" " + str(resource) + right_space*" " + extra_space*" "
        return return_val

    def printBoard(self):
        resource_list = []
        number_list = []
        for i in self.hexes:
            temp_str = self.formatHex(i.resourceType)
            resource_list.append(temp_str)              # Resource list contains all formatted strings of resourceTypes.
            temp_str2 = self.formatHex(i.number)
            number_list.append(temp_str2)               # Number list contains all formatted strings of numbers.

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
