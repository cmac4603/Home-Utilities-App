from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class HomeButtons(GridLayout):
    def __init__(self, **kwargs):
        super(HomeButtons, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        btn1 = Button(text='BElGen Live Graph')
        btn2 = Button(text='Lights')
        btn3 = Button(text='Unused')
        btn4 = Button(text='Unused')
        self.add_widget(btn1)
        btn1.bind(on_press = callbackgraph)
        self.add_widget(btn2)
        btn2.bind(on_press = callbacklights)
        self.add_widget(btn3)
        btn3.bind(on_press = callbackunused)
        self.add_widget(btn4)
        btn4.bind(on_press = callbackunused)

def callbackgraph(instance):
    print('The button <%s> is being pressed' %instance.text)

def callbacklights(instance):
    print('The button <%s> is being pressed' %instance.text)

def callbackunused(instance):
    print('The button is <%s>' %instance.text)

class HomeUtilitiesApp(App):
    def build(self):
        return HomeButtons()

HomeUtilitiesApp().run()
