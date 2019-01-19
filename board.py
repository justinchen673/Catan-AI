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
        self.vertices = vertices
        self.hexes = hexes

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
