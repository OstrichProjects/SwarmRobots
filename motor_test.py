#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, 0)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, 0)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, 0)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, 0)

GPIO.output(11, 1)
GPIO.output(13, 1)
sleep(2)
GPIO.output(11, 0)
GPIO.output(13, 0)
GPIO.output(12, 1)
GPIO.output(15, 1)
sleep(2)
GPIO.output(12, 0)
GPIO.output(11, 1)
sleep(2)
GPIO.output(11, 0)
GPIO.output(12, 1)
GPIO.output(15, 0)
GPIO.output(13, 1)
sleep(2)
GPIO.output(12, 0)
GPIO.output(13, 0)

