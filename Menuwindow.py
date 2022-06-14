# Kivy elements
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
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

        self.login = BetterInput(multiline = False , size_hint = (0.75 , 0.3) , pos_hint = {"center_x" : 0.5})
        self.password = BetterInput(multiline = False , size_hint = (0.75 , 0.3) , pos_hint = {"center_x" : 0.5} , password = True)

        Loggingbox = BoxLayout(orientation = "vertical" , padding = ["20dp" , "50dp" ,"20dp" ,"50dp"] , spacing = "20dp")
        LoggingButtons = BoxLayout()

        Loggingbox.add_widget(self.login)
        Loggingbox.add_widget(self.password)
        Loggingbox.add_widget(LoggingButtons)

        LoggingButtons.add_widget(Button(text = "Log in" , size_hint = (1 , 0.5) , on_press = self.Dologin))
        LoggingButtons.add_widget(Button(text = "Sign up" , size_hint = (1 , 0.5) , on_press = self.Dosignup))

        up.add_widget(Button(size_hint = (0.7 , 1)))
        up.add_widget(Loggingbox)

        self.holder.add_widget(up)
        self.holder.add_widget(self.games)

        self.add_widget(self.holder)

    def Dologin(self , *args):
        
        name = self.login.text
        passwd = self.password.text

        if name == "" or passwd == "":return


        response = login(user_name=name , password=passwd)

        print(response)

        if response == True :
            storage.current_user = storage.accounts[name]
    
    def Dosignup(self ,*args):
        
        name = self.login.text
        passwd = self.password.text

        if name == "" or passwd == "":return

        response = create_account(user_name=name , password=passwd)

        print(response)

    

class BetterInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.halign = "center"
        self.font_size = "20dp"

    def on_text(self , *args):
       
        self.text = self.text.replace(" " , "")
        self.text = self.text.lower()

        if len(self.text) >= 15:
            self.text = self.text[:15]

        
    def on_size(self, instance, value):
        self.padding_y =  [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]