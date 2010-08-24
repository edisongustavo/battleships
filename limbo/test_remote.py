'''
Created on Jan 25, 2010

@author: victorhg
'''
from twisted.spread  import pb
from twisted.internet import reactor
from battleship.game.network.service import RemoteGame
from battleship.game.model import Board, Position
from twisted.trial import unittest as trialunit

class RemoteGameTest(trialunit.TestCase):
    def setUp(self):
        self.board = Board(2, 2)
        self.server = reactor.listenTCP(0, pb.PBServerFactory(RemoteGame(self.board)))
        clientFactory = pb.PBClientFactory()
        reactor.connectTCP("localhost", self.server.getHost().port,clientFactory)
        def gotRoot(ref):
            self.ref = ref
        return clientFactory.getRootObject().addCallback(gotRoot)

    def tearDown(self):
        self.ref.broker.transport.loseConnection()
        return self.server.stopListening()

    def test_BoardHasNoAliveBoats(self):
        d = self.ref.callRemote("hasBoatsAlive")
        def callback(res):
            self.failUnless(res is False)
        d.addCallback(callback)
        return d
    
    def test_RemoteHitShouldAffectBoard(self):
        self.board.setBoatPosition(Position(1,1))
        d = self.ref.callRemote("hasBoatsAlive")
        d.addCallback(lambda hasBoats: self.failUnless(hasBoats is True))
        
        d = self.ref.callRemote("hitTarget", 1, 1)
        d.addCallback(lambda hitted: self.failUnless(hitted is True, "Hit failed"))
        
        d = self.ref.callRemote("hasBoatsAlive")
        d.addCallback(lambda hasBoats: self.failUnless(hasBoats is False, "Couldn' hit target remotely"))
        return d
