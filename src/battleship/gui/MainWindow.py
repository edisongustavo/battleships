'''
Created on 09/09/2009

@author: emuenz
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from gui.objects import Board
from pygame.locals import *

class MainWindow():
    objects = []
    
    camera = None
    
    def AddCamera(self, camera):
        self.camera = camera
        
    def __init__(self, pygame):
        self.display = pygame.display;
        self.display.set_mode((640, 480), OPENGL | DOUBLEBUF)
        
        self.windowResize((640, 480))
        self.initOpenGL()
        
        self.objects.append(Board())
        
    def windowResize(self, (width, height)):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
    def initOpenGL(self):
        glShadeModel(GL_SMOOTH)
        glClearColor(0, 0, 0, 0)
        glClearDepth(1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    
    def ShowFps(self, fps):
        pass #self.display.set_caption("Fps: {0}".format(fps))
        
    def Render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        if not (self.camera == None):
            self.camera.Render()
        else:
            glTranslatef(0, 0, -5.0)
        
        for object in self.objects:
            object.Render()
        
        self.display.flip()
