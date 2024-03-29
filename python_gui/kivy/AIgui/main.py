import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from ast import While
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import googletrans



Config.set('graphics', 'resizable', 1)

engine =pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[-1].id)

class CalcGridLayout(GridLayout):
		

	def callback(self,call):
		self.greet.text = str(call)
		
	def speak(self,audio):
		engine.say(audio)
		engine.runAndWait()

	def wishme(): #will greet you according to time of the day
		hour = int(datetime.datetime.now().hour)
		speak("hello sir .")    
		if hour>=0 and hour<12:         # if time is between 0 to 12 in the morning
			speak("Good Morning!")

		elif hour>=12 and hour<18:      #if time is between 12 to 6
			speak("Good Afternoon!")
		else:
			speak("Good Evining!")         
		speak("i am friday, how may i help you?")         

	def listen():		
		k = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening....")
			k.pause_threshold == 1
			audio=k.listen(source)
		try:
			print("Recognizing......")
			speak("Recognizing......")
			query=k.recognize_google(audio, language='mar-in')    
			print("user said: ",{query},"\n")

		except Exception as e:
			print("Say that again please....")
			speak("Say that again please....")
			return "None"
		return query

	def cal(self,con):		
		# if __name__ == "__main__":
		# 	wishme()
		# 	while True:
		query=str(con)
				
		if 'wikipedia' in query:
				try:
					self.speak('searching Wikipedia....')
					query= query.replace("wikipedia","")
					results = wikipedia.summary(query,sentences=1)
					self.speak("Acording To Wikipedia")
					self.speak(results)
				except Exception as e:
					print(e)
					self.speak("sorry boss ,i am not able get any appropriate result from wikipedia")
		
		if 'time' in query:
				strtime= datetime.datetime.now().strftime("%H:%M:%S")
				print(strtime)
				self.speak(f"The time is {strtime}")
				print(f"The time is {strtime}")
		if 'youtube' in query:
				webbrowser.open('https://youtu.be/iik25wqIuFo')
		if'who are you' in query:
				self.speak('I am veronica, i am A.i system of created by self,with love of you, i m a ho,such a disspointment to this dammed world')
		
		

class CalculatorApp(App):
	def build(self):
		return CalcGridLayout()
        
calcApp = CalculatorApp()
calcApp.run()
