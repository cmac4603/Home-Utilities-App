from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from ElectricGraph2 import ElectricGraph2

class MenuScreen(Screen):
    pass

class BElGenLiveGraph(Screen):
    def callgraph(self):
        return ElectricGraph2().run()

class Lights(Screen):
    def callback(self, instance, value):
            if value is True:
                print instance, 'is on!'
            elif value is False:
                print instance, 'is off!'

class ScreenManagement(ScreenManager):
    pass


smsettings = Builder.load_string( """
ScreenManagement:
    MenuScreen:
    BElGenLiveGraph:
    Lights:

<MenuScreen>:
    name: 'menu'
    BoxLayout:
        padding: 10,200,10,200
        spacing: 10
        Button:
            text: 'BElGen Live Graph'
            on_press: app.root.current = 'belgen'
        Button:
            text: 'Lights'
            on_press: app.root.current = 'lights'
        Button:
            text: 'None'
        Button:
            text: 'None'

<BElGenLiveGraph>:
    name: 'belgen'
    on_enter: root.callgraph()

<Lights>:
    name: 'lights'
    BoxLayout:
        padding: 150,0,150,0
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
""" )

class HomeUtilities(App):
    def build(self):
        return smsettings

if __name__=='__main__':
    HomeUtilities().run()