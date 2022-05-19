from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button 
from globals import *
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.graphics import Rectangle, Color
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import RoundedRectangle

class CardsBoard(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.anchor_x = "left"
        self.anchor_y = "top"
        self.padding = "5dp"
        x = Box()
        self.add_widget(x)
class xyz(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation ='tb-rl' 
        self.size_hint = (0.72 , 0.55)
        
        with self.canvas:
            c = hex_to_kv("#FFFFFFF" , 0.8)
            Color(c[0], c[1], c[2], c[3])
 
            self.rect = Rectangle(pos = self.pos,
                                  size =(self.width / 2.,
                                        self.height / 2.))
 
     
            self.bind(pos = self.update_rect,
                  size = self.update_rect)
        
       

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
class GameScreen(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.anchor_x = "left"
        self.anchor_y = "bottom"
        self.padding = ["20dp" , 0 ,0 ,"20dp"]
        self.add_widget(xyz())
       
        
       
    
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
        k = AnchorLayout(anchor_x = "left",anchor_y = "bottom")
        
        x = BoxLayout(orientation = "vertical" , size_hint = (0.75 , 1))

        
        x.add_widget(CardsBoard())
        x.add_widget(GameScreen())
        k.add_widget(x)
        self.add_widget(k)

        # self.add_widget(CardsBoard())
        # self.add_widget(GameScreen())
        
        
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

        
class Box(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 7
        self.rows = 2
        self.size_hint = (0.75 , 0.4)
        self.padding = "20dp"
        self.spacing = "20dp"
      
        
        with self.canvas:
            c = hex_to_kv("#01401C" , 0.8)
            Color(c[0], c[1], c[2], c[3])  # set the colour
 
            # Setting the size and position of canvas
            self.rect = RoundedRectangle(pos = self.pos,
                                  size =(self.width / 2.,
                                        self.height / 2.) ,radius = [10])
 
            # Update the canvas as the screen size change
            self.bind(pos = self.update_rect,
                  size = self.update_rect)
        for i in range(10):
            self.add_widget(BoxCards())
       
    # update function which makes the canvas adjustable.
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
class BoxCards(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = "photos/red_joker.png" 
        self.allow_stretch=True
        
