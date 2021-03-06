from kivy.support import install_twisted_reactor
install_twisted_reactor()

from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.factory.app.on_connection(self.transport)

    def dataReceived(self, data):
        self.factory.app.print_message(data)


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def __init__(self, app):
        self.app = app

    def clientConnectionLost(self, conn, reason):
        self.app.print_message("connection lost")

    def clientConnectionFailed(self, conn, reason):
        self.app.print_message("connection failed")


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.actionbar import ActionBar
from kivy.properties import ObjectProperty
from kivy.garden.graph import Graph, SmoothLinePlot
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

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
    connection = None

    def connect_to_server(self):
        print('connect_to_server run')
        reactor.connectTCP('localhost', 8000, EchoFactory(self))

    def on_connection(self, connection):
        self.print_message("connected succesfully!")
        self.connection = connection

    def send_message(self, *args):
        self.connection.write('lightswitch1')

    def print_message(self, msg):
        print(msg + "\n")

class RoomTemp(Screen):
    pass

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
    RoomTemp:

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
        padding: 10,130,10,130
        Button:
            background_normal: 'belgen-button.png'
            on_press: app.root.current = 'belgen'
        Button:
            background_normal: 'battery.png'
        Button:
            background_normal: 'light-bulb.png'
            on_press: app.root.current = 'lights'
        Button:
            background_normal: 'temp.png'
            on_press: app.root.current = 'temp'

<BElGenLiveGraph>:
    name: 'belgen'
    actionbar: navbar
    NavBar:
        id: navbar

<Lights>:
    name: 'lights'
    actionbar: navbar
    source: root.connect_to_server()
    NavBar:
        id: navbar
    BoxLayout:
        padding: 100,200,100,200
        Switch:
            id: ls1
            on_active: root.send_message()

<RoomTemp>:
    name: 'temp'
    actionbar: navbar
    NavBar:
        id: navbar
    Label:
        font_name: 'DroidSans'
        font_size: 128
        text: '00.0' + u'\u00B0' + 'C'


<NavBar>:
    pos_hint: {'top':1}
    ActionView:
        ActionPrevious:
            title: 'BelGen v3.0.1p'
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
    connection = None

    def build(self):
        return smsettings

    def exit_app(self):
        return exit().stop()

if __name__=='__main__':
    HomeUtilities().run()
