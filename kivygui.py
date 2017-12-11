from kivy.app import App
from kivy.uix.label import Label
# from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput

# class LoginScreen(GridLayout):
#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#
#         self.add_widget(Label(text="Username: "))
#         self.username = TextInput(multiline = False)
#         self.add_widget(self.username)
#
#         self.add_widget(Label(text="Password: "))
#         self.password = TextInput(multiline = False, password=True)
#         self.add_widget(self.password)

class Widgets(Widget):
    pass

class TouchInput(Widget):
    def on_touch_down(self,touch):
        print(touch)
    def on_touch_move(self,touch):
        print(touch)
    def on_touch_up(self,touch):
        print("RELEASED!",touch)


class SimpleKivy(App):
    def build(self):
        return TouchInput()

if __name__ == "__main__":
    SimpleKivy().run()
