'''
Created on 09/09/2009

@author: emuenz
'''
from MVC.EventManager import EventManager
from events.keyboard import KeyboardEvent
from gui.Camera import FreeCamera
from gui.MainWindow import *
from pygame.locals import *
import pygame

class Battleships(object):
    isFinished = False
    def __init__(self):
        pygame.init()
        
        self.eventManager = EventManager()
        
        self.view = MainWindow(pygame)
        
        camera = FreeCamera(self.eventManager)
        self.view.AddCamera(camera)
        
    def handleEvent(self, event):
        if event.type == KEYDOWN or event.type == KEYUP:
            self.eventManager.Post(KeyboardEvent(event.type, event.key))

    def mainLoop(self):
        while not self.isFinished:
            event = pygame.event.poll()
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                break
            
            self.handleEvent(event)
            
            self.view.Render()
