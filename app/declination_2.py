import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor_2_A1_pin = 18 # black
motor_2_A2_pin = 23 # yellow
motor_2_B1_pin = 24 # green
motor_2_B2_pin = 25 # white

# adjust if different
StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]
 
GPIO.setup(motor_2_A_1_pin, GPIO.OUT)
GPIO.setup(motor_2_A_2_pin, GPIO.OUT)
GPIO.setup(motor_2_B_1_pin, GPIO.OUT)
GPIO.setup(motor_2_B_2_pin, GPIO.OUT)
 
 
def setStep(w1, w2, w3, w4):
    GPIO.output(motor_2_A_1_pin, w1)
    GPIO.output(motor_2_A_2_pin, w2)
    GPIO.output(motor_2_B_1_pin, w3)
    GPIO.output(motor_2_B_2_pin, w4)
 
def forward(delay, steps):
    for i in list(range(steps)):
        for j in reversed(list(range(StepCount))):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay/1000.0)
 
def backwards(delay, steps):
    for i in list(range(steps)):
        for j in list(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay/1000.0)
 

 

