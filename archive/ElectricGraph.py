from math import sin
from kivy.app import App
from kivy.garden.graph import Graph, MeshLinePlot
#import kivy.graphics.instructions.CanvasBase
#from kivy.graphics import Fbo

class ElectricGraph(App):
    def build(self):
        print 'create graph'
        #self.canvas.add(Color(1., 1., 0))
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                      x_ticks_major=25, y_ticks_major=1,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)
        return graph

    #def on_start(self):
        #print 'create d+s fbo'
        #fbo = Fbo(size=(100, 100))
        #print fbo

    #def android_back(self):
        #sm.remove_screen(screen)
