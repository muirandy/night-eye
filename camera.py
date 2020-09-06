from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.image_effect = 'gpen'
camera.start_preview()

camera.start_recording('/home/pi/Desktop/p_video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()