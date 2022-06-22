# Kivy elements
from kivy.uix.popup import Popup

# Other

from console import *

class Terminal(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
