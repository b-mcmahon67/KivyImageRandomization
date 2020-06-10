import kivy
kivy.require('2.0.0') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
import random
from PIL import Image
import tempfile

tf = tempfile.NamedTemporaryFile()


Images = ['TPAB', 'GKMC' ]
ImageFiles = {'TPAB': "/Users/BrianMcMahon/Desktop/TPAB.jpg", 'GKMC': "/Users/BrianMcMahon/Desktop/gkmc.jpeg"}

def cropImage(image):

          imagefile = StringProperty()
          
          im = Image.open(ImageFiles[image])
          w,h = im.size
          print(w,h)
          left = random.randrange(0,w)
          upper = random.randrange(0,h)
          right = random.randrange(left,w)
          lower= random.randrange(upper,h)

          box = (left, upper, right, lower)
          im_crop = im.crop(box)

          im_crop.save(tf.name+'.jpg')

          filepath = (tf.name+'.jpg')

          return filepath



Builder.load_file("imageprocessing.kv")

class LoginScreen(Screen):
  pass

class ImageScreen(Screen):
  pass

class WindowManager(ScreenManager):
  pass

class RootLayout(FloatLayout):
  pass
    

class MainApp(App):
      
      imagefile = StringProperty()
      
      def selectImage(self):
        
        image = random.choice(Images)
        filepath = cropImage(image)

        self.imagefile = (filepath)

      def build(self):
        return RootLayout()

    
       

if __name__ == '__main__':
    app = MainApp()
    app.run()
