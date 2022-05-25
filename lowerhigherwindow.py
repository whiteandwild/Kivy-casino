from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button 
from globals import *
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.graphics import Rectangle, Color , Line
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import RoundedRectangle
from kivy.uix.togglebutton import ToggleButton

class CardsBoard(BoxLayout):
    def __init__(self, **kwargs):
        self.size_hint = (1 , 0.5)
        super().__init__(**kwargs)
        with self.canvas:
            c = hex_to_kv("#01401C" , 0.8)
            Color(c[0], c[1], c[2], c[3])  # set the colour
 
            # Setting the size and position of canvas
            self.rect = RoundedRectangle(pos = self.pos,
                                  size =(self.width / 2.,
                                        self.height / 2.) ,radius = [10])
 
            # Update the canvas as the screen size change
            self.bind(pos = update_rect,
            size = update_rect)
    
        x = Box()
      
        self.add_widget(x)
   
        
class Box(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 7
        self.rows = 2
        self.pos_hint = {"top" :1}
        self.size_hint = (1 , 1)
        self.padding = "20dp"
        self.spacing = "10dp"
      
        
        with self.canvas:
            c = hex_to_kv("#01401C" , 0.8)
            Color(c[0], c[1], c[2], c[3])  # set the colour
 
            # Setting the size and position of canvas
            self.rect = RoundedRectangle(pos = self.pos,
                                  size =(self.width / 2.,
                                        self.height / 2.) ,radius = [10])
 
            # Update the canvas as the screen size change
            self.bind(pos = update_rect,
                  size = update_rect)
        for i in range(10):
            self.add_widget(BoxCards())
       
  
class BoxCards(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = "photos/sus_card.png" 
        self.allow_stretch = True
        self.keep_ratio = False        
        

class xyz(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint = (0.1,0.6)
        self.pos_hint = {"top" : 1}
        
        # a.add_widget(Button(size_hint = (0.8 , 0.3) ,))
        # a.add_widget(BoxCards(size_hint = (0.75 , 0.75)))
        # a.add_widget(Button(size_hint = (0.8 , 0.3)))
        with self.canvas.before:
            c = hex_to_kv("#435341" , 0.8)
            Color(c[0], c[1], c[2], c[3])
 
            self.rect = Rectangle(pos = self.pos,
                                  size =(self.width / 2.,
                                        self.height / 2.))
        self.bind(pos = update_rect,
                  size = update_rect)
        # self.add_widget(a)
       



class GameScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.add_widget(xyz())
        # with self.canvas.before:
        #     c = hex_to_kv("#FFFFFFF" , 0.8)
        #     Color(c[0], c[1], c[2], c[3])
 
        #     self.rect = Rectangle(pos = self.pos,
        #                           size =(self.width / 2.,
        #                                 self.height / 2.))
 
        #     self.bind(pos = self.update_rect,
        #           size = self.update_rect)
        
        a = AnchorLayout(anchor_x = "center" , anchor_y = "top")
        
        a.add_widget(RealgameScreen())
        self.add_widget(a)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
class RealgameScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.75, 1)
        self.padding = 5
        self.spacing = 5
        self.orientation = 'vertical'
        self.add_widget(CardShow())
        more = ToggleButton(size_hint = (0.4 , 1) ,background_down = "",background_normal = "", background_color = hex_to_kv("#0CF25D") , background_disabled_down = "" , text = "Wyższa" , font_size = "50dp")
        joker = ToggleButton(size_hint = (0.3 , 1), background_down = "", background_normal = "" , background_color = hex_to_kv("#F2A71B" , 1) , background_disabled_down = "" ,text = "Joker" , font_size = "50dp")
        less = ToggleButton(size_hint = (0.4 , 1) ,background_down = "", background_normal = "" , background_color = hex_to_kv("#F23005" , 1) , background_disabled_down = "" ,
        text = "Niższa" , font_size = "50dp")
        
        

        # more.state = 'down'

        more.bind(on_press=self.switch)
        joker.bind(on_press=self.switch)
        less.bind(on_press=self.switch)

        self.holder = BoxLayout(orientation = 'horizontal' , size_hint = (1 , 0.3) , spacing = 10 ,padding = (0 , 10 , 0 ,0))
        self.holder.add_widget(less)
        self.holder.add_widget(joker)
        self.holder.add_widget(more)




        self.add_widget(self.holder)
        # self.lockall()
    def switch(self , obj , *args):
       
        if obj.state == 'normal': 
            obj.background_color = (obj.background_color[0] , obj.background_color[1], obj.background_color[2] , 1)
            return
        for child in self.holder.children:
            child.background_color = (child.background_color[0] , child.background_color[1], child.background_color[2] , 1)
            child.state = 'normal'
        obj.state = 'down'
        obj.background_color = (obj.background_color[0] , obj.background_color[1], obj.background_color[2] , 0.5)
    def lockall(self):
        for child in self.holder.children:
            child.disabled = True

class CardShow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint = (1 , 0.75)
        self.spacing = 5
        self.padding = 20
        self.canvas_opacity = 0
        self.correct_color = "#337306"
        self.wrong_color = "#3232"
        with self.canvas.before:
                Color(rgba=hex_to_kv(self.correct_color , self.canvas_opacity)) #background for whole window
                self.rect = Rectangle(pos = self.pos,
                                  size =(self.width / 2.,
                                        self.height / 2.))
                Color((0,0,0,1))
                
                self.line = Line(width = 2 , rectangle = (self.x+5 , self.y , self.width , self.height ))
               
                self.bind(pos = update_line,size = update_line)
                
        
        # self.add_widget(Button())
        # self.add_widget(Button())
        self.add_widget(Image(size_hint = (0.4 , 1) , source = "photos/sus_card.png" , keep_ratio = True , allow_stretch = True ))
        self.add_widget(Image(size_hint = (0.4 , 1),source = "photos/sus_card.png" , keep_ratio = True , allow_stretch = True))

class LowerHigher(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'LowerHigher'
        self.bind(
                size=self._update_rect,
                pos=self._update_rect
            )

        with self.canvas.before:
                Color(rgb=hex_to_kv("#A6032F")) #background for whole window
                self.rect = Rectangle(
                    size=self.size,
                    pos=self.pos
                )
        
        
        x = BoxLayout(orientation = "vertical" ,padding = "5dp" ,spacing = 0,size_hint = (0.75 , 1))

        
        x.add_widget(CardsBoard())
        x.add_widget(GameScreen())
        self.add_widget(x)
        
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


def update_rect(obj, *args):
        obj.rect.pos = obj.pos
        obj.rect.size = obj.size
def update_line(obj , *args):
    obj.rect.pos = obj.pos
    obj.rect.size = obj.size
    obj.line.rectangle = (obj.x , obj.y , obj.width ,obj.height)
