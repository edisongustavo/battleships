'''
Created on 09/09/2009

@author: emuenz
'''
import engine.render

class Board(engine.render.RenderObject):
    
    class Grid(engine.render.RenderObject):
        """
        Represents the grid that will be drawn over the water, in which we
        can differentiate each cell that the user can see and interact
        """
        def __init__(self):
            engine.render.RenderObject.__init__(self)
#            self.first_line = engine.render.Object()
#            gl_object = engine.render.Object()
#            #TODO [edison]: how should I add a line?
#            #gl_object.add_line((0.0, -1.0), (0.0, 1.0))
#            gl_object.color = engine.render.COLOR_WHITE
#            self._gl_object = gl_object

        
    class Water(engine.render.RenderObject):
        """
        The water that will be drawn. It is just a flat shape, but I want it
        to be a fully simulated water in the future
        """
        def __init__(self):
            engine.render.RenderObject.__init__(self)
            self.gl_object.vertices = [(-1.0, -1.0, 1.0)
                               , (1.0, -1.0, 1.0)
                               , (1.0, 1.0, 1.0)
                               , (-1.0, 1.0, 1.0)]
            self.gl_object.texture = engine.render.Texture("data/textures/water.jpg") 
            
    def __init__(self):
        engine.render.RenderObject.__init__(self)
        self.__water = self.Water() 
        self.__grid = self.Grid() 
    
    def _render(self):
        self.__water.render()
        self.__grid.render()
