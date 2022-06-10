# Kivy elements
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

# Other
from globals import *




class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'mainmenu'

        self.holder = BoxLayout(orientation = "vertical")
        self.games = GridLayout(rows = 1 , cols = 3 , padding = "15dp" , spacing = "15dp")
        

        self.games.add_widget(Button(text="Lower Higher" , on_press = lambda x: App.get_running_app().gen_screen('LowerHigher')))
        self.games.add_widget(Button())
        self.games.add_widget(Button())

        up = BoxLayout()

        up.add_widget(Button(size_hint = (0.7 , 1)))
        up.add_widget(Button(size_hint = (0.3 , 1)))

        self.holder.add_widget(up)
        self.holder.add_widget(self.games)

        self.add_widget(self.holder)

  