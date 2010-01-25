import threading
from twisted.spread import pb
from twisted.internet import reactor
from zope.interface import Interface, implements
from battleship.game.model import Position, Board

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
        self.board.hitAtPosition(position)
    
    def hasBoatsAlive(self):
        return self.board.hastBoatsAlive()
    
    # Remote Methods to be accessed during game
    def remote_hitTarget(self, row, column):
        self.hitTarget(Position(row, column))
    
    def remote_hasBoatsAlive(self): 
        return self.hasBoatsAlive()
    

    
class GameServer(threading.Thread):      
    def run(self):
        reactor.listenTCP(8789, pb.PBServerFactory(RemoteGame(Board(10, 10))))
        print "Running server..."
        reactor.run()
        
        
class GameClient:
    def connect(self, address, port):
        clientFactory = pb.PBClientFactory()
        reactor.connectTCP(address, port,clientFactory)
        def gotRoot(ref):
            self.ref = ref
        clientFactory.getRootObject().addCallback(gotRoot)
    
    def sendHitCommand(self, position):
        self.ref.remoteCall("hitTarget", position.row, position.column);
        