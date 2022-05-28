# Kivy elements
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button 
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
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty

# Other
from globals import *

class LowerHigher(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'LowerHigher'
        self.bind(size=update_rect , pos=update_rect)

        ##########################
        with self.canvas.before:
                Color(rgb=hex_to_kv("#A6032F")) #background for whole window
                self.rect = Rectangle(size=self.size,pos=self.pos)
        ##########################

        
        
        Leftside = BoxLayout(orientation = "vertical" ,padding = "5dp" ,spacing = 0,size_hint = (0.75 , 1)) # Left window side  / cards and choose window
        Rightside = BoxLayout(size_hint = (0.25 , 1) , padding = "7dp" , orientation = 'vertical' , spacing = "5dp") # Right window side / timer and balance

        

        holder = BoxLayout(orientation = "horizontal" , size_hint = (1,1)) # Wrapper for whole screen
        holder.add_widget(Leftside)
        
        """
        left side
        """
        
        self.GS  = GameScreen() # cards choose window
        Leftside.add_widget(CardsBoard()) # cards board
        Leftside.add_widget(self.GS)

        
        self.GS.change_state(True) # Disable all buttons 

        """
        Right side
        """

        holder.add_widget(Rightside)

        self.timer = Timer()
        Rightside.add_widget(self.timer)
        Rightside.add_widget(Button()) # Temp object

        
        self.LoadStart() # Load start button 
    
        """
        end
        """
        self.add_widget(holder)
       
    
    def LoadTimer(self):
        self.timer.padding = "100dp"
        self.timer.add_widget(Label(font_size= "50dp" ,text = 'Time left:'))
        self.timer.add_widget(self.timer.clock)
        self.GS.change_state(False)

    def LoadStart(self):
        self.timer.padding = 0
        b = Button(text = "START" , font_size = "50dp")
        b.background_color = hex_to_kv("#F2A71B" , 0.6)
        b.background_normal = ""
        b.background_down = ""
        b.bind(on_press = lambda *args : self.swap(mode=1))
        self.timer.add_widget(b)

    def swap(self , mode): # Swaps timer elements
        self.timer.clear_widgets()
        if mode == 1:
            self.LoadTimer()
            self.timer.clock.start()

"""
Left side
"""   

class CardsBoard(BoxLayout):
    def __init__(self, **kwargs):
        self.size_hint = (1 , 0.5)
        super().__init__(**kwargs)
        ##########################
        with self.canvas:
            c = hex_to_kv("#01401C" , 0.8)
            Color(c[0], c[1], c[2], c[3])  # set the colour
 
            # Setting the size and position of canvas
            self.rect = RoundedRectangle(pos = self.pos , size =(self.width / 2. , self.height / 2.) ,radius = [10])
 
            # Update the canvas as the screen size change
            self.bind(pos = update_rect,size = update_rect)
        ##########################
        x = Box()
      
        self.add_widget(x)
   
        
class Box(GridLayout): # Cards displayer
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 7
        self.rows = 2
        self.pos_hint = {"top" :1}
        self.size_hint = (1 , 1)
        self.padding = "20dp"
        self.spacing = "10dp"
      
        ##########################
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
        ##########################

        for i in range(10):
            card = BoxCard()
            card.source = "photos/sus_card.png"  # Blank card
            self.add_widget(card)
       
  
class BoxCard(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_stretch = True
        self.keep_ratio = False        
        

class GameScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.RGS = BoxLayout()
        self.RGS.size_hint = (0.75, 1)
        self.RGS.padding = 5
        self.RGS.spacing = 5
        self.RGS.orientation = 'vertical'

        a = AnchorLayout(anchor_x = "center" , anchor_y = "top") # Wrapper

        """
        Buttons
        """
        more = ToggleButton(size_hint = (0.4 , 1) ,background_down = "",background_normal = "", background_color = hex_to_kv("#0CF25D") , background_disabled_down = "" , text = "Wyższa" , font_size = "50dp")
        
        joker = ToggleButton(size_hint = (0.3 , 1), background_down = "", background_normal = "" , background_color = hex_to_kv("#F2A71B" , 1) , background_disabled_down = "" ,text = "Joker" , font_size = "50dp")

        less = ToggleButton(size_hint = (0.4 , 1) ,background_down = "", background_normal = "" , background_color = hex_to_kv("#F23005" , 1) , background_disabled_down = "" ,
        text = "Niższa" , font_size = "50dp")

        more.bind(on_press=self.switch)
        joker.bind(on_press=self.switch)
        less.bind(on_press=self.switch)
        """
        Add buttons
        """
        self.RGS.holder = BoxLayout(orientation = 'horizontal' , size_hint = (1 , 0.3) , spacing = 10 ,padding = (0 , 10 , 0 ,0))
        self.RGS.holder.add_widget(less)
        self.RGS.holder.add_widget(joker)
        self.RGS.holder.add_widget(more)



        self.RGS.add_widget(CardShow())
        self.RGS.add_widget(self.RGS.holder)

        a.add_widget(self.RGS)
        self.add_widget(a)

    def switch(self , obj , *args): # Only 1 button pressed at a clip
       
        if obj.state == 'normal': # Toggle normal on double click at the same button
            obj.background_color = (obj.background_color[0] , obj.background_color[1], obj.background_color[2] , 1)
            return

        # Apply normal state for all
        for child in self.RGS.holder.children:
            child.background_color = (child.background_color[0] , child.background_color[1], child.background_color[2] , 1)
            child.state = 'normal'

        obj.state = 'down' # Apply down state for pressed button
        obj.background_color = (obj.background_color[0] , obj.background_color[1], obj.background_color[2] , 0.5)

    def change_state(self , new_state): # Disable / Enable all buttons
        for child in self.RGS.holder.children:
            child.disabled = new_state


class CardShow(BoxLayout): # Show 2 cards 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint = (1 , 0.75)
        self.spacing = 5
        self.padding = 20

        self.canvas_opacity = 0
        self.correct_color = "#337306"
        self.wrong_color = "#3232"

        ##########################
        with self.canvas.before:
                Color(rgba=hex_to_kv(self.correct_color , self.canvas_opacity)) #background for whole window
                self.rect = Rectangle(pos = self.pos,
                                  size =(self.width / 2.,
                                        self.height / 2.))
                Color((0,0,0,1))
                
                self.line = Line(width = 2 , rectangle = (self.x+5 , self.y , self.width , self.height ))
               
                self.bind(pos = update_line,size = update_line)
        ##########################
        
        self.add_widget(Image(size_hint = (0.4 , 1) , source = "photos/sus_card.png" , keep_ratio = True , allow_stretch = True ))
        self.add_widget(Image(size_hint = (0.4 , 1),source = "photos/sus_card.png" , keep_ratio = True , allow_stretch = True))


"""
Right side
"""

class Timer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_hint = {"top" : 1}
        self.orientation = "vertical" 
        self.padding = "100dp" 
        self.spacing = 5
        self.size_hint = (1 , 0.5)
        ##########################
        with self.canvas.before:
            Color((0,0,0,1))
            self.line = Line(width = 1 , rectangle = (self.x+5 , self.y , self.width , self.height ))
               
            self.bind(pos = self.update_border,size = self.update_border)
        ##########################
        self.clock = IncrediblyCrudeClock()

    def update_border(self , *args):
        self.line.rectangle = (self.x , self.y , self.width ,self.height)

        
class IncrediblyCrudeClock(Label): # Stolen from stackOverflow 
    a = NumericProperty(15)  # Seconds
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size= "50dp"

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)
        
        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "0"

        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def stop(self):
        self.anim.stop()

    def on_a(self, instance, value):
        self.text = str(round(value, 1))


def update_rect(obj, *args): # Update canvas rectangle for backgrounds
        obj.rect.pos = obj.pos
        obj.rect.size = obj.size

def update_line(obj , *args): # Update border pos for line and pos for rectangle
    obj.rect.pos = obj.pos
    obj.rect.size = obj.size
    obj.line.rectangle = (obj.x , obj.y , obj.width ,obj.height)


