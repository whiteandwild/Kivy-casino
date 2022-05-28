from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from globals import *

class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'mainmenu'
        self.add_widget(Button(text="siema" , background_color =hex_to_kv("#A6032F") ))
  
