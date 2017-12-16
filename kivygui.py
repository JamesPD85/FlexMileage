from kivy.app import App
from kivy.graphics import Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import socket

class LoginForm(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline = False, password=True)
        self.add_widget(self.password)

class Widgets(Widget):
    pass

class MainMenu(Screen):
    pass

class LoginScreen(Screen):
    def build(self):
        return LoginForm()

class QuitScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("simplekivy.kv")

class SimpleKivy(App):
    def build(self):
        return presentation

if __name__ == "__main__":
    SimpleKivy().run()
