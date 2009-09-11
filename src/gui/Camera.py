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
    
    isMovingForward= False
    isMovingBackward= False
    isStrafingLeft= False
    isStrafingRight= False
    
    def __init__(self, eventDispatcher):
        eventDispatcher.RegisterListener(self)
        
    def Notify(self, event):
        if isinstance(event, KeyboardEvent):
            
            isStarting = event.type == pygame.KEYDOWN
             
            if event.key == pygame.K_UP:
                self.isMovingForward= isStarting 
            if event.key == pygame.K_DOWN:
                self.isMovingBackward= isStarting
                
            if event.key == pygame.K_LEFT:
                self.isStrafingLeft= isStarting
            if event.key == pygame.K_RIGHT:
                self.isStrafingRight= isStarting
            
    def Render(self):
        if self.isMovingForward:
            self.z += 0.01

        if self.isMovingBackward:
            self.z -= 0.01
            
        if self.isStrafingLeft:
            self.x += 0.01
            
        if self.isStrafingRight:
            self.x -= 0.01

        glTranslatef(self.x, self.y, self.z)