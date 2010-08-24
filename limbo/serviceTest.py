'''
Created on Jan 21, 2010

@author: victorhg
'''
import unittest
from battleship.game.network.service import RemoteGame
from battleship.game.model import Board, Position


class RemoteGameTest(unittest.TestCase):
    
    def testGameServiceHittingBlankSpots(self):
        self.startGame().withPositionOcupied(self.inPosition(1, 1)).hitTarget(self.inPosition(0,0)).expectBoatsAlive(True)
    
    def testGameServiceTargetHitted(self):
        self.startGame().withPositionOcupied(self.inPosition(1, 1)).hitTarget(self.inPosition(1, 1)).expectBoatsAlive(False)
    
    def startGame(self):
        self.service = RemoteGame(Board(2, 2))
        return self
    
    def withPositionOcupied(self, position):
        self.board = Board(2, 2)
        self.board.setBoatPosition(position)
        self.service = RemoteGame(self.board)
        return self
    
    def hitTarget(self, position):
        self.service.hitTarget(position)
        return self
    
    def inPosition(self, row, column):
        return Position(row, column)

    def expectBoatsAlive(self, expectedBoatsAlive):
        self.assertEquals(expectedBoatsAlive, self.service.hasBoatsAlive())
        return self



        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()