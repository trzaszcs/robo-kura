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
enable_com_timeout(2000)
while True:
 sensor()
 break
print("end")
