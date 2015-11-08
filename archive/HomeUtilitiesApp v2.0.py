from kivy.app import App
from kivy.uix.button import Button
from ElectricGraph import ElectricGraph
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.gridlayout import GridLayout
import android

sm = ScreenManager()
homescreen = Screen(name='HomeScreen')
belgenscreen = Screen(name='BElGenLiveGraph')
sm.add_widget(homescreen)
sm.add_widget(belgenscreen)

class HomeScreen(GridLayout, Screen):
    def __init__(self, **kwargs):
        print(sm.current_screen)
        self.register_event_type('on_back_pressed')
        self.register_event_type('on_menu_pressed')
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

    def on_back_pressed(self, *args):
        pass

    def on_menu_pressed(self, *args):
        pass

class BelGenLiveGraph(Screen):
    def __init__(self, **kwargs):
        print(sm.current_screen)
        self.register_event_type('on_back_pressed')
        self.register_event_type('on_menu_pressed')
        super(HomeScreen, self).__init__(**kwargs)

def callbackgraph(instance):
    sm.current = 'BElGenLiveGraph'
    print(sm.current_screen)
    ElectricGraph().run()

def callbacklights(instance):
    print("The button <%s> is being pressed" %instance.text)

def callbackunused(instance):
    print("The button <%s> is being pressed" %instance.text)

class HomeUtilitiesApp(App):
    def build(self):
        self.bind(on_start=self.post_build_init)
        self.effectwidget
        return HomeScreen()

    def post_build_init(self, ev):
            # Map Android keys
            if platform == 'android':
                android.map_key(android.KEYCODE_BACK, 1000)
                android.map_key(android.KEYCODE_MENU, 1001)
            win = self._app_window
            win.bind(on_keyboard=self._key_handler)

    def _key_handler(self, *args):
        key = args[1]
        print key
        # 1000 is "back" on Android
        # 27 is "escape" on computers
        # 1001 is "menu" on Android
        if key in (1000, 27):
            self.sm.current_screen.dispatch("on_back_pressed")
            return True
        elif key == 1001:
            self.sm.current_screen.dispatch("on_menu_pressed")
            return True

HomeUtilitiesApp().run()
