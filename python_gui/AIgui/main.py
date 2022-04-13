import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 1)

class CalcGridLayout(GridLayout):
	def calculate(self, calculation):
		if calculation:
			try:
				# Solve formula and display it in entry
				# which is pointed at by display
				self.display.text = str(calculation)
			except Exception:
				self.display.text = "Error"

	def cal(self, con):
		if con:
			try:
				self.display.text = str(con)
                
			except Exception:
				self.display.text = "Error"




class CalculatorApp(App):
	def build(self):
		return CalcGridLayout()
        
calcApp = CalculatorApp()
calcApp.run()
