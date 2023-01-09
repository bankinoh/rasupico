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

base=Pin(15,Pin.OUT)
col=Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

st=0
cnt=0
tb=0
ta=0
tw=0
rpm=0

#duty_preset
freq=100
dw=60
db=60
dg=10
dy=20
dr=30


#Openning
#独立
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
    time.sleep(0.1)

#ベース電源ON
base.value(1)


while True:
    st=col.value()
    time.sleep(0.001)
    if not col.value() == st:
        if col.value() == 0:
            led_r0.duty_u16(int(65535*1/dr))
            cnt+=1
            print(cnt)
            ta=time.ticks_ms()
            tw=ta-tb
            tb=ta
            rpm=60000/tw
            print(rpm)
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
    if cnt == 10:
        cnt = 1
    else:
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