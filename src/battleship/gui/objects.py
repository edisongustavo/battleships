'''
Created on 09/09/2009

@author: emuenz
'''
from OpenGL.GL import *
import pygame

class Board(object):
    xRotationAngle = yRotationAngle = zRotationAngle = 0
    def __init__(self):
        self.loadTexture()
        pass;
    
    def loadTexture(self):
        file = 'data/textures/water.jpg'
        textureSurface = pygame.image.load(file)
        textureBuffer = pygame.image.tostring(textureSurface, 'RGBX', 1)
        
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, int(self.texture))
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, textureSurface.get_width(), textureSurface.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, textureBuffer)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    
    def Render(self):
        self.xRotationAngle += 0.1
        self.yRotationAngle += 0.15
        self.zRotationAngle += 0.25
        
        glRotatef(self.xRotationAngle, 1, 0, 0)
        glRotatef(self.yRotationAngle, 0, 1, 0)
        glRotatef(self.zRotationAngle, 0, 0, 1)
        
        glBindTexture(GL_TEXTURE_2D, int(self.texture))
        glBegin(GL_QUADS)
        # Front Face
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
