import kivy
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.actionbar import ActionBar

class MainWindow(Screen):
    pass

class SelectScreen(Screen):
    pass

class RHScreen(Screen):
    pass

class FCHScreen(Screen):
    pass

class PCHScreen(Screen):
    pass

class PHScreen(Screen):
    pass

class ABScreen(Screen):
    pass

class LBScreen(Screen):
    pass

class ABBScreen(Screen):
    pass

class ESBScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.manager.current = 'main'

class WindowManager(ScreenManager):
    pass

class FloatLayout(BoxLayout):
    pass

kv = Builder.load_file('arellanomap.kv')

class ArellanoMap(App): 
    def build(self): 
        return kv

if __name__ == "__main__":
    ArellanoMap().run()

