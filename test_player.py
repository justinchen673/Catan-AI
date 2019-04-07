import unittest
from player import *
from board import *
from setup import *

class Test_player(unittest.TestCase):

	def setUp(self):
		print('setUp')
		self.plyr1 = Player("A")
		self.plyr2 = Player("B")
		self.playerList = []
		self.playerList.append(self.plyr1)
		self.playerList.append(self.plyr2)
		

	def tearDown(self):
		print('tearDown\n')

	def test_victorious(self):
		self.plyr1.largestArmy = True
		self.plyr1.longestRoad = True
		self.assertFalse(self.plyr1.test_victorious)

if __name__ == '__main__':
	unittest.main()