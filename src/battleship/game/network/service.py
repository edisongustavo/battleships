import threading
from twisted.spread import pb
from twisted.internet import reactor
from zope.interface import Interface, implements
from battleship.game.model import Position, Board
from twisted.python import util

class GameService(Interface):
    def hitTarget(position):
        """Hits Target"""
    def hasBoatsAlive():
        """Returns wheather there are still boats lefting"""
 

class RemoteGame(pb.Root, pb.Referenceable):
    
    implements(GameService)
    def __init__(self, board):
        self.board = board
    
    def hitTarget(self, position):
        return self.board.hitAtPosition(position)
    
    def hasBoatsAlive(self):
        return self.board.hastBoatsAlive()
    
    # Remote Methods to be accessed during game
    def remote_hitTarget(self, row, column):
        print "hit target called"
        return self.hitTarget(Position(row, column))
    
    def remote_hasBoatsAlive(self): 
        print "has boats called"
        return self.hasBoatsAlive()
    

    
class GameServer(threading.Thread):      
    def run(self):
        board = Board(10, 10)
        board.setBoatPosition(Position(1,1))
        reactor.listenTCP(8789, pb.PBServerFactory(RemoteGame(board)))
        print "Running server..."
        installSignalHandlers=0
        reactor.run(installSignalHandlers)
        
        
class GameClient(threading.Thread):
    def run(self):
        installSignalHandlers=0
        reactor.run(installSignalHandlers)
        
    def connect(self, address, port):
        self.connected = False
        clientFactory = pb.PBClientFactory()
        reactor.connectTCP(address, port,clientFactory)
        d = clientFactory.getRootObject()
        def gotRoot(ref):
            self.ref = ref
            self.connected = True
            print "connected!"
        d.addCallback(gotRoot)
        return self
    
    def sendHitCommand(self, position):
        d = self.ref.callRemote("hitTarget", position.row, position.column);
        return d
    
    def getHasBoatsAlive(self):
        d = self.ref.callRemote("hasBoatsAlive");
        return d
        