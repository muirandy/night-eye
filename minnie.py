from picamera import PiCamera
from gpiozero import MotionSensor
from gpiozero import LED
from time import sleep

camera = PiCamera()
sensor = MotionSensor(4)

cameraNightMode = LED(19)
cameraNightMode.off()

for i in range(2):
    sensor.wait_for_motion()
    print("minnie")
    # camera.start_recording('/home/pi/Desktop/minnieVideo' + i + '.h264')
    # sleep(10)
    # camera.stop_recording()
