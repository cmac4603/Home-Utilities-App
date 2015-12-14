from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
import pyowm

class Weather(Screen):
    addr = StringProperty()

    def wx_forecast(self):
        owm = pyowm.OWM('fa7813518ed203b759f116a3bac9bcce')
        observation = owm.weather_at_place('London,uk')
        w = observation.get_weather()
        i = w.get_weather_icon_name()
        addr = str("http://openweathermap.org/img/w/" + i + ".png")
        print(addr)
        return addr

    def update(self):
        Clock.schedule_interval(self.ids.wxlabel.source, 45)
    #def update(self):
        #self.wx_forecast()
        #Clock.schedule_interval(lambda dt: self.ids.wxlabel, 30)

class ScreenManagement(ScreenManager):
    pass

smsettings = Builder.load_string( """
ScreenManagement:
    Weather:

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
                on_release:
""" )

class HomeUtilities(App):
    def build(self):
        return smsettings

if __name__=='__main__':
    HomeUtilities().run()
