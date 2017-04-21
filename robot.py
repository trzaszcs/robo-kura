from gopigo import *
import time
from picamera import PiCamera

def hello():
 forward()
 time.sleep(.5)
 stop()

def cumshot():
 camera = PiCamera()
 camera.resolution = (48, 32)
 camera.color_effects = (128,128)
 camera.start_preview()
 # Camera warm-up time
 # time.sleep(2)
 camera.capture('foo.jpg')

def distance_sensor():
  distance_sensor_pin = analogPort
  while True:
    try:
        print (us_dist(distance_sensor_pin))
        time.sleep(.5)

    except IOError:
        print ("Error")

def dziob():
 enable_servo()
 servo(80)
 time.sleep(0.3)
 servo(25)
 time.sleep(1)
 servo(80)
 time.sleep(0.3)
 servo(0)



def distance_sensor_test():
  distance_sensor_pin = analogPort
  while True:
    try:
        distance = us_dist(distance_sensor_pin)
        if distance < 5:
	  led_on(1)
	else:
	  lef_off(1)
        time.sleep(.5)

    except IOError:
        print ("Error")

def motion_sensor():
 motion_sensor_pin = 0
 pinMode(motion_sensor_pin,"INPUT")
 while True:
   try:
     print (digitalRead(motion_sensor_pin))
     time.sleep(.5)
   except IOError:
     print ("Error") 

print("start")
enable_com_timeout(2000)
hello()
dziob()
cumshot()
print("end")
