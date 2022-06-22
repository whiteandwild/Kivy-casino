# Kivy elements
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.graphics import Rectangle, Color , Line , Ellipse
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.behaviors import ButtonBehavior
# Other
from globals import *
from universalwidgets import *

class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'mainmenu'
       
        self.holder = holder()
        self.games = GridLayout(rows = 1 , cols = 3 , padding = "15dp" , spacing = "15dp")
        
        

        self.games.add_widget(Button(text="Lower Higher" , on_press = lambda x: App.get_running_app().gen_screen('LowerHigher')))
        self.games.add_widget(Button())
        self.games.add_widget(Button())

        up = BoxLayout()
        ##### References
        self.login = BetterInput(multiline = False , size_hint = (2, 1) , hint_text = "username",pos_hint = {'center_y' : 0.8})
        self.password = BetterInput(multiline = False , password = True , size_hint = (1, 1) , hint_text = "password")
        self.info = Label(text = "" , color = "red" , font_size = "20dp")
        self.rememberMe = CheckBox(size_hint = (0.05 , 1) , pos_hint = {"center_y" : 0.5} , color = [0,0,0,1])
        self.balance = Balancelabel(color = [0,0,0,1],font_name = "RobotoMono-Regular" , font_size = "50dp")
        #####


        self.LogBox = AnchorLayout()
        
 
        up.add_widget(Button(size_hint = (0.7 , 1)))
        up.add_widget(self.LogBox)


        self.holder.add_widget(up)
        self.holder.add_widget(self.games)

        self.add_widget(self.holder)
        self.CreateLoginBox()

        if storage.current_user.user_name != "Guest":
            self.CreateProfileBox()
            self.on_login()
            

    def Clear_inputs(self): # After log in
        # self.login.text = ""
        self.password.text = ""
        self.info.text = ""
        self.rememberMe.active = False

    def CreateLoginBox(self):

        ##### References
        self.login = BetterInput(multiline = False , size_hint = (2, 1) , hint_text = "username",pos_hint = {'center_y' : 0.8})
        self.password = BetterInput(multiline = False , password = True , size_hint = (1, 1) , hint_text = "password")
        self.info = Label(text = "" , color = "red" , font_size = "20dp")
        self.rememberMe = CheckBox(size_hint = (0.05 , 1) , pos_hint = {"center_y" : 0.5} , color = [0,0,0,1])
        #####

        self.password.ispasswd = True
        self.login.ispasswd = False
  

        self.LogBox.clear_widgets()
        self.Al = AnchorLayout(padding = ["40dp" , "60dp" , "40dp" , "60dp"] , anchor_x = "center") # Center Login widget
        self.LogBox.add_widget(self.Al)

        LogBoxholder = LBH(orientation = 'vertical' , size_hint = (None , 0.9) , width = 500)
        self.Al.add_widget(LogBoxholder)
        add_bg(LogBoxholder , "#FFFFFF" , 0.8)

        
        LoginLogo = BoxLayout(size_hint = (0.5 , 1) , pos_hint = {'center_x' : 0.5})
        
        #####
        Circle = BoxLayout() # Top logo
        Circle.add_widget(Image(source = "photos/loginLogo.png" , keep_ratio = True , allow_stretch = True  , size_hint = (1.4 , 1.4) , pos_hint = {'center_y' : 1}))
        LoginLogo.add_widget(Circle)
        #####

        ##### Mid
        Creds = BoxLayout(orientation = "vertical" ,padding = ["20dp" , 0 , "20dp" , 0] ,spacing = "10dp" , size_hint = (1 , 1.3))

        u_name = BoxLayout()
        img = Image(source = "photos/user.png",size_hint = (None , 1) ,width = 50 ,  keep_ratio = True , allow_stretch = True , pos_hint = {'center_y' : 0.8})
        add_bg(img , "#FFAE00" , 1)
        u_name.add_widget(img)
        u_name.add_widget(self.login)

        u_passwd = BoxLayout()
        img = Image(source = "photos/passwd.png",size_hint = (None , 1) ,width = 50 , keep_ratio = True , allow_stretch = True ,pos_hint = {'center_y' : 0.8})
        add_bg(img , "#FFAE00" , 1)
        u_passwd.add_widget(img)
        holderForPasswd = AnchorLayout(anchor_x = "right" , pos_hint = {'center_y' : 0.8}) 
        holderForPasswd.add_widget(self.password)
        holderForPasswd.add_widget(showhide(source = "photos/show.png" , on_press = self.Show_hide_passwd,size_hint = (0.2 , 0.85) , allow_stretch = True , keep_ratio = True))


        u_passwd.add_widget(holderForPasswd)
        # holderForPasswd.add_widget(Button(text = "Show" , on_press = self.Show_hide_passwd , size_hint = (0.3 , 0.5) ,background_color = [0,0,0,0] , color = [0 , 0, 0 ,1]  , font_size = "25dp"))


        Extras = BoxLayout(size_hint = (0.9 , 0.4) , pos_hint = {"center_x" : 0.5})
        RememberMe = BoxLayout(spacing = "10dp")
        RememberMe.add_widget(self.rememberMe)
        L = LeftLabel(text = "Don't log out" , color = [0,0,0,1] , halign = "left" , valign = "center" , font_size = "15dp")
        RememberMe.add_widget(L)

        Extras.add_widget(RememberMe)
        Extras.add_widget(self.info)

        
        Creds.add_widget(u_name)
        Creds.add_widget(u_passwd)
        Creds.add_widget(Extras)
        

        # Buttons
        Login_Buttons = BoxLayout(size_hint = (0.75 ,0.5),pos_hint = {"center_x" : 0.5} , spacing = "30dp")

        Login_Buttons.add_widget(HoverButton(pos_hint = {"center_y" : 0} ,font_name = "RobotoMono-Regular", text = "Log in" , on_press = self.Dologin , size_hint = (1 , 1) , background_normal = "" , background_color = hex_to_kv("#F2A71B" , 0.8) , color = [0,0,0,1] , font_size = "30dp"))
        Login_Buttons.add_widget(HoverButton(pos_hint = {"center_y" : 0} , font_name = "RobotoMono-Regular",text = "Sign up" , on_press = self.Dosignup ,background_normal = "" , background_color = hex_to_kv("#F2A71B" , 0.8) , color = [0,0,0,1] , font_size = "30dp"))


        LogBoxholder.add_widget(LoginLogo)
        LogBoxholder.add_widget(Creds)
        LogBoxholder.add_widget(Login_Buttons)

     

    def CreateProfileBox(self):


        self.balance = Balancelabel(text = f"{storage.current_user.balance} coins" , color = [0,0,0,1],font_name = "RobotoMono-Regular")
        whole = BoxLayout(padding = "10dp")
        self.LogBox.add_widget(whole)

        holder = BoxLayout(orientation = "horizontal")
        whole.add_widget(holder)

        add_bg(holder , "#FFFFFF" , 0.8)

        leftSide = BoxLayout(orientation = "vertical" , size_hint_x = 0.9)
        holder.add_widget(leftSide)

        ProfileImage = AnchorLayout(anchor_x = "center" , anchor_y = "center" ,padding = "10dp" , size_hint = (1 , 1.3))
        ProfileImage.add_widget(Image(source = "photos/userprofile.png"))

        unameHolder = BoxLayout(size_hint = (0.75 , 0.3) , pos_hint = {"center_x" : 0.5})
        self.uname= Label(text = storage.current_user.user_name , font_size = "50dp" , color = [0,0,0,1]  , font_name = "RobotoMono-Regular" , valign = "top" , halign = "center")
        unameHolder.add_widget(self.uname)


        ProfileButtons = BoxLayout(padding = "20dp" , spacing = "20dp" , size_hint = (1, 0.6))
        ProfileButtons.add_widget(RoundedButton( r=7 , c=hex_to_kv("#F2A71B" , 0.8) , text = "Log out", font_size = "20dp" , color = [0,0,0,1] ,font_name = "RobotoMono-Regular"  , on_press = lambda x : self.on_logout(whole)) )
        ProfileButtons.add_widget(RoundedButton(r=7,c=hex_to_kv("#00000" , 0.9) , text = "Terminal" , font_size = "20dp" , color = [1,1,1,1] ,font_name = "RobotoMono-Regular"  , on_press = self.open_terminal))
        


        leftSide.add_widget(ProfileImage)
        leftSide.add_widget(unameHolder)
        leftSide.add_widget(ProfileButtons)

        rightSide = BoxLayout(orientation = "vertical" , padding = ["10dp" , "10dp" , "10dp" , "20dp"] , spacing = "20dp")

        ubalanceHolder = AnchorLayout(anchor_x = "center" , anchor_y = "center" , size_hint_y = 0.3)
        rightSide.add_widget(ubalanceHolder)
        ubalanceHolder.add_widget(self.balance)

        statsHolder = BoxLayout(orientation = "vertical" , padding = [0, "40dp" , 0 , "20dp"])
        # add_border(statsHolder , "#FFFFFF" , 3)
        rightSide.add_widget(statsHolder)

        # statsHolder.add_widget(Label(text = "Stats:" , font_size = "50dp" , color = [0,0,0,1] , size_hint = (1, 0.5) , halign = "center"))

        stats = BoxLayout(orientation = 'vertical')

        self.maxBetLabel = StatsLabel(text = f"Max bet : {storage.current_user.maxBet} coins" , color = [0,0,0,1]  , font_size = "20dp" , valign = "center" , halign = "center")
        self.maxWinLabel = StatsLabel(text = f"Max win : {storage.current_user.maxWin} coins" , color = [0,0,0,1]  , font_size = "20dp" , valign = "center", halign = "center")
        self.totalBetsLabel = StatsLabel(text = f"Total bets : {storage.current_user.totalBets} coins" , color = [0,0,0,1]  , font_size = "20dp" , valign = "center", halign = "center")
        self.winRatioLabel = StatsLabel(text = f"Win ratio : {calc_winratio(storage.current_user)}%" , color = [0,0,0,1]  , font_size = "20dp" , valign = "center", halign = "center")

        stats.add_widget(self.maxBetLabel)
        stats.add_widget(self.maxWinLabel)
        stats.add_widget(self.totalBetsLabel)
        stats.add_widget(self.winRatioLabel)
        statsHolder.add_widget(stats)



        holder.add_widget(rightSide)
        
    def update_stats(self):
        
        if storage.current_user.user_name != "Guest":
            self.maxBetLabel.text =f"Max bet : {storage.current_user.maxBet} coins" 
            self.maxWinLabel.text = f"Max win : {storage.current_user.maxWin} coins"
            self.totalBetsLabel.text =f"Total bets : {storage.current_user.totalBets} coins" 
            self.winRatioLabel.text = f"Win ratio : {calc_winratio(storage.current_user)}%"
            self.balance.text = f"{storage.current_user.balance} coins"


    def Dologin(self , *args):
        
        name = self.login.text
        passwd = self.password.text
        rememberme = True if self.rememberMe.state == "down" else False

        if name == "" or passwd == "":return


        response = login(user_name=name , password=passwd , rememberme=rememberme)


        if response == True :
        
            
        
            self.CreateProfileBox()
            self.on_login()
        else:
            self.info.text = response
    
    def Dosignup(self ,*args):
        
        name = self.login.text
        passwd = self.password.text
        rememberme = True if self.rememberMe.state == "down" else False
        
        if name == "" or passwd == "":return

        response = create_account(user_name=name , password=passwd , rememberme=rememberme)

        if response == True :
            
            self.CreateProfileBox()
            self.on_login()
        else:
            self.info.text = response

    def on_login(self , *args):
        self.update_stats()
        self.change_to_profile()

    def on_logout(self ,obj, *args):
        logout()
        self.LogBox.remove_widget(obj)
        create_guest()
        self.change_to_login()
        # self.CreateLoginBox()

    def change_to_profile(self):
        self.Clear_inputs()
        self.Al.disabled = True
        self.Al.opacity = 0
    
    def change_to_login(self):
        self.Al.disabled = False
        self.Al.opacity = 1

    def Show_hide_passwd(self, obj , *args):
        if obj.mode == 0:
            self.password.password = False
            obj.mode = 1
            obj.source = "photos/hide.png"
        elif obj.mode == 1:
            self.password.password = True
            obj.mode = 0
            obj.source = "photos/show.png"

    def on_pre_enter(self, *args):
        if storage.current_user != None:
            self.update_stats()

    def open_terminal(self , *args):
        storage.current_user.reset()
        self.update_stats()


class holder(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        with self.canvas.before:
            
            self.rect = Rectangle(size=self.size,pos=self.pos , source = "photos/MenuBackground.png")
            self.bind(pos = update_rect,size = update_rect)

class LBH(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_size(self , *args):
        self.width = self.height * (500/297)

class showhide(ButtonBehavior , Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mode = 0
       
class Balancelabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[15],
            )
            self.bind(pos = update_rect,size = update_rect)


    def on_size(self , *args):
        self.font_size = self.width /8