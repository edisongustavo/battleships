
from battleship.game.network.service import GameClient
from battleship.game.model import Position



client = GameClient()
client.connect("localhost", 8789).start()

while not client.connected:
    pass

def alive(alive):
    print "Has more boats? "+alive.__str__()
d = client.getHasBoatsAlive()
d.addCallback(alive)
d = client.sendHitCommand(Position(1,1))
def hitted(hit):
    print "hitted? "+hit.__str__()
d.addCallback(hitted)
d = client.getHasBoatsAlive()
d.addCallback(alive)