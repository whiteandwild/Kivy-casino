from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Color , RoundedRectangle , Line
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.label import Label
from globals import hex_to_kv

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
