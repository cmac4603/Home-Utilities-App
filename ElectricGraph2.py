from math import sin
from kivy.app import App
from kivy.garden.graph import Graph, MeshLinePlot
from get_v import getvoltages

class ElectricGraph2(App):
    def build(self):
        print 'create graph'
        #self.canvas.add(Color(1., 1., 0))
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                      x_ticks_major=25, y_ticks_major=1,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        with open("adclog.txt") as fh:
            coords = []
            for line in fh:
                line = line.strip('()\n')  # Get rid of the newline and  parentheses
                line = line.split(', ')  # Split into two parts
                c = tuple(float(x) for x in line)  # Make the tuple
                coords.append(c)
        plot.points = coords
        graph.add_plot(plot)
        return graph

ElectricGraph2().run()