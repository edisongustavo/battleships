'''
Created on 10/09/2009

@author: Guga
'''
from OpenGL.GL import *
from events.keyboard import KeyboardEvent
import pygame

class FreeCamera(object):
    '''
    A free camera that does simple movement
    '''
    
    x = 0
    y = 0
    z = 0
    
    #Refactor: Should be in World coordinates. This value doesnt say much...
    zSpeed = 10
    strafeSpeed = 5
    
    isMovingForward = False
    isMovingBackward = False
    isStrafingLeft = False
    isStrafingRight = False
    
    def __init__(self, eventDispatcher, gameTick):
        eventDispatcher.RegisterListener(self)
        self.gameTick = gameTick
        
    def Notify(self, event):
        if isinstance(event, KeyboardEvent):
            
            isStarting = event.type == pygame.KEYDOWN
             
            if event.key == pygame.K_UP:
                self.isMovingForward = isStarting 
            if event.key == pygame.K_DOWN:
                self.isMovingBackward = isStarting
                
            if event.key == pygame.K_LEFT:
                self.isStrafingLeft = isStarting
            if event.key == pygame.K_RIGHT:
                self.isStrafingRight = isStarting
                
            if event.key == pygame.K_F1:
                self.gameTick.MAX_GAME_TICKS += 1
                self.gameTick.calculate()
            if event.key == pygame.K_F2:
                self.gameTick.MAX_GAME_TICKS -= 1
                self.gameTick.calculate()
            
    def Render(self):
        if self.isMovingForward:
            self.z += self.normalizeValue(self.gameTick.GetFps(), self.zSpeed)

        if self.isMovingBackward:
            self.z -= self.normalizeValue(self.gameTick.GetFps(), self.zSpeed)
            
        if self.isStrafingLeft:
            self.x += self.normalizeValue(self.gameTick.GetFps(), self.strafeSpeed)
            
        if self.isStrafingRight:
            self.x -= self.normalizeValue(self.gameTick.GetFps(), self.strafeSpeed)

        glTranslatef(self.x, self.y, self.z)

    def normalizeValue(self, fps, speed):
        return speed / fps
