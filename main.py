import kivymd as kivymd
from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.lang import Builder

class MainWidget(Widget):
    pass



class mainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('main.kv')



mainApp().run()