# Kivy elements
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

# Other

from cards import *
from globals import *
from universalwidgets import *

class BlackJack(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "BlackJack"
        add_bg(self ,"#A6032F" , 1)

        self.dealerScore = 0
        self.playerScore = 0
        self.playing = False



        holder = BoxLayout()

        
        self.Rightside = BoxLayout(size_hint = (0.35 , 1) , padding = "7dp" , orientation = 'vertical' , spacing = "5dp")
        self.Rightside.add_widget(BettingWindow(size_hint = (1,0.5)))
        holder.add_widget(Button())
        holder.add_widget(self.Rightside)
        

        self.add_widget(holder)

        self.menu = Button(text = "MENU" , background_color = hex_to_kv("#DED5CA") , background_normal = "" , on_press = self.change_to_menu)
        
    
        self.Buttons = BoxLayout(size_hint = (None , None) , size = (150 , 75) , pos_hint = {"right" : 1} , spacing = 5 , padding = 5)
        self.Buttons.add_widget(Button(text = "INFO" , background_color = hex_to_kv("#DED5CA") , background_normal = "" , on_press = self.info))
        self.Buttons.add_widget(self.menu)

        self.add_widget(self.Buttons)
    def info(self , *args):
        pass
    def change_to_menu(self , *args):

    
        if self.playing:
            
            def fun(*args):
                return_coins()
                popup.dismiss()
                self.manager.current = 'mainmenu'
                
            c = BoxLayout(orientation = "vertical")
            holder = BoxLayout()


            l = Label(text = "Coins will return and you won't be able to continue current game" , color = [0,0,0,1]) 

        
            c.add_widget(l)
            c.add_widget(holder)
            

            popup = Popup(title = "Are you sure??" , title_align = 'center',title_color= [0,0,0,1] , title_size = "30dp" , separator_color = "red" , size_hint =(0.75 , 0.2) , content = c)
            popup.background = ""
            popup.background_color = [1,1,1,0.9]



            holder.add_widget(Button(text = "Yes" , on_press = fun ))
            holder.add_widget(Button(text = "No , return to game" , on_press = popup.dismiss))
            popup.open()
        else:
            self.manager.current = 'mainmenu'
    def add_score(self , card , player):

        cardScore = 0
        if card.figure in ["2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10"]:
            cardScore = int(card.figure)
        elif card.figure == "A":
            pass
        else:
            cardScore = 10
        
        if player == "player":
            self.playerScore += cardScore
        elif player == "dealer":
            self.dealerScore += cardScore

    def check_if_over(self , points):
        return (True if points >= 21 else False)

    def check_who_won(self):
        if self.playerScore > 21:
            return "Dealer"
        
        pDiff = 21-self.playerScore
        dDiff = 21-self.playerScore

        if pDiff == dDiff: return "Draw"

        if pDiff < dDiff : return "Player"
        else:
            return "Dealer"  
        
        

    def DealerTurn(self):

        while self.dealerScore < 17:
            # get card
            pass       
            

