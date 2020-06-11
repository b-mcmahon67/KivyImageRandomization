import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.widget import Widget


class MyImageWidget(Widget):

    def __init__(self,**kwargs):
        super(MyImageWidget,self).__init__(**kwargs)
        self.image = Image(source='/Users/BrianMcMahon/Desktop/ImageProcessing/BPPvsBLM.jpg')
        self.add_widget(self.image)
        Clock.schedule_interval(self.update_pic,1)

    def update_pic(self,dt):
        self.image.reload()


class MyApp(App):
    def build(self):
        return MyImageWidget()


MyApp().run()