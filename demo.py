#!/usr/bin/python3
import kivy
import paho.mqtt.client as mqtt
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder


#mqttClient = mqtt.Client()
#mqttClient.connect("192.168.0.47",1883,60)
#mqttClient.loop_start()

class Commande(BoxLayout):
	Builder.load_string("""
<Commande>:
	Slider:
		id:slider_id
		min:0
		max:50
		value:20
		on_value:root.OnSliderValueChange(slider_id.value)
	Label:
		id:Valtemp
		text: str(slider_id.value)
""")
	def __init__(self,**kwargs):
		super(Commande,self).__init__(**kwargs)
	def OnSliderValueChange(self,*args):
		text = str(*args)
		#mqttClient.publish("/maison/cuisine/temperature",text)
		print("/maison/cuisine/temperature",text)
	

class CommandeApp(App):
    def build(self):
        return Commande()


CommandeApp().run()
