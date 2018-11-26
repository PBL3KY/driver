import RPi.GPIO as GPIO
import pigpio

GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.OUT)
#GPIO.setup(19, GPIO.OUT)
gpio_pin0 = 18
gpio_pin1 = 19

pi = pigpio.pi()
pi.set_mode(gpio_pin0, pigpio.OUTPUT)
pi.set_mode(gpio_pin1, pigpio.OUTPUT)
#pwm1 = GPIO.PWM(18, 1000)
#pwm2 = GPIO.PWM(19, 1000)
flg=0
#Rota=0 停止
#Rota=1 前進
#Rota=2 後退
#Rota=3 ブレーキ
#Speed=0~100%
class Motor_Rotation:
    def L_Rota(self,Rota,Speed):
        flg=0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        if Rota==0:
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
        elif Rota==1:
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
        elif Rota==2:
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
        elif Rota==3:
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
        else:
            print("L_Rota_Errer")
            flg=1
        if Speed>=0 and Speed<=100 and flg==0:
            #pwm1.start(Speed)
            sp=Speed*10000
            pi.hardware_PWM(gpio_pin0, 1000, sp)
        else:
            print("L_Speed_Errer")
        print(Rota)
        print(Speed)
    def R_Rota(self,Rota,Speed):
        flg=0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)
        if Rota==0:
            GPIO.output(20, GPIO.LOW)
            GPIO.output(21, GPIO.LOW)
        elif Rota==1:
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(21, GPIO.LOW)
        elif Rota==2:
            GPIO.output(20, GPIO.LOW)
            GPIO.output(21, GPIO.HIGH)
        elif Rota==3:
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(21, GPIO.HIGH)
        else:
            print("R_Rota_Errer")
            flg=1
        if Speed>=0 and Speed<=100 and flg==0:
            #pwm2.start(Speed)
            sp=Speed*10000
            pi.hardware_PWM(gpio_pin1, 1000, sp)
        else:
                print("R_Speed_Errer")
        print(Rota)
        print(Speed)

