from machine import Pin, PWM
import time

class Motor:
    def __init__(self, p1, p2):
        self.p1 = Pin(p1, Pin.OUT)
        self.p2 = Pin(p2, Pin.OUT)
    def f(self):
        self.p1.high()
        self.p2.low()
    def b(self):
        self.p1.low()
        self.p2.high()
    def n(self):
        self.p1.low()
        self.p2.low()

fl = Motor(12, 13)
fr = Motor(10, 11)

bl = Motor(19, 18)
br = Motor(21, 20)



def neutral():
    fl.n()
    fr.n()
    bl.n()
    br.n()

def fwd():
    fl.f()
    fr.f()
    bl.f()
    br.f()

def bck():
    fl.b()
    fr.b()
    bl.b()
    br.b()
    
    
def rgt():
    fl.f()
    fr.b()
    bl.f()
    br.b()
    
    
def lft():
    fl.b()
    fr.f()
    bl.b()
    br.f()




while True:
    fwd()
    time.sleep(1)  
    bck()
    time.sleep(1)
    lft()
    time.sleep(1)
    rgt() 
    time.sleep(1)
