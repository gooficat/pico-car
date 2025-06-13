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

l = Motor(0, 1)

r = Motor(2, 3)



def neutral():
    l.n()
    r.n()

def fwd():
    l.f()
    r.f()

def bck():
    l.b()
    r.b()
    
    
def rgt():
    l.f()
    r.b()
    
    
def lft():
    l.b()
    r.f()




while True:
    fwd()
    time.sleep(1)  
    bck()
    time.sleep(1)
    lft()
    time.sleep(1)
    rgt() 
    time.sleep(1)
