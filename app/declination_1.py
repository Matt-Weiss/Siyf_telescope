import RPi.GPIO as GPIO
import time

 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


dir_pin = 21
step_pin = 20
enable_pin = 16
microstep_pin = 26

GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(microstep_pin, GPIO.OUT)

GPIO.output(enable_pin, 1 ) 
GPIO.output(dir_pin, 1 )
GPIO.output(microstep_pin, 1 )

GPIO.output(enable_pin, 0 )
 
def forward(delay, steps):
    for i in list(range(steps)):
        GPIO.output(dir_pin, 0 )
        GPIO.output(step_pin, 1 )
        time.sleep(delay/1000)
        GPIO.output(step_pin, 0 )
        time.sleep(delay/1000)     
 
def backwards(delay, steps):
    for i in range(steps):
        GPIO.output(dir_pin, 1 )
        GPIO.output(step_pin, 1 )
        time.sleep(delay/1000)
        GPIO.output(step_pin, 0 )
        time.sleep(delay/1000)
     

 
