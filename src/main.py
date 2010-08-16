'''
Created on 09/09/2009

@author: emuenz
'''
from game.Battleships import Battleships 
#from game.network.service import GameServer

if __name__ == '__main__':
    app = Battleships()
    app.mainLoop();

#    GameServer().start()
