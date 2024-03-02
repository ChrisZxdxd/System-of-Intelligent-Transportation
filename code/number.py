# 初始化
import RPi.GPIO as GPIO
import time

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    pin = [18, 19, 20, 21, 22, 23, 24, 25]
    for i in range(8):
        GPIO.setup(pin[i], GPIO.OUT)
    num = {}
    num['0'] = '00000011'
    num['1'] = '10011111'
    num['2'] = '00100101'
    num['3'] = '00001101'
    num['4'] = '10011001'
    num['5'] = '01001001'
    num['6'] = '01000001'
    num['7'] = '00011111'
    num['8'] = '00000001'
    num['9'] = '00001001'
    num['.'] = '11111111'
    return num, pin

def draw(str1, num, pin):
    n = num[str1]
    for i in range(8):
        x = int(pin[i])  # 引脚位置
        y = int(n[i])   # 引脚状态
        GPIO.output(x, y)


def work(num, pin, show_str='.', a=0):
    idx = 0
    flag = True
    while flag:
        draw(show_str[idx], num, pin)
        idx = idx + 1
        if idx >= len(show_str):
            flag = False
        time.sleep(a)
