# Kivy elements
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
# Other

from console import *
from globals import *
from universalwidgets import *

class Terminal(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.75,0.75)


        self.title = "Terminal"
        self.separator_color = hex_to_kv("#C0FF00")

        holder = BoxLayout(orientation = "vertical" , padding = [0,0,0,"20dp"])
        self.add_widget(holder)

        
        self.Scrolling = ScrollView(do_scroll_y = True , do_scroll_x = False , bar_width = 5 , scroll_type = ['bars', 'content'] , always_overscroll = False)
        self.outputs = xyzGrid(cols = 1 , row_default_height = 35 , row_force_default = True , size_hint_y = None , padding = [0,0,20,20], orientation = "bt-rl")
        self.outputs.bind(minimum_height = self.outputs.setter("height"))
        # self.outputs = xyzGrid(cols = 1 , row_default_height = 30 , row_force_default = True , size_hint = (1,1), padding = [0,0,20,0] , orientation = "bt-rl")
        self.Scrolling.add_widget(self.outputs)

        apply = Button(on_press = self.apply , size_hint = (0.2 , 1) , color = hex_to_kv("#C0FF00")  , text = "Enter" , font_size = "30dp")
        InputBox = BoxLayout(size_hint = (1 , 0.1))

        holder.add_widget(self.Scrolling)
        # holder.add_widget(self.outputs)
        holder.add_widget(InputBox)

        self.input = TextInput(multiline = False)
        InputBox.add_widget(self.input)
        InputBox.add_widget(apply)

     
       
        
        if storage.current_user.isAdmin:
            self.commands = get_admin_commands()
        else:
            self.commands = get_admin_commands()    

    def apply(self , *args):
        
        self.on_input()
    def on_input(self , *args):
        
        command = self.input.text
        
        arguments = command.split()
        self.print_com(command)
        if arguments[0] not in self.commands:
            self.print_res("Invalid command")
        else:
            res = self.commands[arguments[0]](arguments[1:])
            for r in res:
                tmp = self.print_res(r)
        self.Scrolling.scroll_y = 0

        


    def print_res(self, value):
        tmp = TerminalLabel(text = value , color = hex_to_kv("#C0FF00"))
        tmp.font_size = "20dp"
        self.outputs.add_widget(tmp , len(self.outputs.children))
        
        return tmp
        
    def print_com(self, value):
        tmp = TerminalLabel(text = f"{value} :{storage.current_user.user_name}" , color = [1,1,1,1])
        
        self.outputs.add_widget(tmp , len(self.outputs.children))
        self.outputs.on_size()

class TerminalLabel(LeftLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.halign = "right"
        self.font_size = "20dp"

class xyzGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_size(self , *args):
        return
        self.minimum_height = max(self.parent.height , self.height)
      