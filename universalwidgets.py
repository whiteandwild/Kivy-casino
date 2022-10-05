from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Color , RoundedRectangle , Line
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.animation import Animation
from globals import *
from kivy.uix.boxlayout import BoxLayout

class BetterInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.halign = "left"
        self.font_size = "20dp"
        self.background_color = [1,1,1,1] 
        self.background_normal =  'photos/white.png'
        self.background_active ='photos/white.png'
        self.font_name = "RobotoMono-Regular"
        self.ispasswd = False
    def on_text(self , *args):
       
        self.text = self.text.replace(" " , "")
        
        if not self.ispasswd:
            self.text = self.text.lower()

        if len(self.text) >= 15:
            self.text = self.text[:15]

        
    def on_size(self, instance, value):
        self.padding_y =  [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]

def update_rect(obj, *args): # Update canvas rectangle for backgrounds

    obj.rect.pos = obj.pos
    obj.rect.size = obj.size

def add_bg(obj , color , opacity):
    with obj.canvas.before:
            Color(rgba = hex_to_kv(color , opacity))
            obj.rect = Rectangle(size=obj.size,pos=obj.pos)
            obj.bind(pos = update_rect,size = update_rect)
def add_border(obj , color , width):
    with obj.canvas.before:
        Color(rgba = hex_to_kv(color))
        obj.line = Line(width = width , rectangle = (obj.x, obj.y , obj.width , obj.height ))
        obj.bind(pos = update_line,size = update_line)

def update_line(obj , *args): # Update border pos for line and pos for rectangle

    if getattr(obj , "rect" , False):
        obj.rect.pos = obj.pos
        obj.rect.size = obj.size
    obj.line.rectangle = (obj.x , obj.y , obj.width ,obj.height)

from kivy.properties import BooleanProperty, ObjectProperty
from kivy.core.window import Window

class HoverBehavior(object):
    """Hover behavior.
    :Events:
        `on_enter`
            Fired when mouse enter the bbox of the widget.
        `on_leave`
            Fired when the mouse exit the widget 
    """

    hovered = BooleanProperty(False)
    border_point= ObjectProperty(None)
    '''Contains the last relevant point received by the Hoverable. This can
    be used in `on_enter` or `on_leave` in order to know where was dispatched the event.
    '''

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        #Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            #We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass

from kivy.factory import Factory
Factory.register('HoverBehavior', HoverBehavior)


class HoverToggleButton(HoverBehavior ,ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self , *args):
        if not self.disabled: 
            Window.set_system_cursor('hand')
    def on_leave(self):
        Window.set_system_cursor('arrow')
class HoverButton(HoverBehavior ,Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self , *args):
        if not self.disabled: 
            Window.set_system_cursor('hand')
    def on_leave(self):
        Window.set_system_cursor('arrow')
        
class RoundedButton(HoverButton , Button):
    def __init__(self,r,c, **kwargs):
        super().__init__(**kwargs)
        self.background_color = c
        self.background_normal = ""
    
        # self.border = [r]
        # with self.canvas.before:
        #     Color(rgba = c)
        #     self.rect = RoundedRectangle(size = self.size , pos = self.pos , radius = [r])
        #     self.bind(pos = update_rect,size = update_rect)
class LeftLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "RobotoMono-Regular"
    def on_size(self , *args):
        self.text_size = self.size

class StatsLabel(LeftLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_size(self, *args):
        # self.text_size = self.size
        self.font_size = self.width /16
class BettingWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        Bet = BoxLayout(size_hint = (1 , 0.75) , pos_hint = {"center_y" : 0.5} , orientation = "vertical")
        ##########################
        with Bet.canvas.before:
            
            c = hex_to_kv("#01401C" , 0.8)
            Color(c[0], c[1], c[2], c[3])  # set the colour
 
            # Setting the size and position of canvas
            Bet.rect = RoundedRectangle(pos = Bet.pos , size =(Bet.width / 2. , Bet.height / 2.) ,radius = [10])
 
            # Update the canvas as the screen size change
            Bet.bind(pos = update_rect,size = update_rect)
        ##########################

        self.creds = Credentials()

        self.button_mode = 0 # 0 bet / 1 leave
        
        self.BetButton = BoxLayout(size_hint = (1 , 0.5) , padding = "13dp")
        self.b = HoverButton(size_hint = (0.8 , 1) , text = "BET" , font_size = "70dp" ,background_disabled_normal = "" , background_normal = '', background_color = hex_to_kv("#DED5CA"))
        self.b.bind(on_press = self.button_action)

        self.BetAmount = Betting()

        self.BetButton.add_widget(self.b)

        Bet.add_widget(self.creds)
    
        Bet.add_widget(self.BetAmount)
        Bet.add_widget(self.BetButton)
        self.add_widget(Bet)

    def lock_bet(self):
        self.b.disabled = not self.b.disabled

    def leave_button(self):
        self.b.text = "LEAVE"
        self.button_mode = 1

    def bet_button(self):
        self.b.text = "BET"
        self.button_mode = 0
    
    def button_action(self , *args):
        return
        



class Credentials(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = "15dp"
        self.spacing = "2dp"
        self.size_hint = (1 , 0.6)
        name = BoxLayout(size_hint = (1 , 0.2))
        balance = BoxLayout(size_hint = (1 , 0.2))
        ##########################
        with name.canvas.before:
            
            c = hex_to_kv("#FFFFFF" , 1)
            Color(c[0], c[1], c[2], c[3])  # set the colour
 
            # Setting the size and position of canvas
            name.rect = RoundedRectangle(pos = name.pos , size =(name.width / 2. , name.height / 2.) , radius = [8, 8 , 0 , 0])
 
            # Update the canvas as the screen size change
            name.bind(pos = update_rect,size = update_rect)
        ##########################

        ##########################
        with balance.canvas.before:
            
            c = hex_to_kv("#FFFFFF" , 1)
            Color(c[0], c[1], c[2], c[3])  # set the colour
 
            # Setting the size and position of canvas
            balance.rect = RoundedRectangle(pos = balance.pos , size =(balance.width / 2. , balance.height / 2.) , radius = [0 , 0, 8, 8])
 
            # Update the canvas as the screen size change
            balance.bind(pos = update_rect,size = update_rect)
        ##########################

        name.add_widget(Label(text = storage.current_user.user_name , font_size = "25dp" , color = (0 , 0, 0 , 1)))

        self.b = Label(text = str(int(storage.current_user.balance)) + " Coins" , font_size = "25dp" , color = (0 , 0, 0 , 1))
        balance.add_widget(self.b)

        self.add_widget(name)
        self.add_widget(balance)
    def update_balance(self , new_value):
    

        def p(self , *args):
            obj = args[0]
            obj.b.text = f'{str(int(obj.prev))} Coins'
        self.prev = int(self.b.text.split()[0])
        if self.prev == new_value : return
        dur = 1 if abs(self.prev-new_value) < 10000 else 2

        anim = Animation(prev = new_value , duration = dur)
        anim.bind(on_progress = p)
        anim.start(self)

        self.b.text = f'{str(int(self.prev))} coins'

class Betting(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = "13dp"
        
        
        self.orientation = 'vertical'
    
        upp = BoxLayout(size_hint = (1,0.3) , pos_hint = {"center_x" : 0.5} , spacing = 1)
        down = BoxLayout(size_hint = (1,0.3) , pos_hint = {"center_x" : 0.5} , spacing = 1)
        self.CoinsInput = AmountInput()

        upp.add_widget(HoverButton(font_size = "17dp" , background_color = hex_to_kv("#A14E0B") , background_normal = "" , text = "10000" , on_press = lambda x : self.CoinsInput.add_coins(10000)))
        upp.add_widget(HoverButton(font_size = "17dp",background_color = hex_to_kv("#E0801E" ) , background_normal = "" ,text = "1000" , on_press = lambda x : self.CoinsInput.add_coins(1000)))
        upp.add_widget(HoverButton(font_size = "17dp",background_color = hex_to_kv("#ED861F") , background_normal = "" ,text = "100" , on_press = lambda x : self.CoinsInput.add_coins(100)))
        upp.add_widget(HoverButton(font_size = "17dp",background_color = hex_to_kv("#F2BE22") , background_normal = "" ,text = "10" , on_press = lambda x : self.CoinsInput.add_coins(10)))

        down.add_widget(HoverButton(font_size = "17dp" , background_color = hex_to_kv("#F2BE22") , background_normal = "",text = "0" , on_press = lambda x : self.CoinsInput.mul_coins(0)))
        down.add_widget(HoverButton(font_size = "17dp" , background_color = hex_to_kv("#1D594E") , background_normal = "",text = "1/2x" , on_press = lambda x : self.CoinsInput.mul_coins(0.5)))
        down.add_widget(HoverButton(font_size = "17dp" , background_color = hex_to_kv("#F28705") , background_normal = "",text = "2x" , on_press = lambda x : self.CoinsInput.mul_coins(2)))
        down.add_widget(HoverButton(font_size = "17dp" , background_color = hex_to_kv("#F23030") , background_normal = "",text = "Max" , on_press = lambda x : self.CoinsInput.max_coins()))
        
        self.add_widget(upp)
       
        self.add_widget(self.CoinsInput)
        self.add_widget(down)


class AmountInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input_filter = 'int' 
        self.hint_text = "0"
        self.text = '0'
        self.font_size = "30dp" 
        self.halign = "center" 
        self.valign ='center'
        self.background_normal =  'photos/white.png'
        self.background_active ='photos/white.png'
        self.size_hint = (1, 0.5)
        
        self.multiline = False
        self.bind(on_touch_down = self.mouseclick)

    def add_coins(self , to_add):
        tmp = int(self.text)
        if self.mouse == "left":
            tmp += to_add
        if self.mouse == "right":
            tmp -= to_add
        if tmp > 999999 :
            tmp = 999999
        elif tmp < 0:
            tmp = 0
        self.text = str(tmp)
    def mul_coins(self , mul):
        
        tmp = int(self.text)
        tmp *= mul
        tmp = int(tmp)
        if tmp > 999999 :
            tmp = 999999
        self.text = str(tmp)
    def max_coins(self):
        self.text = str(storage.current_user.balance)
    def on_size(self, instance, value):
        self.padding_y =  [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
    def on_text(self, instance, value):
        
        if len(self.text) >= 7:
            self.text = self.text[:7]
    def mouseclick(self,instance ,touch):
        self.mouse = touch.button
            
