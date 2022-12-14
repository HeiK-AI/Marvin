#!/usr/bin/python3
# coding: utf-8


import pigpio
import time



pi = pigpio.pi()
pin = 26
pi.set_mode(pin, pigpio.OUTPUT) 

dc = 192 #duty cycle between 0 and 255

pi.set_PWM_frequency(pin,8000) #frequenz between 10 to 8000Hz

print(pi.get_PWM_frequency(pin))

pi.set_PWM_dutycycle(pin,dc)

#for dc in range (255):
#	pi.set_PWM_dutycycle(pin,dc)
#	dc=dc+1
#	time.sleep(.1)
#	print(dc)


time.sleep(30)
pi.write(pin,0)
pi.stop()
