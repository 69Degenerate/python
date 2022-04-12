
from kivy.app import App as a
from kivy.uix.button import Button as b
from kivy.uix.widget import Widget


class game(Widget):
    pass
# class bu(b):
#     def __init__(self, **kwargs):
#         super(bu,self).__init__(**kwargs)
#         self.text='hello'
#         self.pos=(15,150)
#         self.size=(200,200)
#         self.size_hint=(None,None)


class app(a):
    def build(self):
        return game()



if __name__=='__main__':
    app().run()