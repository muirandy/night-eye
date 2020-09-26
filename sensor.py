from gpiozero import MotionSensor
from time import sleep

sensor = MotionSensor(4)

sleep(10)
sensor.wait_for_motion()
print("dog")