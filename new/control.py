#from pynput.mouse import Controller
from pynput.mouse import Controller

def controlMouse() :
    mouse = Controller()
    mouse.position = (100,260) #(l to r, top to bottom) 

controlMouse()   