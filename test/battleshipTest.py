'''
Created on Jan 21, 2010

@author: victorhg
'''
import unittest
from battleship.game.model import Board, Position

class Test(unittest.TestCase):


    def setUp(self):
        numRows = 10
        numColumns= 10
        self.board = Board(numRows, numColumns)

    def testAttackingEmptyBoardResultsInNonAcert(self):
        self.assertFalse(self.board.hitAtPosition(Position(0,0)))
        
    def testAttackingPositionWithShipResultInAcert(self):
        self.board.setBoatPosition(Position(1,1))
        self.assertTrue(self.board.hitAtPosition(Position(1,1)))

    def testAttackingMultiplePositionSetted(self):
        self.board.setBoatPosition(Position(1,1))
        self.board.setBoatPosition(Position(2,1))
        self.board.setBoatPosition(Position(3,1))
        self.assertTrue(self.board.hitAtPosition(Position(1,1)))
        self.assertTrue(self.board.hitAtPosition(Position(2,1)))
        self.assertTrue(self.board.hitAtPosition(Position(3,1)))

    def testBoardShouldBeAbleToKnowWhenGameIsOver(self):
        self.board.setBoatPosition(Position(1,1))
        self.assertTrue(self.board.hastBoatsAlive())
        self.assertTrue(self.board.hitAtPosition(Position(1,1)))
        self.assertFalse(self.board.hastBoatsAlive())
        
    def testBoardShouldStartWithNoAlivePosition(self):
        self.assertFalse(self.board.hastBoatsAlive())
    
    def testHitBlankSpotsShouldNotKillBoats(self):
        self.board.setBoatPosition(Position(1,1))
        self.assertTrue(self.board.hastBoatsAlive())
        self.assertFalse(self.board.hitAtPosition(Position(2,2)))
        self.assertTrue(self.board.hastBoatsAlive())
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()