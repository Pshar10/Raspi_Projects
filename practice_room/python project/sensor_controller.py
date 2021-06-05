from fake_gpio import GPIO # For testing in PC
# import RPi.GPIO as GPIO # For testing in Raspberry Pi
import time

class SensorController:

  def __init__(self):
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    self.distance = None
    print('Sensor controller initiated')

  def track_rod(self):
    # ...
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(self.PIN_ECHO, GPIO.IN)
    GPIO.output(self.PIN_TRIGGER, GPIO.LOW)    
    print( "Waiting for sensor to settle")
    # time.sleep(2)
    print('Monitoring')
    GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
    pulse_start_time = 0
    pulse_end_time = 0
    while GPIO.input(self.PIN_ECHO)==0:
            pulse_start_time = time.time()
    while GPIO.input(self.PIN_ECHO)==1:
            pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    self.distance = round(pulse_duration * 171.50, 2)
    

  def get_distance(self):
    return self.distance