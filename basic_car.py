from machine import Pin
import time

in1 = Pin(1, Pin.OUT)
in2 = Pin(2, Pin.OUT)
in3 = Pin(3, Pin.OUT)
in4 = Pin(4, Pin.OUT)

def fwd():
    in1.high()
    in2.low()
    in3.high()
    in4.low()

def lft():
    in1.high()
    in2.low()
    in3.low()
    in4.high()
def rgt():
    in1.low()
    in2.high()
    in3.high()
    in4.low()
def stop():
    in1.low()
    in2.low()
    in3.low()
    in4.low()

while True:
  fwd()
  time.sleep(1)
  lft()
  time.sleep(1)
  rgt()
  time.sleep(1)
  bck()
  time.sleep(1)
