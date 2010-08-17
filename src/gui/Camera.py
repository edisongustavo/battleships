'''
Created on 10/09/2009

@author: Guga
'''
from OpenGL.GL import *
from game.events import KeyboardEvent
import pygame

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
        self.x = 0
        self.y = 0
        self.z = 0
        self._game_tick = gameTick
    
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
                
            if event.key == pygame.K_F1:
                self._game_tick.MAX_FPS += 1
                self._game_tick._calculate()
            if event.key == pygame.K_F2:
                self._game_tick.MAX_FPS -= 1
                self._game_tick._calculate()
            
    def render(self):
        if self.is_moving_forward:
            self.z += self._normalize(self.z_speed)

        if self.is_moving_backward:
            self.z -= self._normalize(self.z_speed)
            
        if self.is_strafing_left:
            self.x += self._normalize(self.strafe_speed)
            
        if self.is_strafing_right:
            self.x -= self._normalize(self.strafe_speed)

        glTranslatef(self.x, self.y, self.z)

    def _normalize(self, speed):
        return speed / self._game_tick.fps
