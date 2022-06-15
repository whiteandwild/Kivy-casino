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

        self.login = BetterInput(multiline = False , size_hint = (2, 1) , hint_text = "Enter username")
        self.password = BetterInput(multiline = False , password = True , size_hint = (2, 1) , hint_text = "Enter password")

        LogBox = BoxLayout(padding = ["40dp" , "60dp" , "40dp" , "60dp"])

        LogBoxholder = BoxLayout(orientation = 'vertical')
        add_bg(LogBoxholder , "#FFFFFF" , 0.8)

        LogBox.add_widget(LogBoxholder)

        LoginLogo = BoxLayout(size_hint = (0.4 , 0.6) , pos_hint = {'center_x' : 0.5})
        Circle = BoxLayout(pos_hint = {'center_y' : 1})

        Circle.add_widget(Button())
        # with Circle.canvas:
        #     Color(rgba = [1,0,1,1])
        #     Circle.rect = Ellipse()
        #     Circle.bind(pos = update_rect,size = update_circle)
        

        LoginLogo.add_widget(Circle)


        Creds = BoxLayout(orientation = "vertical" ,padding = ["20dp" , 0 , "20dp" , 0] ,spacing = "10dp" , size_hint = (1 , 0.5))

        u_name = BoxLayout(pos_hint = {"center_x" :0.1})
        img = Image(source = "user.png",size_hint = (None , 1) ,width = 50 ,  keep_ratio = True , allow_stretch = True)
        add_bg(img , "#FFAE00" , 1)
        u_name.add_widget(img)
        u_name.add_widget(self.login)

        

        u_passwd = BoxLayout()
        img = Image(source = "passwd.png",size_hint = (None , 1) ,width = 50 , keep_ratio = True , allow_stretch = True)
        add_bg(img , "#FFAE00" , 1)
        u_passwd.add_widget(img)
        u_passwd.add_widget(self.password)

        
        Creds.add_widget(u_name)
        Creds.add_widget(u_passwd)

        LogBoxholder.add_widget(LoginLogo)
        LogBoxholder.add_widget(Creds)
        LogBoxholder.add_widget(Button())


        # holderForPasswd = AnchorLayout(size_hint = (0.75 , 0.3) , pos_hint = {"center_x" : 0.5}  , anchor_x = "right") 
        # holderForPasswd.add_widget(self.password)
        # holderForPasswd.add_widget(Button(text = "Show" , on_press = self.Show_hide_passwd , size_hint = (0.3 , 0.5) ,background_color = [0,0,0,0] , color = [0 , 0, 0 ,1]  , font_size = "25dp"))

        # Loggingbox = BoxLayout(orientation = "vertical" , padding = ["20dp" , "50dp" ,"20dp" ,"50dp"] , spacing = "20dp")
        # LoggingButtons = BoxLayout()
        # RememberMe = BoxLayout()
        
        # Loggingbox.add_widget(self.login)
        # Loggingbox.add_widget(holderForPasswd)
        # Loggingbox.add_widget(RememberMe)
        # Loggingbox.add_widget(LoggingButtons)
        
        
        # RememberMe.add_widget(CheckBox())
        # tmp = Label(text = "Remember me" , halign = "left")
        # def xyz(obj , *args):
        #     obj.text_size = obj.size

        # tmp.bind(on_size = xyz)
       
        # RememberMe.add_widget(tmp)


        

        # LoggingButtons.add_widget(Button(text = "Log in" , size_hint = (1 , 0.5) , on_press = self.Dologin))
        

        # LoggingButtons.add_widget(Button(text = "Sign up" , size_hint = (1 , 0.5) , on_press = self.Dosignup))

        up.add_widget(Button(size_hint = (0.7 , 1)))
        up.add_widget(LogBox)
        # up.add_widget(Loggingbox)

        self.holder.add_widget(up)
        self.holder.add_widget(self.games)

        self.add_widget(self.holder)

    def Dologin(self , *args):
        
        name = self.login.text
        passwd = self.password.text

        if name == "" or passwd == "":return


        response = login(user_name=name , password=passwd)

        print(response)

        if response == True :
            storage.current_user = storage.accounts[name]
    
    def Dosignup(self ,*args):
        
        name = self.login.text
        passwd = self.password.text

        if name == "" or passwd == "":return

        response = create_account(user_name=name , password=passwd)

        print(response)

    def Show_hide_passwd(self, obj , *args):
        
        if obj.text == "Hide":
            self.password.password = True
            obj.text = "Show"
        elif obj.text == "Show":
            self.password.password = False
            obj.text = "Hide"
    

class BetterInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.halign = "left"
        self.font_size = "20dp"

    def on_text(self , *args):
       
        self.text = self.text.replace(" " , "")
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
            

def update_rect(obj, *args): # Update canvas rectangle for backgrounds

    obj.rect.pos = obj.pos
    obj.rect.size = obj.size
def update_circle(obj, *args): # Update canvas rectangle for backgrounds

    obj.rect.pos = obj.pos
    obj.rect.size = (min(obj.size) , min(obj.size))

def add_bg(obj , color , opacity):
    with obj.canvas.before:
        with obj.canvas.before:
            Color(rgba = hex_to_kv(color , opacity))
            obj.rect = Rectangle(size=obj.size,pos=obj.pos)
            obj.bind(pos = update_rect,size = update_rect)