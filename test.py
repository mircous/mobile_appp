from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        btn = Button(text ="Push Me !",
                    font_size ="20sp",
                    background_color =(1, 1, 1, 1),
                    color =(1, 1, 1, 1),
                    size =(32, 32),
                    size_hint =(.2, .2),
                    pos =(300, 20))
        btn.on_press = self.next
        self.add_widget(btn)

    def build(self):
        return Label(text='Hello world')

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text ="Push Me !",
                    font_size ="20sp",
                    background_color =(1, 1, 1, 1),
                    color =(1, 1, 1, 1),
                    size =(32, 32),
                    size_hint =(.2, .2),
                    pos =(300, 20))
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'

    # def build(self):
    #     btn = Button(text ="Push Me !",
    #                font_size ="20sp",
    #                background_color =(1, 1, 1, 1),
    #                color =(1, 1, 1, 1),
    #                size =(32, 32),
    #                size_hint =(.2, .2),
    #                pos =(300, 20))
    #     return btn
    # def build(self):
    #     screen = Screen()

    #     btn= MDRectangleFlatButton(text="Submit",pos_hint={'center_x':0.5,'center_y':0.3},on_release=self.btnfunc)
    #     screen.add_widget(btn)
    #     # adding widgets to screen

    #     return screen
    # def btnfunc(self,obj):
    #     print("button is pressed!!")
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        return sm

if __name__ == '__main__':
    MyApp().run()
