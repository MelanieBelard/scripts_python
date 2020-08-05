from gpiozero import MotionSensor
from gpiozero import LED
from picamera import PiCamera
from datetime import datetime
from time import sleep

pir      = MotionSensor(21)
camera   = PiCamera()
led      = LED(14)

while True:
    
    pir.wait_for_motion()
    
    t = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    print("Mouvement détecté à", t, "!")
    led.on()
    
    video = '/home/pi/video_mouvements/' + t + ".h264"
    camera.start_recording(video)
    
    fileName = '/home/pi/video_mouvements/' + t + ".jpeg"
    camera.capture(fileName)
    
    pir.wait_for_no_motion()
    
    t = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    print("Mouvement arrêté à", t, "!\n")
    led.off()
    
    camera.stop_recording()
