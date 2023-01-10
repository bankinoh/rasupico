from machine import Pin,PWM
import time

led_r0=PWM(Pin(10))
led_w1=PWM(Pin(9))
led_w2=PWM(Pin(8))
led_b1=PWM(Pin(7))
led_b2=PWM(Pin(6))
led_g1=PWM(Pin(5))
led_g2=PWM(Pin(4))
led_y1=PWM(Pin(3))
led_y2=PWM(Pin(2))
led_r1=PWM(Pin(1))
led_r2=PWM(Pin(0))

base=Pin(15, Pin.OUT)
col=Pin(16, Pin.IN, Pin.PULL_DOWN)

#duty_preset
freq=1000
dw=60
db=60
dg=10
dy=20
dr=30

pluseup=0
st=0
tb=0
ta=0
tw=0
rpm=0


def pulse(p):
    global pulseup
    pulseup=p

def openning():
    #初期化
    led_r0.freq(freq)
    led_r0.duty_u16(int(65535*1/dr))
    time.sleep(0.1)
    led_r0.duty_u16(0)

    led_w1.freq(freq)
    led_w1.duty_u16(int(65535*1/dw))
    time.sleep(0.1)
    led_w1.duty_u16(0)

    led_w2.freq(freq)
    led_w2.duty_u16(int(65535*1/dw))
    time.sleep(0.1)
    led_w2.duty_u16(0)

    led_b1.freq(freq)
    led_b1.duty_u16(int(65535*1/db))
    time.sleep(0.1)
    led_b1.duty_u16(0)

    led_b2.freq(freq)
    led_b2.duty_u16(int(65535*1/db))
    time.sleep(0.1)
    led_b2.duty_u16(0)

    led_g1.freq(freq)
    led_g1.duty_u16(int(65535*1/dg))
    time.sleep(0.1)
    led_g1.duty_u16(0)

    led_g2.freq(freq)
    led_g2.duty_u16(int(65535*1/dg))
    time.sleep(0.1)
    led_g2.duty_u16(0)

    led_y1.freq(freq)
    led_y1.duty_u16(int(65535*1/dy))
    time.sleep(0.1)
    led_y1.duty_u16(0)

    led_y2.freq(freq)
    led_y2.duty_u16(int(65535*1/dy))
    time.sleep(0.1)
    led_y2.duty_u16(0)

    led_r1.freq(freq)
    led_r1.duty_u16(int(65535*1/dr))
    time.sleep(0.1)
    led_r1.duty_u16(0)

    led_r2.freq(freq)
    led_r2.duty_u16(int(65535*1/dr))
    time.sleep(0.1)
    led_r2.duty_u16(0)

    #全点灯2回
    for led_two in range(2):
        led_r0.duty_u16(int(65535*1/dr))
        led_w1.duty_u16(int(65535*1/dw))
        led_w2.duty_u16(int(65535*1/dw))
        led_b1.duty_u16(int(65535*1/db))
        led_b2.duty_u16(int(65535*1/db))
        led_g1.duty_u16(int(65535*1/dg))
        led_g2.duty_u16(int(65535*1/dg))
        led_y1.duty_u16(int(65535*1/dy))
        led_y2.duty_u16(int(65535*1/dy))
        led_r1.duty_u16(int(65535*1/dr))
        led_r2.duty_u16(int(65535*1/dr))
        time.sleep(0.05)
        led_r0.duty_u16(0)
        led_w1.duty_u16(0)
        led_w2.duty_u16(0)
        led_b1.duty_u16(0)
        led_b2.duty_u16(0)
        led_g1.duty_u16(0)
        led_g2.duty_u16(0)
        led_y1.duty_u16(0)
        led_y2.duty_u16(0)
        led_r1.duty_u16(0)
        led_r2.duty_u16(0)
        time.sleep(0.05)

    #ベース電源ON
    base.value()
    
    col.irq(trigger=Pin.IRQ_RISING,handler=pulse)


def math():
    if pulseup(p):
            global tb,ta,tw,rpm
            led_r0.duty_u16(int(65535*1/dr))
            tb=time.ticks_ms()
            tw=tb-ta
            ta=tb
            rpm=60000/tw
            if rpm > 1000:
                led_w1.duty_u16(int(65535*1/dw))
            if rpm > 2000:
                led_w2.duty_u16(int(65535*1/dw))
            if rpm > 3000:
                led_b1.duty_u16(int(65535*1/db))
            if rpm > 4000:
                led_b2.duty_u16(int(65535*1/db))
            if rpm > 5000:
                led_g1.duty_u16(int(65535*1/dg))
            if rpm > 6000:
                led_g2.duty_u16(int(65535*1/dg))
            if rpm > 7000:
                led_y1.duty_u16(int(65535*1/dy))
            if rpm > 8000:
                led_y2.duty_u16(int(65535*1/dy))
            if rpm > 9000:
                led_r1.duty_u16(int(65535*1/dr))
            if rpm > 10000:
                led_r2.duty_u16(int(65535*1/dr))
            print (rpm)
            pulseup=0
            
            
            
openning()

while True:
    st=col.value()
    if not col.value()==st:
        if col.value()==0:
            math()
        else:
            time.sleep(0.1)
            led_r0.duty_u16(0)
            led_w1.duty_u16(0)
            led_w2.duty_u16(0)
            led_b1.duty_u16(0)
            led_b2.duty_u16(0)
            led_g1.duty_u16(0)
            led_g2.duty_u16(0)
            led_y1.duty_u16(0)
            led_y2.duty_u16(0)
            led_r1.duty_u16(0)
            led_r2.duty_u16(0)
