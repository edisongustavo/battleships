'''
Created on 09/09/2009

@author: emuenz
'''
from OpenGL.GL import *
import pygame
from gui import transformations

class Texture(object):
    
    def __init__(self, file):
        image = pygame.image.load(file)
        buffer = pygame.image.tostring(image, 'RGBX', 1)
        
        self.__texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, int(self.__texture))
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, buffer)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    
    @property    
    def raw(self):
        return self.__texture

class RenderObject(object):
    """ Parent representing a Render object """
    def __init__(self):
        pass
    
    transformations = []
    
    def render(self):
        for transformation in self.transformations:
            transformation.execute()

        self._render()
        
    def _render(self):
        # no-op on purpose. Derived objects must override this method, so it is a "protected method"
        pass

class Board(RenderObject):
    
    class Grid(RenderObject):
        """
        Represents the grid that will be drawn over the water, in which we
        can differentiate each cell that the user can see and interact
        """
        def __init__(self):
            pass
        
        def _render(self):
            pass
        
    class Water(RenderObject):
        """
        The water that will be drawn. It is just a flat shape, but I want it
        to be a fully simulated water in the future
        """
        def __init__(self):
            self.texture = Texture("data/textures/water.jpg")
            
        def _render(self):
            # Front Face
            glBindTexture(GL_TEXTURE_2D, int(self.texture.raw))
            glBegin(GL_QUADS)
            glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, 1.0)
            glTexCoord2f(1.0, 0.0); glVertex3f(1.0, -1.0, 1.0)
            glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, 1.0)
            glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, 1.0)
            glEnd();
            
    def __init__(self):
        self.__water = self.Water() 
        self.__grid = self.Grid() 
    
    def _render(self):
        self.__water.render()
        self.__grid.render()