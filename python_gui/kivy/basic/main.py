
from kivy.app import App as a
from kivy.uix.button import Button as b
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput


class game(Widget):
    def textt(self,call):
        self.leb.text=str(call)


class app(a):
    def build(self):
        return game()



if __name__=='__main__':
    app().run()