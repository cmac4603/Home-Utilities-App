from kivy.app import App
from kivy.uix.button import Button
from ElectricGraph2 import ElectricGraph2
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.gridlayout import GridLayout
from plyer import vibrator

sm = ScreenManager()
homescreen = Screen(name='HomeScreen')
belgenscreen = Screen(name='BElGenLiveGraph')
sm.add_widget(homescreen)
sm.add_widget(belgenscreen)

class HomeScreen(GridLayout, Screen):
    def __init__(self, **kwargs):
        print(sm.current_screen)
        super(HomeScreen, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 2
        btn1 = Button(text="BElGen Live Graph")
        btn2 = Button(text="Lights")
        btn3 = Button(text="Unused")
        btn4 = Button(text="Unused")
        btn5 = Button(text="Unused")
        btn6 = Button(text="Unused")
        self.add_widget(btn1)
        btn1.bind(on_press = callbackgraph)
        self.add_widget(btn2)
        btn2.bind(on_press = callbacklights)
        self.add_widget(btn3)
        btn3.bind(on_press = callbackunused)
        self.add_widget(btn4)
        btn4.bind(on_press = callbackunused)
        self.add_widget(btn5)
        btn5.bind(on_press = callbackunused)
        self.add_widget(btn6)
        btn6.bind(on_press = callbackunused)
        vibrator.vibrate(0.1)

class BelGenLiveGraph(Screen):
    pass

def callbackgraph(instance):
    sm.current = 'BElGenLiveGraph'
    print(sm.current_screen)
    ElectricGraph2().run()

def callbacklights(instance):
    print("The button <%s> is being pressed" %instance.text)

def callbackunused(instance):
    print("The button <%s> is being pressed" %instance.text)

class HomeUtilitiesApp(App):
    def build(self):
        return HomeScreen()

HomeUtilitiesApp().run()
