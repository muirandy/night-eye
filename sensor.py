from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

camera = PiCamera()
sensor = MotionSensor(4)

#sleep(10)
sensor.wait_for_motion()
print("dog")
camera.capture('/home/pi/Desktop/sensor5.jpg')