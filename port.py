"""
port.py

This file holds the representation of the Port object, which just holds the
conversion type of the port. resourceType denotes what resource you need to
trade in, and number denotes how many of that resource you need to trade in to
get a resource of your choice.
"""

class Port:
    '''
    This represents a port, which allows for easier trading.
    '''

    def __init__(self, number, resourceType):
        self.number = number
        self.resourceType = resourceType
