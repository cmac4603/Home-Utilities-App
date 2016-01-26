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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.actionbar import ActionBar, ActionItem
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.garden.graph import Graph, SmoothLinePlot
from kivy.core.audio import SoundLoader
from kivy.factory import Factory
from kivy.uix.popup import Popup
import pyowm

owm = pyowm.OWM('fa7813518ed203b759f116a3bac9bcce')
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()

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
                line = line.strip('()\n')
                line = line.split(', ')
                c = tuple(float(x) for x in line)
                coords.append(c)
        plot.points = coords
        graph.add_plot(plot)
        self.add_widget(graph)

class Lights(Screen):
    connection = None

    def connect_to_server(self):
        reactor.connectTCP('192.168.1.3', 8000, EchoFactory(self))

    def on_connection(self, connection):
        self.print_message("connected succesfully!")
        self.connection = connection

    def send_message(self, id, instance, value):
        if value is True:
            name = str(id)
            self.connection.write(name + ' on')
        elif value is False:
            name = str(id)
            self.connection.write(name + ' off')

    def print_message(self, msg):
        print(msg + "\n")

class RoomTemp(Screen):
    pass

class LoadMusic(Screen):
    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def load(self, path, filename):
        musicfile = str(filename)[3:][:-2]
        music = SoundLoader.load(musicfile)
        music.play()

    def cancel(self):
        smsettings.current = 'menu'

Factory.register('LoadMusic', cls=LoadMusic)

class Weather(Screen):

    def wx_forecast(self):
        i = w.get_weather_icon_name()
        addr = str("http://openweathermap.org/img/w/" + i + ".png")
        print(addr)
        return addr

    def dismiss_popup(self):
        self._popup.dismiss()

    def more_details(self):
        content = DetailDialog(cancel=self.dismiss_popup)
        self._popup = Popup(title="More details", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()


class DetailDialog(FloatLayout):
    cancel = ObjectProperty(None)

    def temp_details(self):
        wtemp = str(w.get_temperature('celsius'))
        wtemp2 = wtemp.replace("'", "")
        return wtemp2.strip("{}")

    def wind_details(self):
        wwind = str(w.get_wind())
        wwind2 = wwind.replace("'", "")
        wwind3 = wwind2.replace("u", "")
        return wwind3.strip("{}")

    def humi_details(self):
        whumi = str(w.get_humidity())
        whumi2 = whumi.replace("'", "")
        return whumi2.strip("{}")

Factory.register('DetailDialog', cls=DetailDialog)

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
    LoadMusic:
    Weather:

<MenuScreen>:
    name: 'menu'
    actionbar: navbar
    NavBar:
        id: navbar
    GridLayout:
        padding: 60,75,60,0
        rows: 2
        columns: 3
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
        Button:
            background_normal: 'headset.png'
            on_press: app.root.current = 'music'
        Button:
            background_normal: 'wx.png'
            on_press: app.root.current = 'weather'

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
        padding: 50,50,50,50
        Switch:
            id: ls1
            on_active: root.send_message('ls1', *args)
        GridLayout:
            columns: 1
            rows: 3
            padding: 50,50,50,0
            Button:
                size_hint_y: None
                height: 10
                size_hint_x: None
                width: 15
                text: 'On'
                on_press: print(ls2.value)
            Slider:
                id: ls2
                orientation: 'vertical'
                padding: 20
                max: 10
                min: 1
            Button:
                size_hint_y: None
                height: 10
                size_hint_x: None
                width: 15
                text: 'Off'
                on_press: print('off')
        Switch:
            id: ls3
            on_active: root.send_message('ls3', *args)
        Switch:
            id: ls4
            on_active: root.send_message('ls4', *args)

<RoomTemp>:
    name: 'temp'
    actionbar: navbar
    NavBar:
        id: navbar
    Label:
        font_size: 128
        text: '00.0' + u'\u00B0' + 'C'

<LoadMusic>:
    name: 'music'
    actionbar: navbar
    BoxLayout:
        padding: 10,50,10,10
        orientation: "vertical"
        FileChooserIconView:
            id: filechooser
            path: '~/Downloads/Music'
            on_submit: filechooser.selection, root.load(filechooser.path, filechooser.selection)
    NavBar:
        id: navbar

<Weather>:
    name: 'weather'
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        GridLayout:
            rows: 1
            padding: 200
            AsyncImage:
                id: wxlabel
                allow_stretch: True
                source: root.wx_forecast()
        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: 'Change Location'
                on_press:
            Button:
                text: 'More Details'
                on_release: root.more_details()
    NavBar:
        id: navbar

<DetailDialog>:
    GridLayout:
        cols: 1
        size: root.size
        pos: root.pos
        Label:
            pos: root.pos
            font_size: 24
            text: root.temp_details()
        Label:
            pos: root.pos
            font_size: 24
            text: 'wind ' + root.wind_details()
        Label:
            pos: root.pos
            font_size: 24
            text: 'humidity ' + root.humi_details()

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Back"
                on_release: root.cancel()

<NavBar>:
    pos_hint: {'top':1}
    ActionView:
        ActionPrevious:
            title: 'BelGen v3.2.1p'
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
