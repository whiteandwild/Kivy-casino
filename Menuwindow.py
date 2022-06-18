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
        #####

        self.password.ispasswd = True
        self.login.ispasswd = False

        self.LogBox = BoxLayout(padding = ["40dp" , "60dp" , "40dp" , "60dp"] , orientation = 'vertical')
        
 
        up.add_widget(Button(size_hint = (0.7 , 1)))
        up.add_widget(self.LogBox)


        self.holder.add_widget(up)
        self.holder.add_widget(self.games)

        self.add_widget(self.holder)
        self.CreateLoginBox()

    def CreateLoginBox(self):
        Al = AnchorLayout(anchor_x = "center") # Center Login widget
        self.LogBox.add_widget(Al)

        LogBoxholder = LBH(orientation = 'vertical' , size_hint = (None , 0.9) , width = 500)
        Al.add_widget(LogBoxholder)
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

        Login_Buttons.add_widget(Button(pos_hint = {"center_y" : 0} ,font_name = "RobotoMono-Regular", text = "Log in" , on_press = self.Dologin , size_hint = (1 , 1) , background_normal = "" , background_color = hex_to_kv("#F2A71B" , 0.8) , color = [0,0,0,1] , font_size = "30dp"))
        Login_Buttons.add_widget(Button(pos_hint = {"center_y" : 0} , font_name = "RobotoMono-Regular",text = "Sign up" , on_press = self.Dosignup ,background_normal = "" , background_color = hex_to_kv("#F2A71B" , 0.8) , color = [0,0,0,1] , font_size = "30dp"))


        LogBoxholder.add_widget(LoginLogo)
        LogBoxholder.add_widget(Creds)
        LogBoxholder.add_widget(Login_Buttons)


    def Dologin(self , *args):
        
        name = self.login.text
        passwd = self.password.text

        if name == "" or passwd == "":return


        response = login(user_name=name , password=passwd)

        

        if response == True :
            storage.current_user = storage.accounts[name]
        else:
            self.info.text = response
    
    def Dosignup(self ,*args):
        
        name = self.login.text
        passwd = self.password.text

        if name == "" or passwd == "":return

        response = create_account(user_name=name , password=passwd)

        if response == True :
            storage.current_user = storage.accounts[name]
        else:
            self.info.text = response

    def Show_hide_passwd(self, obj , *args):
        if obj.mode == 0:
            self.password.password = False
            obj.mode = 1
            obj.source = "photos/hide.png"
        elif obj.mode == 1:
            self.password.password = True
            obj.mode = 0
            obj.source = "photos/show.png"
    

class BetterInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.halign = "left"
        self.font_size = "20dp"
        self.background_color = [1,1,1,1] 
        self.background_normal =  'photos/white.png'
        self.background_active ='photos/white.png'
        self.font_name = "RobotoMono-Regular"
    def on_text(self , *args):
       
        self.text = self.text.replace(" " , "")
        
        if not self.ispasswd:
            self.text = self.text.lower()

        if len(self.text) >= 15:
            self.text = self.text[:15]

        
    def on_size(self, instance, value):
        self.padding_y =  [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]

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
class LeftLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_size(self , *args):
        self.text_size = self.size

class showhide(ButtonBehavior , Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mode = 0
       

def update_rect(obj, *args): # Update canvas rectangle for backgrounds

    obj.rect.pos = obj.pos
    obj.rect.size = obj.size
def update_circle(obj, *args): # Update canvas rectangle for backgrounds

    obj.rect.pos = obj.pos
    obj.rect.size = (min(obj.size) , min(obj.size))

def add_bg(obj , color , opacity):
    with obj.canvas.before:
            Color(rgba = hex_to_kv(color , opacity))
            obj.rect = Rectangle(size=obj.size,pos=obj.pos)
            obj.bind(pos = update_rect,size = update_rect)


