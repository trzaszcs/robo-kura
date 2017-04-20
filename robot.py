from gopigo import *
import time


def hello():
 forward()
 time.sleep(.5)
 stop()

def distance_sensor():
  distance_sensor_pin = analogPort
  while True:
    try:
        print (us_dist(distance_sensor_pin))
        time.sleep(.5)

    except IOError:
        print ("Error")

def dziob()
 enable_servo()
 servo(80)
 time.sleep(0.3)
 servo(25)
 time.sleep(1)

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
 

print("start")
enable_com_timeout(2000)
distance_sensor_test()
print("end")
