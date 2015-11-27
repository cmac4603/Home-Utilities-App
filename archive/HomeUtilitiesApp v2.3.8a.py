from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.actionbar import ActionBar
from kivy.properties import ObjectProperty
from kivy.garden.graph import Graph, SmoothLinePlot

__version__"2.3.8a"

class MenuScreen(Screen):
    actionbar = ObjectProperty()

class BElGenLiveGraph(Screen):
    def __init__(self, **kwargs):
        super(BElGenLiveGraph, self).__init__(**kwargs)
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                      x_ticks_major=25, y_ticks_major=1,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=-0, xmax=10, ymin=-12,
                      ymax=12)
        plot = SmoothLinePlot(color=[0.49, 0.98, 1, 1])
        with open("adclog.txt") as fh:
            coords = []
            for line in fh:
                line = line.strip('()\n')  # Get rid of the newline and parentheses
                line = line.split(', ')  # Split into two parts
                c = tuple(float(x) for x in line)  # Make the tuple
                coords.append(c)
        plot.points = coords
        graph.add_plot(plot)
        self.add_widget(graph)

class Lights(Screen):
    def callback(self, instance, value):
            if value is True:
                print instance, 'is on!'
            elif value is False:
                print instance, 'is off!'

class NavBar(ActionBar):
    def go_back(self, *args):
        smsettings.current = 'menu'

class ScreenManagement(ScreenManager):
    pass

smsettings = Builder.load_string( """
ScreenManagement:
    MenuScreen:
    BElGenLiveGraph:
    Lights:

<MenuScreen>:
    name: 'menu'
    actionbar: navbar
    Image:
        source: 'home_wallpaper2.jpg'
        allow_stretch: True
        keep_ratio: False
    NavBar:
        id: navbar
    BoxLayout:
        padding: 10,300,10,300
        Button:
            background_normal: 'belgen-button.png'
            on_press: app.root.current = 'belgen'
        Button:
            background_normal: 'battery.png'
        Button:
            background_normal: 'light-bulb.png'
            on_press: app.root.current = 'lights'
        Button:
            background_normal: 'none.png'
            text: 'None'
            color: (1,0,0,1)

<BElGenLiveGraph>:
    name: 'belgen'
    actionbar: navbar
    NavBar:
        id: navbar

<Lights>:
    name: 'lights'
    actionbar: navbar
    NavBar:
        id: navbar
    BoxLayout:
        padding: 150,250,150,250
        Switch:
            id: light_switch1
            on_active: root.callback(*args)
        Switch:
            id: light_switch2
            on_active: root.callback(*args)
        Switch:
            id: light_switch3
            on_active: root.callback(*args)
        Switch:
            id: light_switch4
            on_active: root.callback(*args)

<NavBar>:
    pos_hint: {'top':1}
    ActionView:
        ActionPrevious:
            title: 'Home Utilities v2.3.7'
            app_icon: 'MB__home.png'
            with_previous: False
            on_release: root.go_back()
        ActionOverflow:
        ActionButton:
            text: 'Btn0'
            icon: 'atlas://data/images/defaulttheme/audio-volume-high'
        ActionButton:
            text: 'Btn1'
        ActionButton:
            text: 'Btn2'
        ActionGroup:
            text: 'Group1'
            ActionButton:
                text: 'Btn3'
            ActionButton:
                text: 'Btn4'
            ActionButton:
                text: 'Exit'
                on_press: app.exit_app()
""" )

class HomeUtilities(App):
    def build(self):
        return smsettings

    def exit_app(self):
        return exit().stop()

if __name__=='__main__':
    HomeUtilities().run()