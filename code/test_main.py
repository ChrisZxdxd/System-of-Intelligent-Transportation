import distinguish_body
import time
import cv2
import LightControlOne as lco
import gc
import number
# import serial
# ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)


message = """
1:启动识别程序
2:退出系统
"""
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)  # 树莓派改为2 

print('系统开始运行' )

while True:
    #print('%s' % message)
    gongneng = 1
    if gongneng == 1:
        lco.init() #初始化信号灯以及舵机
        num, pin = number.init() # 初始化数码管引脚
        number.work(num, pin, '.')
        print('开始识别，按‘q’终止识别')
        while True:
            a = distinguish_body.work(cap1, cap2)
            if a == 1:   #判断到有人后且达到放行条件
                lco.work(num, pin) #切换信号灯并开放舵机
                time.sleep(5)  # 放行一次后系统休眠一定时间
            elif a == 2:
                cv2.destroyAllWindows()
                print('识别结束')
                break
            gc.collect()

    elif gongneng == 2:
        print('系统已关闭')
        break
