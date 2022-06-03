# Kivy elements
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button 
from kivy.config import Config

###   Set up starting window size
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '900')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.core.window import Window # Must be after config setup
# Screens
from lowerhigherwindow import LowerHigher
from Menuwindow import MenuScreen

# Other
from globals import * 




class TestApp(App):

    def build(self):
        
        sm = ScreenManager()

        """
        Window priority system for easier ui programming
        """
        screens = {1 : MenuScreen ,0 : LowerHigher}
        for s in sorted(screens): sm.add_widget(screens[s]())

        return sm

if __name__ == '__main__':
    
    
    #lock window resizing under minimum size
    Window.minimum_width, Window.minimum_height = Window.size 
    
    TestApp().run()