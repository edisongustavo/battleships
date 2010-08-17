'''
Created on 09/09/2009

@author: emuenz
'''
from pygame.locals import *
import gui.camera
import gui.windows
import pygame
import time
from game import events

class Fps(object):
    """Class to calculate the FPS that the game is running """
    
    _fps = 120 #doesnt start with 0 because the user might want to start using the camera before being able to measure the _fps 
    
    def __init__(self):
        self.accumulated_time = 0
        self.frames = 0
        self._time_on_current_frame = 0
        self.time = time.time()
    
    def update(self):
        previous_time = self.time
        self.time = time.time()
        self.frames += 1
        
        difference = self.time - previous_time
        self._time_on_current_frame = difference
        self.accumulated_time += difference
        if self.accumulated_time >= 1:
            self._fps = self.frames / self.accumulated_time
            self.frames = 0
            self.accumulated_time = 0
    
class GameTicks(object):
    """ Class the handle the current tick of the game """
    MAX_GAME_TICKS = 120
    
    def __init__(self, fps):
        self._game_tick = 0
        self._fps = fps
        self._calculate()
        
    def _calculate(self):
        self.MAX_FPS = 1000 / self.MAX_GAME_TICKS
        
    def update(self):
        self._fps.update()
        self._game_tick += 1
        
        #HACK: remove this sleep thing, it is here only for testing
        current_frame_time = self._fps._time_on_current_frame
        if current_frame_time < self.MAX_FPS:
            sleep_time_inMS = self.MAX_FPS - current_frame_time
            time.sleep(sleep_time_inMS / 1000)
    
    @property
    def tick(self):
        return self._game_tick
    
    @property
    def fps(self):
        #HACK [edison]: must remove this, should not rely on this kind of behaviour
        return self._fps._fps

class Battleships(object):
    """ The main class of the game. It glues everything together """
    def __init__(self):
        self.is_finished = False
        
        pygame.init()
        
        self._event_manager = events.EventManager()
        self._fps = Fps()
        self._ticks = GameTicks(self._fps)
        
        camera = gui.camera.FreeCamera(self._event_manager, self._ticks)
        self._view = gui.windows.MainWindow(camera)
        self._view.add_object(gui.objects.Board())
        
    def handleEvent(self, event):
        if event.type == KEYDOWN or event.type == KEYUP:
            self._event_manager.Post(events.KeyboardEvent(event.type, event.key))

    def main_loop(self):
        while not self.is_finished:
            event = pygame.event.poll()
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                break
            
            self.handleEvent(event)
            
            self._view.show_fps(self._fps._fps)
            self._view.render()
            
            self._ticks.update()
