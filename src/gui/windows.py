'''
Created on 09/09/2009

@author: emuenz
'''
from OpenGL.GL import *
from OpenGL.GLU import *
import gui.objects
import pygame

class MainWindow():
        
    def __init__(self, camera):
        self.__objects = []
        self.__camera = camera

        self.__pygame_display = pygame.display;
        self.__pygame_display.set_mode((640, 480), pygame.locals.OPENGL | pygame.locals.DOUBLEBUF)
        
        self.__window_resize((640, 480))
        self.__init_openGL()
        
    def add_object(self, object):
        self.__objects.append(gui.objects.Board())
        
    def __window_resize(self, (width, height)):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
    def __init_openGL(self):
        glShadeModel(GL_SMOOTH)
        glClearColor(0, 0, 0, 0)
        glClearDepth(1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    
    def show_fps(self, fps):
        pass #self.__pygame_display.set_caption("Fps: {0}".format(fps))
        
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        self.__camera.render()
        
        for object in self.__objects:
            object.render()
        
        self.__pygame_display.flip()