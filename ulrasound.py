from machine import Pin, PWM
import time
import utime

trigger = Pin(8, Pin.OUT)
echo = Pin(7, Pin.IN)

ena = PWM(Pin(5))
enb = PWM(Pin(6))

in1 = Pin(1, Pin.OUT)
in2 = Pin(2, Pin.OUT)
in3 = Pin(3, Pin.OUT)
in4 = Pin(4, Pin.OUT)

neck = PWM(Pin(9))

ena.freq(1000)
enb.freq(1000)

neck.freq(50)

min_duty = 1638
max_duty = 7864
half_duty = int(max_duty/2)

speed = 100000

def fwd():
    ena.duty_u16(speed)
    in1.high()
    in2.low()
    enb.duty_u16(speed)
    in3.high()
    in4.low()

def lft():
    ena.duty_u16(speed)
    in1.high()
    in2.low()
    enb.duty_u16(speed)
    in3.low()
    in4.high()
def rgt():
    ena.duty_u16(speed)
    in1.low()
    in2.high()
    enb.duty_u16(speed)
    in3.high()
    in4.low()
def stop():
    ena.duty_u16(0)
    in1.low()
    in2.low()
    enb.duty_u16(0)
    in3.low()
    in4.low()

def get_dist():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    timeout = utime.ticks_us() + 30000
    
    signaloff = 0
    signalon = 0
    
    while echo.value() == 0:
        signaloff = utime.ticks_us()
        if utime.ticks_us() > timeout:
            return 100
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    timepassed = signalon - signaloff
    dist = (timepassed * 0.0343) / 2
    return dist

while True:
    dis = get_dist()
    if dis > 30:
        fwd()
    else:
        stop()
        neck.duty_u16(min_duty)
        time.sleep(1)
        dis_l = get_dist()
        neck.duty_u16(max_duty)
        time.sleep(1)
        dis_r = get_dist()
        neck.duty_u16(half_duty)
        if dis_r > dis_l:
            rgt()
        else:
            lft()
        time.sleep(1)
    time.sleep(0.2)

