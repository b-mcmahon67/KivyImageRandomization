import kivy
kivy.require('2.0.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
import time
from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.start()

def image_job():
    return Image(source ='/Users/BrianMcMahon/Desktop/TPAB.jpg')

class MainApp(App):
    def build(self):

        
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .1, 'center_y': .1})
        
        sched.edd_interaval_job(image_job, seconds =10)

if __name__ == '__main__':
    app = MainApp()
    app.run()

