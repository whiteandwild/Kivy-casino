from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.checkbox import CheckBox
from kivy.config import Config
from kivy.graphics import Rectangle, Color , Line 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image

from globals import hex_to_kv


class test1(BoxLayout):
    def __init__(self, **kwargs):
         super().__init__(**kwargs)
         self.size_hint = (0.5 , 1)
         self.pos_hint = {"center_x" : 0.5}
         self.add_widget(test2())

         

         self.add_widget(Button())

class test2(ToggleButton):
    def __init__(self, **kwargs):
         super().__init__(**kwargs)
         self.size_hint = (0.5 , 1)
         self.color = [1,1,1,1]
         


class test3(Label,ButtonBehavior):
    def __init__(self, **kwargs):
         super().__init__(**kwargs)
         self.text_size = self.size
         self.font_size = "13dp"
         self.color = [1,1,1,1]
         self.text = "Kurwa"
         self.halign = 'center'
         self.valign = 'center'
        
    def on_size(self , *args):
        self.text_size = self.size
class TestApp(App):

    def build(self):
        
        root = BoxLayout(size_hint = (1,1) , orientation = "vertical")
        with root.canvas.before:
                Color(rgba=hex_to_kv("#FFFFFF" , 0.85)) #background for whole window
                root.rect = Rectangle(size=root.size,pos=root.pos)
                root.bind(pos = update_rect,size = update_rect)

        safasf = BoxLayout(orientation = "vertical" , padding = "30dp")

        tmp = BoxLayout(size_hint =(1, 0.2))

        tmp.add_widget(Image(source = "user.png",size_hint = (0.2 , 0.5) , keep_ratio = True , allow_stretch = True))
        tmp.add_widget(TextInput(size_hint = (2,0.5) , hint_text = "Login"))

        safasf.add_widget(tmp)

        tmp = BoxLayout(size_hint =(1, 0.2))

        tmp.add_widget(Image(source = "passwd.png",size_hint = (0.2 , 0.5) ,keep_ratio = True ,allow_stretch = True))
        tmp.add_widget(TextInput(size_hint = (2,0.5), hint_text = "password"))

        safasf.add_widget(tmp)
        root.add_widget(safasf)
        root.add_widget(Button())
       

        return root
def update_rect(obj, *args): # Update canvas rectangle for backgrounds

    obj.rect.pos = obj.pos
    obj.rect.size = obj.size
   
if __name__ == '__main__':
    
    

    
    TestApp().run()