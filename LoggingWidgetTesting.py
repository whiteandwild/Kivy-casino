from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.checkbox import CheckBox
from kivy.config import Config
from kivy.graphics import Rectangle, Color , Line ,Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '900')

from kivy.core.window import Window # Must be after config setup


from globals import hex_to_kv

class TestApp(App):

    def build(self):
        
        root = BoxLayout(padding = ["30dp" , "30dp" , "30dp" ,"50dp"] , orientation = "vertical")
        with root.canvas.before:
                Color(rgb=hex_to_kv("#A6032F")) #background for whole window
                root.rect = Rectangle(size=root.size,pos=root.pos)
                root.bind(pos = update_rect,size = update_rect)
       
        main = BoxLayout(orientation = 'vertical' , size_hint = (None , None) , width = 600 , height = 400 , pos_hint = {"center_x" :0.5} )

        with main.canvas.before:
                Color(rgba=hex_to_kv("#FFFFFF" , 0.85)) #background for whole window
                main.rect = Rectangle(size=main.size,pos=root.pos)
                main.bind(pos = update_rect,size = update_rect)

        wtf = BoxLayout(size_hint = (0.3 ,1),pos_hint = {"center_x" : 0.5})
        wtf.add_widget(Button(pos_hint = {"center_y" : 1} , text = "Tak to ma byc"))

        main.add_widget(wtf)

        Creds = BoxLayout(orientation = "vertical" ,padding = ["10dp" , 0 , "10dp" , 0] ,spacing = "10dp")

        tmp = BoxLayout(size_hint =(1, 1))
        i = Image(source = "user.png",size_hint = (0.2 , 1) , keep_ratio = True , allow_stretch = True)
        tmp.add_widget(i)
        tmp.add_widget(TextInput(size_hint = (2,1) , hint_text = "Login"))
        with i.canvas.before:
                Color(rgb=hex_to_kv("#A6032F")) #background for whole window
                i.rect = Rectangle(size=i.size,pos=i.pos)
                i.bind(pos = update_rect,size = update_rect)



        Creds.add_widget(tmp)

        Credspart2 = BoxLayout(orientation = "vertical" , spacing = "20dp")
        tmp = BoxLayout(size_hint =(1, 1))

        i = Image(source = "user.png",size_hint = (0.2 , 1) , keep_ratio = True , allow_stretch = True)
        tmp.add_widget(i)

        with i.canvas.before:
                Color(rgb=hex_to_kv("#A6032F")) #background for whole window
                i.rect = Rectangle(size=i.size,pos=i.pos)
                i.bind(pos = update_rect,size = update_rect)
        
    
        tmp.add_widget(TextInput(size_hint = (2,1), hint_text = "password"))




        Creds.add_widget(tmp)

        RememberMe = BoxLayout(pos_hint = {'center_x' : 0.5} , size_hint = (0.75 , 0.8) , spacing = "5dp",padding = [0,"20dp" , 0 , 0])
        RememberMe.add_widget(ToggleButton(size_hint = (0.05 , 1)))
        
        self.r = Label(text = "Remember me" , halign = "left" ,valign="middle", size_hint = (1 , 1) , color = [0,0,0,1])
        RememberMe.add_widget(self.r)
        self.r.bind(size=self.r.setter('text_size'))  
        
        Credspart2.add_widget(RememberMe)
        




        Creds.add_widget(Credspart2)


        main.add_widget(Creds)

        wtf = BoxLayout(size_hint = (0.75 ,1),pos_hint = {"center_x" : 0.5} , spacing = "30dp")
        wtf.add_widget(Button(pos_hint = {"center_y" : 0} , text = "Tak to ma byc"))
        wtf.add_widget(Button(pos_hint = {"center_y" : 0} , text = "Tak to ma byc"))
        main.add_widget(wtf)
        
        
        root.add_widget(main)

        return root

def update_rect(obj, *args): # Update canvas rectangle for backgrounds

    obj.rect.pos = obj.pos
    obj.rect.size = obj.size
   


if __name__ == '__main__':
    
    

    Window.minimum_width, Window.minimum_height = Window.size 
    
    TestApp().run()


