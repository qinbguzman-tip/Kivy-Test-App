from kivy.app import App
from kivy.uix.button import Button
import firebase_admin

class MainApp(App):
  def build(self):
    return Button(text="Hello World")
    
MainApp().run()