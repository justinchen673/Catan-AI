import unittest
from player import *
from board import *
from setup import *

class Test_board(unittest.TestCase):

	def setUp(self):
		print('setUp')
		self.plyr1 = Player("A")
		self.plyr2 = Player("B")
		self.playerList = []
		self.playerList.append(self.plyr1)
		self.playerList.append(self.plyr2)

	def tearDown(self):
		print('tearDown\n')

	def test_dfs(self):
		board1 = createBoard()
		self.plyr1.longestRoadLength = 0
		self.plyr2.longestRoadLength = 0
		self.plyr1.longestRoad = False
		self.plyr2.longestRoad = False

		print('test_dfs_linear')
		board1.placeRoad(2,6,self.plyr1,self.playerList)
		board1.placeRoad(6,10,self.plyr1,self.playerList)
		board1.placeRoad(10,15,self.plyr1,self.playerList)
		board1.placeRoad(15,20,self.plyr1,self.playerList)
		board1.placeRoad(20,26,self.plyr1,self.playerList)
		self.assertTrue(self.plyr1.longestRoad)

		print('playerB overtakes playerA road')
		board1.placeRoad(26,32,self.plyr2,self.playerList)
		board1.placeRoad(32,37,self.plyr2,self.playerList)
		board1.placeRoad(37,42,self.plyr2,self.playerList)
		board1.placeRoad(42,46,self.plyr2,self.playerList)
		board1.placeRoad(46,50,self.plyr2,self.playerList)
		board1.placeRoad(50,53,self.plyr2,self.playerList)
		self.assertTrue(self.plyr2.longestRoad)
		self.assertFalse(self.plyr1.longestRoad)

		board2 = createBoard()
		self.plyr1.longestRoadLength = 0
		self.plyr2.longestRoadLength = 0
		self.plyr1.longestRoad = False
		self.plyr2.longestRoad = False

		print('test_dfs_circular')
		board2.placeRoad(2,6,self.plyr1,self.playerList)
		board2.placeRoad(6,10,self.plyr1,self.playerList)
		board2.placeRoad(10,14,self.plyr1,self.playerList)
		board2.placeRoad(14,9,self.plyr1,self.playerList)
		board2.placeRoad(9,5,self.plyr1,self.playerList)
		board2.placeRoad(5,2,self.plyr1,self.playerList)
		self.assertTrue(self.plyr1.longestRoad)

		print('playerB overtakes playerA road')
		board2.placeRoad(26,32,self.plyr2,self.playerList)
		board2.placeRoad(32,37,self.plyr2,self.playerList)
		board2.placeRoad(37,42,self.plyr2,self.playerList)
		board2.placeRoad(42,46,self.plyr2,self.playerList)
		board2.placeRoad(46,50,self.plyr2,self.playerList)
		board2.placeRoad(50,53,self.plyr2,self.playerList)
		board2.placeRoad(53,49,self.plyr2,self.playerList)
		self.assertTrue(self.plyr2.longestRoad)
		self.assertFalse(self.plyr1.longestRoad)

		board3 = createBoard()
		self.plyr1.longestRoadLength = 0
		self.plyr2.longestRoadLength = 0
		self.plyr1.longestRoad = False
		self.plyr2.longestRoad = False

		print('test_dfs_linear')
		board3.placeRoad(2,6,self.plyr1,self.playerList)
		board3.placeRoad(6,10,self.plyr1,self.playerList)
		board3.placeRoad(10,15,self.plyr1,self.playerList)
		board3.placeRoad(15,20,self.plyr1,self.playerList)
		board3.placeRoad(20,26,self.plyr1,self.playerList)
		self.assertTrue(self.plyr1.longestRoad)

		print('playerB matches playerA road length')
		board3.placeRoad(26,32,self.plyr2,self.playerList)
		board3.placeRoad(32,37,self.plyr2,self.playerList)
		board3.placeRoad(37,42,self.plyr2,self.playerList)
		board3.placeRoad(42,46,self.plyr2,self.playerList)
		board3.placeRoad(46,50,self.plyr2,self.playerList)
		self.assertTrue(self.plyr1.longestRoad)
		self.assertFalse(self.plyr2.longestRoad)

		board4 = createBoard()
		self.plyr1.longestRoadLength = 0
		self.plyr2.longestRoadLength = 0
		self.plyr1.longestRoad = False
		self.plyr2.longestRoad = False

		print('test_dfs_branching')
		board4.placeRoad(9,5,self.plyr1,self.playerList)
		board4.placeRoad(2,5,self.plyr1,self.playerList)
		board4.placeRoad(2,6,self.plyr1,self.playerList)
		board4.placeRoad(6,10,self.plyr1,self.playerList)
		board4.placeRoad(10,15,self.plyr1,self.playerList)
		board4.placeRoad(15,20,self.plyr1,self.playerList)
		board4.placeRoad(20,26,self.plyr1,self.playerList)
		board4.placeRoad(10,14,self.plyr1,self.playerList)
		board4.placeRoad(14,19,self.plyr1,self.playerList)
		board4.placeRoad(19,24,self.plyr1,self.playerList)
		self.assertEqual(self.plyr1.longestRoadLength, 7)
		self.assertTrue(self.plyr1.longestRoad)

		print('playerB matches playerA road length')
		board4.placeRoad(26,32,self.plyr2,self.playerList)
		board4.placeRoad(32,37,self.plyr2,self.playerList)
		board4.placeRoad(37,42,self.plyr2,self.playerList)
		board4.placeRoad(42,46,self.plyr2,self.playerList)
		board4.placeRoad(46,50,self.plyr2,self.playerList)
		board4.placeRoad(50,53,self.plyr2,self.playerList)
		board4.placeRoad(53,49,self.plyr2,self.playerList)
		board4.placeRoad(49,45,self.plyr2,self.playerList)
		self.assertTrue(self.plyr2.longestRoad)
		self.assertFalse(self.plyr1.longestRoad)

		board5 = createBoard()
		self.plyr1.longestRoadLength = 0
		self.plyr2.longestRoadLength = 0
		self.plyr1.longestRoad = False
		self.plyr2.longestRoad = False

		print('test_dfs_circular')
		board5.placeRoad(2,6,self.plyr1,self.playerList)
		board5.placeRoad(6,10,self.plyr1,self.playerList)
		board5.placeRoad(10,14,self.plyr1,self.playerList)
		board5.placeRoad(14,9,self.plyr1,self.playerList)
		board5.placeRoad(9,5,self.plyr1,self.playerList)
		board5.placeRoad(5,2,self.plyr1,self.playerList)
		board5.placeRoad(9,13,self.plyr1,self.playerList)
		board5.placeRoad(10,15,self.plyr1,self.playerList)
		board5.placeRoad(15,20,self.plyr1,self.playerList)
		self.assertTrue(self.plyr1.longestRoad)
		self.assertEqual(self.plyr1.longestRoadLength, 8)
if __name__ == '__main__':
	unittest.main()