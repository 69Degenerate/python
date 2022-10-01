import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window

class FirstWindow(Screen):
    def on(self):
            self.ids.but1.font_size=25
    def off(self):
            self.ids.but1.font_size=30

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
	pass

class demo(App):
    def build(self):
         return Builder.load_file("text.kv")
demo().run()