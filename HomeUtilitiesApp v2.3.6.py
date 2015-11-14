from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.actionbar import ActionBar
from ElectricGraph2 import ElectricGraph2
from kivy.properties import ObjectProperty


class MenuScreen(Screen):
    actionbar = ObjectProperty()

class BElGenLiveGraph(Screen):
    def call_graph(self):
        return ElectricGraph2().run()

    def back_button(self, *args):
        smsettings.current = 'menu'

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
        padding: 10,200,10,200
        spacing: 10
        Button:
            background_normal: 'lightning2.png'
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
    on_enter: root.call_graph()
    BoxLayout:
        Button:
            background_normal: 'black_wallpaper.jpg'
            on_press: root.back_button()

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
            title: 'Home Utilities v2.3.6'
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