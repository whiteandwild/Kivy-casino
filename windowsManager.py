# Kivy elements
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button 
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.screenmanager import FadeTransition
###   Set up starting window size
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '900')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.core.window import Window # Must be after config setup
# Screens
from lowerhigherwindow import LowerHigher
from menuwindow import MenuScreen
from BlackJackwindow import BlackJack

# Other
from globals import * 


class TestApp(App):

    def build(self):
        
        load_users_file()
        # fix_accounts()
        
        if not SearchAutoLogin():
            create_guest()

        self.sm = ScreenManager(transition=FadeTransition())

        self.screens = {0 : MenuScreen ,1 : LowerHigher}

        self.sm.add_widget(MenuScreen())
        # self.sm.add_widget(BlackJack())
        
        
        
        
       
      
        return self.sm

    def gen_screen(self, screen):
        
        x = eval(screen)()
        self.sm.add_widget(x)
        Clock.schedule_once( lambda z : self.change_screen(x.name), 0.5)

    def change_screen(self , screen , *args):
        self.sm.current = screen


if __name__ == '__main__':
    
    
    #lock window resizing under minimum size
    Window.minimum_width, Window.minimum_height = Window.size 
    
    TestApp().run()

    # After close:
    return_coins()
    save()


