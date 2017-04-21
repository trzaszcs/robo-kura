from gopigo import *
import time
from picamera import PiCamera

def run():
 distance_sensor_pin = analogPort
 enable_servo()
 
 def dist():
   return us_dist(distance_sensor_pin)
 
 def dziob():
  servo(80)
  time.sleep(0.3)
  servo(25)
  time.sleep(1)
  servo(80)
  time.sleep(0.3)
  servo(0)
 
 def step_forward():
  foward()
  time.sleep(.5)
  stop()

 def step_left():
   left()
   time.sleep(.5)
   stop()
 
 def step_right():
   right()
   time.sleep(.5)
   stop()

 # START LOOP
 step_forward()
 while True:
  current_dist = dist()
  if current_dist > 20:
    dziob()
    step_forward()
  else:
    step_left()
 
def hello():
 forward()
 time.sleep(.5)
 stop()

def cumshot():
 camera = PiCamera()
 camera.resolution = (1024, 768)
 camera.start_preview()
 # Camera warm-up time
 time.sleep(2)
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
dziob()
cumshot()
print("end")
