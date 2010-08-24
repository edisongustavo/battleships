'''
Created on 23/08/2010

@author: Guga
'''
from OpenGL.GL.exceptional import glGenTextures, glBegin, glEnd
from OpenGL.GL.images import glTexImage2D
from OpenGL.constants import GL_UNSIGNED_BYTE
from OpenGL.raw.GL import glBindTexture, glTexParameterf, glVertex3f
from OpenGL.raw.GL.constants import GL_NEAREST, GL_TEXTURE_2D, GL_RGBA, \
    GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_FILTER, GL_QUADS
import pygame

#Color constants
COLOR_WHITE = (0, 0, 0)

class Texture(object):
    """ Class to abstract the use of textures in OpenGL """
    def __init__(self, filename):
        image = pygame.image.load(filename)
        data = pygame.image.tostring(image, 'RGBX', 1)
        
        self.__texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, int(self.__texture))
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        
    def render(self):
        pass

    @property    
    def raw(self):
        return self.__texture
    
class Object(object):
    """ Class to abstract the use of OpenGL objects """
    
    def __init__(self):
        self.texture = None
        self.vertices = []
        
    def render(self):
        if self.texture is not None:
            self.texture.render()

        #TODO: do not use this kind drawing, but instead pass all vertices, like in the tutorial
        #TODO: check how to map the textures too 
        glBegin(GL_QUADS)
        for v in self.vertices:
            glVertex3f(v[0], v[1], v[2])
        glEnd()
    
class RenderObject(object):
    """ Parent representing a Render object """
    
    def __init__(self):
        self.gl_object = Object()
    
    transformations = []
    
    def render(self):
        for transformation in self.transformations:
            transformation.execute()

        self._render()
        
    def _render(self):
        """
         if derived objects want to customize how they're rendered, they should
         override this method, so it is a "protected method"
        """
        self.gl_object.render()
