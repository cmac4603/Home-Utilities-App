from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from ElectricGraph2 import ElectricGraph2

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

Builder.load_string( """
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'BElGen Live Graph'
            on_press: root.manager.current = 'belgen'
            on_press: root.callgraph()
        Button:
            text: 'Lights'
            on_press: root.manager.current = 'lights'
        Button:
            text: 'None'
        Button:
            text: 'None'

<BElGenLiveGraph>:
""" )

# Declare both screens

class MenuScreen(Screen):
    def callgraph(self):
        return ElectricGraph2().run()

class BElGenLiveGraph(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(BElGenLiveGraph(name='belgen'))

class HomeUtilities(App):
    def build(self):
        return sm

if __name__=='__main__':
    HomeUtilities().run()