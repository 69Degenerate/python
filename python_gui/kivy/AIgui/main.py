import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 1)

class CalcGridLayout(GridLayout):

	def cal(self, con):
		return str(con)
	
	def callback(self,call):
		self.greet.text = str(call)




class CalculatorApp(App):
	def build(self):
		return CalcGridLayout()
        
calcApp = CalculatorApp()
calcApp.run()
