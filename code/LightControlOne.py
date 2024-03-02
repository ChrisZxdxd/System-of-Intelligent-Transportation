import RPi.GPIO as GPIO
import time
import serial
import number
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def init(Glight_P=4, Ylight_P=5, Rlight_P=6, Glight_C=13, Ylight_C=16, Rlight_C=17):  # GPIO pins using
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Glight_P, GPIO.OUT)  # GPIO pin 4 for Green Light of Passerbys
    GPIO.setup(Ylight_P, GPIO.OUT)  # GPIO pin 5 for Yellow Light of Passerbys
    GPIO.setup(Rlight_P, GPIO.OUT)  # GPIO pin 6 for Red Light of Passerbys
    GPIO.setup(Glight_C, GPIO.OUT)  # GPIO pin 13 for Green Light of Cars
    GPIO.setup(Ylight_C, GPIO.OUT)  # GPIO pin 16 for Yellow Light of Cars
    GPIO.setup(Rlight_C, GPIO.OUT)  # GPIO pin 17 for Red Light of Cars
    time.sleep(0.1)

    #Vehicles can go through, passerbys can't cross the road.
    GPIO.output(Glight_P, 0)
    GPIO.output(Ylight_P, 0)
    GPIO.output(Rlight_P, 1)
    GPIO.output(Glight_C, 1)
    GPIO.output(Ylight_C, 0)
    GPIO.output(Rlight_C, 0)


def work(num , pin):  #控制信号灯和舵机
    # number.work(num, pin,'5')
    t = 2
    if t == 2:
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 1)
        GPIO.output(13, 1)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        print("倒计时十秒.")
        number.work(num, pin, '8', 1)
        number.work(num, pin, '7', 1)
        number.work(num, pin, '6', 1)
        number.work(num, pin, '5', 1)
        number.work(num, pin, '4', 1)
        number.work(num, pin, '3')
        t = 3
    if t == 3:
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        time.sleep(0.5)
        t = 4
    if t == 4:
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 1)
        GPIO.output(13, 1)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        time.sleep(0.5)
        number.work(num, pin, '2')
        t = 5
    if t == 5:
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        time.sleep(0.5)
        t = 6
    if t == 6:
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 1)
        GPIO.output(13, 1)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        time.sleep(0.5)
        number.work(num, pin, '1')
        t = 7
    if t == 7:
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        time.sleep(0.5)
        t = 8
    if t == 8:
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 1)
        GPIO.output(13, 1)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        time.sleep(0.5)
        number.work(num, pin, '.')
        t = 9
    if t == 9:
        ser.write('1'.encode())  # ****************
        time.sleep(0.1)
        GPIO.output(4, 1)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 0)
        GPIO.output(17, 1)
        print("倒计时十秒.")
        time.sleep(6)
        number.work(num, pin, '9', 1)
        number.work(num, pin, '8', 1)
        number.work(num, pin, '7', 1)
        number.work(num, pin, '6', 1)
        number.work(num, pin, '5', 1)
        number.work(num, pin, '4', 1)
        number.work(num, pin, '3')
        t = 10
    if t == 10:
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        time.sleep(0.5)
        t = 11
    if t == 11:
        GPIO.output(4, 1)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 0)
        GPIO.output(17, 1)
        time.sleep(0.5)
        number.work(num, pin, '2')
        t = 12
    if t == 12:
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        time.sleep(0.5)
        t = 13
    if t == 13:
        GPIO.output(4, 1)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 0)
        GPIO.output(17, 1)
        time.sleep(0.5)
        number.work(num, pin, '1')
        t = 14
    if t == 14:
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        time.sleep(0.5)
        t = 15
    if t == 15:
        GPIO.output(4, 1)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 0)
        GPIO.output(17, 1)
        time.sleep(0.5)
        number.work(num, pin, '.')
        t = 16
    if t == 16:
        GPIO.output(4, 0)
        GPIO.output(5, 1)
        GPIO.output(6, 0)
        GPIO.output(13, 0)
        GPIO.output(16, 1)
        GPIO.output(17, 0)
        print("黄灯持续三秒.")
        number.work(num, pin, '3', 1)
        number.work(num, pin, '2', 1)
        number.work(num, pin, '1', 1)
        number.work(num, pin, '.')
        GPIO.output(4, 0)
        GPIO.output(5, 0)
        GPIO.output(6, 1)
        GPIO.output(13, 1)
        GPIO.output(16, 0)
        GPIO.output(17, 0)
        time.sleep(0.1)
        ser.write('0'.encode());  # *****************
