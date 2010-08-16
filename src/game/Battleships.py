'''
Created on 09/09/2009

@author: emuenz
'''
from gui.Camera import FreeCamera
from gui.MainWindow import *
from pygame.locals import *
import pygame
import time
from events.EventManager import *
from events.keyboard import * 

class Fps():
    
    fps = 120 #doesnt start with 0 because the user might want to start using the camera before being able to measure the fps 
    
    def __init__(self):
        self.accumulatedTime = 0
        self.frames = 0
        self.timeOnCurrentFrame = 0
        self.time = time.time()
    
    def Update(self):
        previousTime = self.time
        self.time = time.time()
        self.frames += 1
        
        difference = self.time - previousTime
        self.timeOnCurrentFrame = difference
        self.accumulatedTime += difference
        if self.accumulatedTime >= 1:
            self.fps = self.frames / self.accumulatedTime
            self.frames = 0
            self.accumulatedTime = 0
    
    def GetFps(self):
        return self.fps
    
    def GetCurrentFrameTime(self):
        return self.timeOnCurrentFrame
    
class GameTicks():
    MAX_GAME_TICKS = 120
    
    gameTick = 0
    
    def __init__(self, fps):
        self.fps = fps
        self.calculate()
        
    def calculate(self):
        self.MAX_TIME_PER_FRAME = 1000 / self.MAX_GAME_TICKS
        
    def Update(self):
        self.fps.Update()
        
        self.gameTick += 1
        
        currentFrameTime = self.fps.GetCurrentFrameTime()
        if currentFrameTime < self.MAX_TIME_PER_FRAME:
            timeToSleepInMs = self.MAX_TIME_PER_FRAME - currentFrameTime
            time.sleep(timeToSleepInMs / 1000)
    
    def GetFps(self):
        return self.fps.GetFps()
    
    def GetTick(self):
        return self.gameTick

class Battleships(object):
    isFinished = False
    def __init__(self):
        pygame.init()
        
        self.eventManager = EventManager()
        
        self.view = MainWindow(pygame)

        self.gameTicks = GameTicks(Fps())
                
        camera = FreeCamera(self.eventManager, self.gameTicks)
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
            
            self.view.ShowFps(self.gameTicks.GetFps())
            self.view.Render()
            
            self.gameTicks.Update()
