from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from ElectricGraph import ElectricGraph
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

sm = ScreenManager(transition=WipeTransition())
homescreen = Screen(name='Home Screen')
sm.add_widget(homescreen)

class HomeButtons(GridLayout):
    def __init__(self, **kwargs):
        super(HomeButtons, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 3
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

def callbackgraph(instance):
    return ElectricGraph().run()

def callbacklights(instance):
    print("The button <%s> is being pressed" %instance.text)

def callbackunused(instance):
    print("The button <%s> is being pressed" %instance.text)

class HomeUtilitiesApp(App):
    def build(self):
        return sm

HomeUtilitiesApp().run()
