'''
Created on 10/09/2009

@author: Guga
'''
from game.events import KeyboardEvent
import pygame
import engine.transformations

class FreeCamera(object):
    '''
    A free camera that does simple movement
    '''
    
    #Refactor: Should be in World coordinates. This value doesnt say much...
    z_speed = 10
    strafe_speed = 5
    
    def __init__(self, eventDispatcher, gameTick):
        self.is_moving_forward = False
        self.is_moving_backward = False
        self.is_strafing_left = False
        self.is_strafing_right = False
        self.__translation = engine.transformations.Translation()
        
        self.__game_tick = gameTick
    
        eventDispatcher.RegisterListener(self)
        
    def Notify(self, event):
        if isinstance(event, KeyboardEvent):
            is_starting = event.type == pygame.KEYDOWN
             
            if event.key == pygame.K_UP:
                self.is_moving_forward = is_starting 
            if event.key == pygame.K_DOWN:
                self.is_moving_backward = is_starting
                
            if event.key == pygame.K_LEFT:
                self.is_strafing_left = is_starting
            if event.key == pygame.K_RIGHT:
                self.is_strafing_right = is_starting
            
    def render(self):
        if self.is_moving_forward:
            self.__translation.z += self.__normalize(self.z_speed)

        if self.is_moving_backward:
            self.__translation.z -= self.__normalize(self.z_speed)
            
        if self.is_strafing_left:
            self.__translation.x += self.__normalize(self.strafe_speed)
            
        if self.is_strafing_right:
            self.__translation.x -= self.__normalize(self.strafe_speed)
            
        self.__translation.translate()

    def __normalize(self, speed):
        return speed / self.__game_tick.fps
