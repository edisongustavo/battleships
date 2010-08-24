'''
Created on 09/09/2009

@author: emuenz
'''
import gui.camera
import gui.windows
import pygame
import time
from game import events
import gui.objects

class Fps(object):
    """Class to calculate the FPS that the game is running """
    
    def __init__(self):
        self.accumulated_time = 0
        self.frames = 0
        self._time_on_current_frame = 0
        self.time = time.time()
        
        self.fps = 120 #doesnt start with 0 because the user might want to start using the camera before being able to measure the __fps 
    
    def update(self):
        previous_time = self.time
        self.time = time.time()
        self.frames += 1
        
        difference = self.time - previous_time
        self._time_on_current_frame = difference
        self.accumulated_time += difference
        if self.accumulated_time >= 1:
            self.fps = self.frames / self.accumulated_time
            self.frames = 0
            self.accumulated_time = 0

#TODO this class needs a refactor. It's too confusing now
class GameTicks(object):
    """ Class the handle the current tick of the game """
    
    def __init__(self, fps):
        self.MAX_GAME_TICKS = 120
        self.__game_tick = 0
        self.__fps = fps
        self.__calculate()
        
    def __calculate(self):
        self.MAX_FPS = 1000 / self.MAX_GAME_TICKS
        
    def update(self):
        self.__fps.update()
        self.__game_tick += 1
        
        #HACK: remove this sleep thing, it is here only for testing
        current_frame_time = self.__fps._time_on_current_frame
        if current_frame_time < self.MAX_FPS:
            sleep_time_inMS = self.MAX_FPS - current_frame_time
            time.sleep(sleep_time_inMS / 1000)
    
    @property
    def tick(self):
        return self.__game_tick
    
    @property
    def fps(self):
        #HACK [edison]: must remove this, should not rely on this kind of behaviour
        return self.__fps.fps

class Battleships(object):
    """ The main class of the game. It glues everything together """
    def __init__(self):
        self.is_finished = False
        
        pygame.init()
        
        self.__event_manager = events.EventManager()
        self.__fps = Fps()
        self.__ticks = GameTicks(self.__fps)
        
        camera = gui.camera.FreeCamera(self.__event_manager, self.__ticks)
        self.__view = gui.windows.MainWindow(camera)
        self.__view.add_object(gui.objects.Board())
        
    def handleEvent(self, event):
        if event.type == pygame.locals.KEYDOWN or event.type == pygame.locals.KEYUP:
            self.__event_manager.Post(events.KeyboardEvent(event.type, event.key))

    def main_loop(self):
        while not self.is_finished:
            event = pygame.event.poll()
            if event.type == pygame.locals.QUIT or (event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_ESCAPE):
                break
            
            self.handleEvent(event)
            
            self.__view.show_fps(self.__fps.fps)
            self.__view.render()
            
            self.__ticks.update()
