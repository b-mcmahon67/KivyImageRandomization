import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
import random
from kivy.properties import StringProperty
from PIL import Image as IMG

Images = ['BLLvBPM', 'AngryCheeto', 'ThenvNow' ]
ImageFiles = {'BLLvBPM': "/Users/BrianMcMahon/Desktop/ImageProcessing/BPPvsBLM.jpg", 'AngryCheeto': "/Users/BrianMcMahon/Desktop/ImageProcessing/ourpresident.jpg",
             'ThenvNow': "/Users/BrianMcMahon/Desktop/ImageProcessing/thennowalways.jpg"}


Builder.load_file("updatepic.kv")

class RootLayout(FloatLayout):
	pass

class MyImageWidget(App):
    def __init__(self,**kwargs):
        super(MyImageWidget,self).__init__(**kwargs)
        self.image = Image(source='/Users/BrianMcMahon/Desktop/crop.jpg')
        self.imagefile = '/Users/BrianMcMahon/Desktop/crop.jpg'
        Clock.schedule_interval(self.update_pic,.3)
        Clock.schedule_interval(self.cropImage, .2)

    def update_pic(self,dt):
        self.image.reload()

    def cropImage(self,dt):

        imagefile = StringProperty()

        img = random.choice(Images)
        
        im = IMG.open(ImageFiles[img])
        w,h = im.size
        print(w,h)
        left = random.randrange(1,w)
        upper = random.randrange(1,h)
        right = random.randrange(left+1,w)
        lower= random.randrange(upper+1,h)

        box = (left, upper, right, lower)
        im_crop = im.crop(box)

        im_crop.save('/Users/BrianMcMahon/Desktop/crop.jpg')
        self.imagefile = StringProperty('/Users/BrianMcMahon/Desktop/crop.jpg')

    def build(self):
        return self.image


MyImageWidget().run()