#!/usr/bin/python

import hal
import sys
import time

#Now we create the HAL component and its pins
c = hal.component("smart-board")
c.newpin("led1",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led2",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led3",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led4",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led5",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led6",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led7",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led8",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led9",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led10",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led11",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led12",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led13",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led14",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led15",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led16",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led17",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led18",hal.HAL_BIT,hal.HAL_OUT)
time.sleep(2)
c.ready()

count = 0
try:
  while 1:
    time.sleep(.01)
    count += 1
  
    if count == 10:
        c["led1"] = 1
    elif count == 20:
        c["led2"] = 1
    elif count == 30:
        c["led3"] = 1
    elif count == 40:
        c["led4"] = 1
    elif count == 50:
        c["led5"] = 1
    elif count == 60:
        c["led6"] = 1
    elif count == 70:
        c["led7"] = 1
    elif count == 80:
        c["led8"] = 1
    elif count == 90:
        c["led9"] = 1
    elif count == 100:
        c["led10"] = 1
    elif count == 110:
        c["led11"] = 1
    elif count == 120:
        c["led12"] = 1
    elif count == 130:
        c["led13"] = 1
    elif count == 140:
        c["led14"] = 1
    elif count == 150:
        c["led15"] = 1
    elif count == 160:
        c["led16"] = 1
    elif count == 170:
        c["led17"] = 1
    elif count == 180:
        c["led18"] = 1
    elif count == 190:
        c["led1"] = 0
        c["led2"] = 0
        c["led3"] = 0
        c["led4"] = 0
        c["led5"] = 0
        c["led6"] = 0
        c["led7"] = 0
        c["led8"] = 0
        c["led9"] = 0
        c["led10"] = 0
        c["led11"] = 0
        c["led12"] = 0
        c["led13"] = 0
        c["led14"] = 0
        c["led15"] = 0
        c["led16"] = 0
        c["led17"] = 0
        c["led18"] = 0
        count = 0
  
except KeyboardInterrupt:
    raise SystemExit

