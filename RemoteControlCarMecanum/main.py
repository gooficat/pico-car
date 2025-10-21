from machine import Pin, PWM
import time
from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8

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

pin_ir = Pin(16, Pin.IN)

Up = 24
Down = 82
Left = 8
Right = 90
Stop = 28


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
    bl.b()
    br.f()
    
    
def lft():
    fl.b()
    fr.f()
    bl.f()
    br.b()

def decodeKeyValue(data):
    return data

def callback(data, addr, ctrl):
    if data < 0:
        pass
    else:
        print(data)
        if data == Up:
            fwd()
        elif data == Down:
            bck()
        elif data == Left:
            lft()
        elif data == Right:
            rgt()
        elif data == Stop:
            neutral()
        
ir = NEC_8(pin_ir, callback)
ir.error_function(print_error)

fwd()
time.sleep(1)
neutral()

try:
    while True:
        pass
except KeyboardInterrupt:
    ir.close()
