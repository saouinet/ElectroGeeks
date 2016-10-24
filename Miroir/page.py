#!/usr/bin/python3

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Label
import paho.mqtt.client as mqtt
from kivy.uix.image import Image
from kivy.lang import Builder

mqttClient = mqtt.Client()


Affichage = Builder.load_string("""
BoxLayout:
	Label:
		text:"Temperature"
	Label:
		id:Valtemp
		text:"20 C"
	Image:
		id:ImgMeteo
		source:"images/pluie.png"
""")

def setTemp(val=20):
	global Affichage
	if "soleil" in Affichage.ids.ImgMeteo.source:
		Affichage.ids.ImgMeteo.source = "images/pluie.png"
	else:
		Affichage.ids.ImgMeteo.source = "images/soleil.png"

	Affichage.ids.Valtemp.text="%f00.1 C" %float(val)

def onMessage(mosq, obj, msg):
	setTemp(msg.payload)

mqttClient.on_message = onMessage
mqttClient.connect("localhost",1883,60)
mqttClient.subscribe("/maison/cuisine/temperature")

mqttClient.loop_start()

class PageApp(App):
	def build(self):
		return Affichage 
PageApp().run()
mqttClient.loop_stop()
