#!/usr/bin/env python
# -*- coding:utf-8 -*-
#carmain
import RPi.GPIO as GPIO
import time
import sys
import carmove
duty=50
enab_pin = [5,6]
inx_pin = [21,22,23,24]
####  inx_pin是控制端in的pin
LeftAhead_pin = inx_pin[0]
LeftBack_pin =  inx_pin[1]
RightAhead_pin =  inx_pin[2]
RightBack_pin =   inx_pin[3]
print("begin setup ena enb pin")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in enab_pin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)
####  初始化使能端pin，设置成高电平
ENA = GPIO.PWM(enab_pin[0],100) #设置5，6脚为pwm脚,且频率为100Hz
ENB = GPIO.PWM(enab_pin[1],100)
ENA.start(duty)
ENB.start(duty)
pin = None
for pin in inx_pin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)
####  初始化控制端pin，设置成低电平
print( "setup ena enb pin over")


while True:
    print("please input: ")
    myelect=input()
    carmove.main(myelect)
