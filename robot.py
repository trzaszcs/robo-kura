from gopigo import *
import time


def hello():
 forward()
 time.sleep(.5)
 stop()

def sensor():
  distance_sensor_pin = gopigo.analogPort
  while True:
    try:
        print (gopigo.us_dist(distance_sensor_pin))
        time.sleep(.5)

    except IOError:
        print ("Error")

print("start")
while True:
 hello()
 break
print("end")
