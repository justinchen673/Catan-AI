import unittest
from player import *
from bot import *

class Test_bot(unittest.TestCase):

	def setUp(self):
		self.bot1 = Bot("A")
		self.card1 = "Knight"
		self.card2 = "Year of Plenty"
		self.card3 = "Monopoly"
		self.card4 = "Victory Point"
		self.card5 = "Road Building"

	def test_calcProbOfDevCard(self):
		totalProb = self.bot1.calcProbOfDevCard(self.card1)
		print(totalProb)


if __name__ == '__main__':
	unittest.main()