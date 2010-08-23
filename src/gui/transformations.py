'''
Created on 23/08/2010

@author: Guga
'''
from OpenGL.raw.GL import glRotatef

class RotationAngles(object):
    """ Helper class for rotations """
    def __init__(self):
        self.x = self.y = self.z = 0
        
    def rotate(self):
        glRotatef(self.x, 1, 0, 0)
    
        glRotatef(self.y, 0, 1, 0)
        glRotatef(self.z, 0, 0, 1)