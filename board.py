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

class Board:
    '''
    This is an object of the entire board.
    '''

    # Pass in the list of vertices and hexes.
    def __init__(self, vertices, hexes):
        self.vertices = vertices
        self.hexes = hexes
