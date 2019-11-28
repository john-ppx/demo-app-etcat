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
c.newpin("led19",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led20",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led21",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led22",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led23",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led24",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led25",hal.HAL_BIT,hal.HAL_OUT)
c.newpin("led26",hal.HAL_BIT,hal.HAL_OUT)
time.sleep(2)
c.ready()

count = 0
try:
  while 1:
    time.sleep(.01)
    count += 1
  
    for i in range(1, 27):
        if count == (i * 10):
            c["led" + str(i)] = 1
        elif count == 270 :
            for j in range(1, 27):
                c["led" + str(j)] = 0
            count = 0
  
except KeyboardInterrupt:
    raise SystemExit

