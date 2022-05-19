from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button 
from globals import * 
from lowerhigherwindow import LowerHigher
class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'mainmenu'
        
        self.add_widget(Button(text="siema" , background_color =hex_to_kv("#A6032F") ))
    pass

class SettingsScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()

        screens = {1 : MenuScreen ,0 : LowerHigher}
        for s in sorted(screens):
            
            sm.add_widget(screens[s]())
       
        
        
       
        

        return sm

if __name__ == '__main__':
    TestApp().run()