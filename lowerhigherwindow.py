# Kivy elements
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.graphics import Rectangle, Color , Line , Callback
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import RoundedRectangle
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty , ListProperty , ColorProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup

# Other

from cards import *
from globals import *

class LowerHigher(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.cards = generate_cards()
        self.name = 'LowerHigher'
        self.playing = False
        self.bind(size=update_rect , pos=update_rect)
        
        ##########################
        with self.canvas.before:
                Color(rgb=hex_to_kv("#A6032F")) #background for whole window
                self.rect = Rectangle(size=self.size,pos=self.pos)
        ##########################

        
        
        self.Leftside = BoxLayout(orientation = "vertical" ,padding = "5dp" ,spacing = 0,size_hint = (0.75 , 1)) # Left window side  / cards and choose window
        self.Rightside = BoxLayout(size_hint = (0.25 , 1) , padding = "7dp" , orientation = 'vertical' , spacing = "5dp") # Right window side / timer and balance

        

        holder = BoxLayout(orientation = "horizontal" , size_hint = (1,1)) # Wrapper for whole screen
        holder.add_widget(self.Leftside)
        
        """
        left side
        """
        
        self.GS  = GameScreen() # cards choose window
        self.CB = CardsBoard()
        self.Leftside.add_widget(self.CB) # cards board
        self.Leftside.add_widget(self.GS)

        
        self.GS.change_state(True) # Disable all buttons 

        """
        Right side
        """

        holder.add_widget(self.Rightside)

        self.timer = Timer()
        self.BW = BettingWindow()
        self.Rightside.add_widget(self.timer)
        self.Rightside.add_widget(self.BW)

        
        self.LoadStart() # Load start button 
    
        """
        end
        """
        self.add_widget(holder)
        
        self.Buttons = BoxLayout(size_hint = (None , None) , size = (150 , 75) , pos_hint = {"right" : 1} , spacing = 5 , padding = 5)
        self.Buttons.add_widget(Button(text = "INFO" , background_color = hex_to_kv("#DED5CA") , background_normal = ""))
        self.Buttons.add_widget(Button(text = "MENU" , background_color = hex_to_kv("#DED5CA") , background_normal = "" , on_press = self.change_to_menu))

        self.add_widget(self.Buttons)
        

        

        storage.c_root = self
    
    def on_leave(self, *args):
        return_coins()
        self.manager.remove_widget(self)
        

    def LoadTimer(self):
        self.timer.padding = "100dp"
        self.timer.clear_widgets()
        self.timer.add_widget(self.timer.clock)
        self.timer.clock.init()
        self.GS.change_state(False)

    def LoadStart(self):
        self.timer.padding = 0
        b = Button(text = "START" , font_size = "50dp" , on_press = self.startRound)
        b.background_color = hex_to_kv("#DED5CA" , 0.9)
        b.background_normal = ""
        b.background_down = ""

        self.timer.add_widget(b)

    def swap(self , mode): # Swaps timer elements
        self.timer.clear_widgets()
        if mode == 1:

            self.LoadTimer()
            self.timer.clock.init()
            self.timer.clock.anim.bind(on_complete = self.finishRound)
           

        elif mode == 0:
            self.LoadStart()

    """
    Round Start / End 
    """
    def startRound(self ,is_new_game = True, *args):
        self.playing = True
        
        if is_new_game:

            self.currentCards = self.cards[:]
            self.ThrownCards = []
            self.CB.box.clear_self()
            self.currentStreak = 1

            for i in range(10): #roll 10 cards to throw
                tmp = choose_random_card(self.currentCards)
                self.currentCards.remove(tmp)
                self.CB.box.add_card(tmp.src)

            self.CardA = choose_random_card(self.currentCards)
            self.currentCards.remove(self.CardA)
            
        storage.c_root.GS.Betshow.Update_strike_bonus(self.currentStreak)
        self.swap(1)
        self.timer.clock.start()

        self.CardB = choose_random_card(self.currentCards)
        self.currentCards.remove(self.CardB)
        self.GS.Cardshow.show_card(self.CardA.src , 0)

        self.GS.roundStart()
        self.BW.BetButton.disabled = False
    
    def finishRound(self , animation, incr_crude_clock):

        def part2(*args):
            self.GS.Cardshow.show_card(self.CardB.src , 1) # Show second card
            
            if result == True:
                self.GS.Cardshow.animate_background(0)
                self.timer.clock.text = "You win\n:)"
                
                self.currentStreak *= 1.5
                
                storage.current_bet = 0
                make_bet(new_bet)

                if self.currentStreak > 3.5:
                    return_coins()
                    
                    Clock.schedule_once(reset_widgets , 3)

                Clock.schedule_once(winning , 3)
                
                return
               
            
            elif result == False:
                self.GS.Cardshow.animate_background(1)
                self.timer.clock.text ="You lose\n:("
                
                self.currentStreak = 1
                Clock.schedule_once(reset_widgets , 3)
            else:
                self.BW.creds.update_balance(return_coins())
                Clock.schedule_once(reset_widgets , 1)
            

        def reset_widgets(*args):
            self.swap(0)
            self.BW.creds.update_balance(storage.current_user.balance)
            self.CB.box.generate_blank_cards()
            self.GS.Cardshow.reset()
            self.GS.roundStart()
            self.GS.change_state(True)
            self.BW.BetButton.disabled = False
            self.BW.bet_button()
            storage.c_root.GS.Betshow.Reset_bet()
            storage.c_root.GS.Betshow.Update_strike_bonus(1)
            
            
            

        def winning(*args):
            self.CB.box.add_card(self.CardA.src)
            self.CardA = self.CardB # Replace cards
            self.GS.Cardshow.reset()
            self.BW.leave_button()
            self.startRound(is_new_game = False)
            

            storage.c_root.GS.Betshow.Reset_bet()
            storage.c_root.GS.Betshow.Change_bet(new_bet)
        
       
        self.playing = False
        self.timer.clock.text = "End"
        self.GS.roundEnd_disable()
        self.BW.BetButton.disabled = True # Lock betting

        x = self.GS.choosed # User input
        result = None
        new_bet = 0

        if x != None: 
            result = compare_cards(self.CardA , self.CardB , x)
            if storage.current_bet == 0: result = None
            else:
              new_bet = bet_end(result , self.currentStreak)
        

        self.GS.Cardshow.resize_card_A()

        Clock.schedule_once(part2 , 1)

    def change_to_menu(self , *args):
        # x = Popup(content=Label(text='Hello world'))
        # x.open()
        self.manager.current = 'mainmenu'


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
        self.box = Box()
      
        self.add_widget(self.box)
   
        
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

        self.generate_blank_cards()
        
            
    def add_card(self,src):
        card = BoxCard()
        card.source = src  # Blank card
        card.keep_ratio = True
        card.allow_stretch = True
        self.add_widget(card)
    
    def generate_blank_cards(self):
        self.clear_widgets()
        for i in range(10):
            card = BoxCard()
            card.source = "photos/sus_card.png"  # Blank card
            card.keep_ratio = True
            card.allow_stretch = True
            self.add_widget(card)

    def clear_self(self):
        self.clear_widgets()
  
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
        self.choosed = None

        a = AnchorLayout(anchor_x = "center" , anchor_y = "top") # Wrapper

        """
        Buttons
        """
        more = ToggleButton(size_hint = (0.4 , 1) ,background_down = "",background_normal = "", background_color = hex_to_kv("#0CF25D") , background_disabled_down = "" , text = "Higher" , font_size = "50dp")
        
        joker = ToggleButton(size_hint = (0.3 , 1), background_down = "", background_normal = "" , background_color = hex_to_kv("#F2A71B" , 1) , background_disabled_down = "" ,text = "Joker" , font_size = "50dp")

        less = ToggleButton(size_hint = (0.4 , 1) ,background_down = "", background_normal = "" , background_color = hex_to_kv("#F23005" , 1) , background_disabled_down = "" ,
        text = "Lower" , font_size = "50dp")

        more.bind(on_press=self.switch)
        joker.bind(on_press=self.switch)
        less.bind(on_press=self.switch)
        """
        Add buttons
        """
        self.RGS.holder = BoxLayout(orientation = 'horizontal' , size_hint = (1 , 0.3) , spacing = 10 ,padding = (0 , 0 , 0 ,0))
        self.RGS.holder.add_widget(less)
        self.RGS.holder.add_widget(joker)
        self.RGS.holder.add_widget(more)


        self.Cardshow = CardShow()
        self.Betshow = BetShow(size_hint = (1 , 0.1))
        self.RGS.add_widget(self.Cardshow)

        self.RGS.add_widget(self.Betshow)
        self.RGS.add_widget(self.RGS.holder)

        a.add_widget(self.RGS)
        self.add_widget(a)

    def switch(self , obj , *args): # Only 1 button pressed at a clip
       
        if obj.state == 'normal': # Toggle normal on double click at the same button
            obj.background_color = (obj.background_color[0] , obj.background_color[1], obj.background_color[2] , 1)
            self.choosed = None
            return

        # Apply normal state for all
        for child in self.RGS.holder.children:
            child.background_color = (child.background_color[0] , child.background_color[1], child.background_color[2] , 1)
            child.state = 'normal'

        obj.state = 'down' # Apply down state for pressed button
        match obj.text:
            case "Higher" : self.choosed = 1
            case "Joker" : self.choosed = 0
            case "Lower" : self.choosed = -1
        obj.background_color = (obj.background_color[0] , obj.background_color[1], obj.background_color[2] , 0.5)

    def change_state(self , new_state): # Disable / Enable all buttons
        for child in self.RGS.holder.children:
            child.disabled = new_state

    def roundEnd_disable(self):
        for child in self.RGS.holder.children:
            if child.state == 'normal': child.disabled = True
    
    def roundStart(self):
        for child in self.RGS.holder.children:
            child.disabled = False
            child.state = "normal"
            child.background_color = (child.background_color[0] , child.background_color[1], child.background_color[2] , 1)
        self.choosed = None


class CardShow(BoxLayout): # Show 2 cards 

    
    c_color = ColorProperty(hex_to_kv("#337306" , 0))
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint = (1 , 0.75)
        self.spacing = 5
        self.padding = 10
        self.s_hint_a = 1
        self.canvas_opacity = 1
        self.correct_color = "#337306"
        self.wrong_color = "#BF0404"
        self.op = 0

        ##########################
        with self.canvas.before:
                Color(rgba=self.c_color)
                self.rect = Rectangle(pos = self.pos,
                                  size =(self.width / 2.,
                                         self.height / 2.))
                Color((0,0,0,1))
                # self.cb = Callback(self.mycallback)
                
                self.line = Line(width = 2 , rectangle = (self.x+5 , self.y , self.width , self.height ))
               
                self.bind(pos = update_line,size = update_line)
        ##########################
        self.A = Image(size_hint = (0.6 , 1) , source = "photos/sus_card.png" , keep_ratio = True , allow_stretch = True , pos_hint = {"center_y" : 0.5} )
        self.B = Image(size_hint = (0.6 , 1) , source = "photos/sus_card.png" , keep_ratio = True , allow_stretch = True )

        self.Aholder = BoxLayout()
        self.Bholder = BoxLayout()

        self.Aholder.add_widget(self.A)
        self.Bholder.add_widget(self.B)
        
        self.add_widget(self.Aholder)
        self.add_widget(self.Bholder)

    def redraw(self , pos , size):
        self.canvas.before.clear()
        with self.canvas.before:
                Color(rgba=self.c_color)
                self.rect = Rectangle(pos = self.pos,
                                  size =(self.width,
                                         self.height))
                Color((0,0,0,1))
                # self.cb = Callback(self.mycallback)
                
                self.line = Line(width = 2 , rectangle = (self.x+5 , self.y , self.width , self.height ))
        
        update_line(self)
               
    def reset(self , mode = 1):
        self.A.source = "photos/sus_card.png"
        self.B.source = "photos/sus_card.png"
        self.A.size_hint = (0.6 , 1)
      
    def show_card(self, src , index ):
        if index == 0: self.A.source = src
        elif index == 1: self.B.source = src

    def resize_card_A(self):
        
        
        self.s_hint_a = 1
        anim = Animation(s_hint_a = 0.7 , duration = 0.5)
        
        def progress(self , *args):
            obj = args[0]
            obj.A.size_hint = (0.6 * obj.s_hint_a, 1 * obj.s_hint_a)
        anim.bind(on_progress = progress)
        anim.start(self)

    def animate_background(self , option):
        
        
        def p(self , *args):
           
            obj = args[0]
            obj.c_color = [obj.c_color[0],obj.c_color[1] ,obj.c_color[2] , obj.op]
            obj.redraw(pos , size)
        if option == 0: new_color = hex_to_kv(self.correct_color , 1)
        elif option == 1: new_color = hex_to_kv(self.wrong_color ,  1)

        def b(self , *args):
            Clock.schedule_once(lambda x: args[0].b.start(args[0]) , 2.5)

        pos = self.rect.pos
        size = self.rect.size 
        self.c_color = [new_color[0], new_color[1] ,new_color[2] , 0]
        self.redraw(pos , size)
        
        
        tmp = [new_color[0] , new_color[1] , new_color[2] , 0]
        self.redraw(pos , size)
        a = Animation(op = 1 , duration = 0.5)
        a.bind(on_progress = p)
        a.bind(on_complete = b)
        self.b = Animation(op = 0 , duration = 0.25)
        self.b.bind(on_progress = p)


        a.start(self)
        

class BetShow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bet = 0
        self.L = Label(text = f"Current bet : {self.bet}")
        self.J = Label(text = "Streak bonus : x1" , font_size = "20dp")
        self.L.font_size = "30dp"
        self.add_widget(self.L)
        self.add_widget(self.J)

    def Change_bet(self , bet):
        self.bet += int(bet)
        self.L.text = f"Current bet : {str(self.bet)}"

    def Reset_bet(self):
        self.bet = 0
        self.L.text = f"Current bet : {str(self.bet)}"

    def Update_strike_bonus(self , bonus):
        self.J.text = f"Streak bonus : x{str(bonus)}"
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
        self.size_hint = (1 , 0.25)
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
    a = NumericProperty(10) # Seconds

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size= "50dp"
        self.halign = "center"
      

    def init(self):
        Animation.cancel_all(self)  # stop any current animations
        self.a = 10
        self.anim = Animation(a=0, duration=self.a)
        
    
    def start(self):
        self.anim.start(self)
    def stop(self):
        self.anim.stop()
     
    def on_a(self, instance, value):
        self.text = "Time left:\n" + str(round(value, 1))

class BettingWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1 , 0.5)


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
        self.b = Button(size_hint = (0.8 , 1) , text = "BET" , font_size = "70dp" ,background_disabled_normal = "" , background_normal = '', background_color = hex_to_kv("#DED5CA"))
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
        
        
        if self.button_mode:
            storage.c_root.GS.Betshow.Change_bet(0)
        else:
            tmp = make_bet(int(self.BetAmount.CoinsInput.text))
            
            if tmp is not False:
                
                storage.c_root.BW.creds.update_balance(tmp)
                storage.c_root.GS.Betshow.Change_bet(int(self.BetAmount.CoinsInput.text))
                self.BetAmount.CoinsInput.text = "0"
            else:
                #   Not succesfull betting 
                pass



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
    
        upp = BoxLayout(size_hint = (0.995,0.3) , pos_hint = {"center_x" : 0.5} , spacing = 1)
        down = BoxLayout(size_hint = (0.995,0.3) , pos_hint = {"center_x" : 0.5} , spacing = 1)
        self.CoinsInput = AmountInput()

        upp.add_widget(Button(font_size = "17dp" , background_color = hex_to_kv("#A14E0B") , background_normal = "" , text = "10000" , on_press = lambda x : self.CoinsInput.add_coins(10000)))
        upp.add_widget(Button(font_size = "17dp",background_color = hex_to_kv("#E0801E" ) , background_normal = "" ,text = "1000" , on_press = lambda x : self.CoinsInput.add_coins(1000)))
        upp.add_widget(Button(font_size = "17dp",background_color = hex_to_kv("#ED861F") , background_normal = "" ,text = "100" , on_press = lambda x : self.CoinsInput.add_coins(100)))
        upp.add_widget(Button(font_size = "17dp",background_color = hex_to_kv("#F2BE22") , background_normal = "" ,text = "10" , on_press = lambda x : self.CoinsInput.add_coins(10)))

        down.add_widget(Button(font_size = "17dp" , background_color = hex_to_kv("#F2BE22") , background_normal = "",text = "0" , on_press = lambda x : self.CoinsInput.mul_coins(0)))
        down.add_widget(Button(font_size = "17dp" , background_color = hex_to_kv("#1D594E") , background_normal = "",text = "1/2x" , on_press = lambda x : self.CoinsInput.mul_coins(0.5)))
        down.add_widget(Button(font_size = "17dp" , background_color = hex_to_kv("#F28705") , background_normal = "",text = "2x" , on_press = lambda x : self.CoinsInput.mul_coins(2)))
        down.add_widget(Button(font_size = "17dp" , background_color = hex_to_kv("#F23030") , background_normal = "",text = "Max" , on_press = lambda x : self.CoinsInput.max_coins()))
        
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
        self.size_hint = (1, 0.5)
        
        self.multiline = False
        
    def add_coins(self , to_add):
        tmp = int(self.text)
        tmp += to_add
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
            


def update_rect(obj, *args): # Update canvas rectangle for backgrounds

    obj.rect.pos = obj.pos
    obj.rect.size = obj.size
   

def update_line(obj , *args): # Update border pos for line and pos for rectangle

    obj.rect.pos = obj.pos
    obj.rect.size = obj.size
    obj.line.rectangle = (obj.x , obj.y , obj.width ,obj.height)


