'''
Created on 09/09/2009

@author: emuenz
'''
from OpenGL.GL import *
import pygame

class Board(object):
    class RotationAngles:
        """ Helper class for rotations """
        def __init__(self):
            self.x = self.y = self.z = 0
            
        def rotate(self):
            glRotatef(self.x, 1, 0, 0)
            glRotatef(self.y, 0, 1, 0)
            glRotatef(self.z, 0, 0, 1)

    def __init__(self):
        self.rotation = self.RotationAngles()
        
        self._load_texture()
    
    def _load_texture(self):
        file = 'data/textures/water.jpg'
        image = pygame.image.load(file)
        buffer = pygame.image.tostring(image, 'RGBX', 1)
        
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, int(self.texture))
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, buffer)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    
    def render(self):
        self.rotation.x += 0.1
        self.rotation.y += 0.15
        self.rotation.z += 0.25
        
        self.rotation.rotate()
        
        glBindTexture(GL_TEXTURE_2D, int(self.texture))
        glBegin(GL_QUADS)

        # Front Face
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, 1.0)
    
        # Back Face
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(1.0, -1.0, -1.0)
    
        # Top Face
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, -1.0)
    
        # Bottom Face
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, 1.0)
    
        # Right face
        glTexCoord2f(1.0, 0.0); glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(1.0, -1.0, 1.0) 
    
        # Left Face
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, 1.0, 1.0) 
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, -1.0)    
        glEnd();
