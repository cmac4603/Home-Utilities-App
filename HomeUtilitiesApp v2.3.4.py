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
    ActionBar:
        pos_hint: {'top':1}
        icon: 'MB__home.png'
        ActionView:
            use_separator: True
            ActionPrevious:
                title: 'Home Utilities v2.3.4'
                with_previous: False
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
                    text: 'Btn5'
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
    ActionBar:
        pos_hint: {'top':1}
        ActionView:
            use_separator: True
            ActionPrevious:
                title: 'Light Switches'
                with_previous: 'menu'
            ActionOverflow:
            ActionButton:
                text: 'Btn0'
                icon: 'atlas://data/images/defaulttheme/audio-volume-high'
            ActionButton:
                text: 'Btn1'
            ActionButton:
                text: 'Btn2'
            ActionButton:
                text: 'Btn3'
            ActionButton:
                text: 'Btn4'
            ActionGroup:
                text: 'Group1'
                ActionButton:
                    text: 'Btn5'
                ActionButton:
                    text: 'Btn6'
                ActionButton:
                    text: 'Btn7'
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