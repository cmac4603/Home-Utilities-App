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
        print ('the switch is ', value)

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
        Switch:
            on_active: root.callback(*args)
""" )

class HomeUtilities(App):
    def build(self):
        return smsettings

if __name__=='__main__':
    HomeUtilities().run()