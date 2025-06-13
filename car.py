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

left = Motor(0, 1)

right = Motor(2, 3)


while True:
    left.f()
    right.f()
    time.sleep(1)

    left.b()
    right.n()
    time.sleep(1)

    left.n()
    right.n()
    time.sleep(1)
