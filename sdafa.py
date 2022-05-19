import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class Grid(GridLayout):
    def __init__(self, **kwargs):

        super(Grid, self).__init__(**kwargs)
        self.rows = 3
        self.title = Label(text="MAIN SCREEN")
        self.add_widget(self.title)
        self.MainGrid = GridLayout()
        self.MainGrid.cols = 2
        self.b4 = Button(text="#b4")
        self.MainGrid.add_widget(self.b4)
        self.add_widget(self.MainGrid)


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)

        self.main_screen = Screen(name="main_screen")
        self.new_screen = Screen(name="new_screen")

        self.add_widget(self.main_screen)
        self.add_widget(self.new_screen)

        grid = Grid()
        grid.b4.bind(on_press=self.change_screen)
        self.main_screen.add_widget(grid)

    def change_screen(self, *args):
        self.current = "new_screen"


class MyApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    MyApp().run()