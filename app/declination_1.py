import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor_1_A1_pin = 12 # black
motor_1_A2_pin = 16 # yellow
motor_1_B1_pin = 20 # green
motor_1_B2_pin = 21 # white

motor_2_A1_pin = 18 # black
motor_2_A2_pin = 23 # yellow
motor_2_B1_pin = 24 # green
motor_2_B2_pin = 25 # white


# adjust if different
StepCount = 8
Seq1 = list(range(0, StepCount))
Seq1[0] = [0,1,0,0]
Seq1[1] = [0,1,0,1]
Seq1[2] = [0,0,0,1]
Seq1[3] = [1,0,0,1]
Seq1[4] = [1,0,0,0]
Seq1[5] = [1,0,1,0]
Seq1[6] = [0,0,1,0]
Seq1[7] = [0,1,1,0]

Seq2 = list(range(0, StepCount))
Seq2[7] = [0,1,0,0]
Seq2[6] = [0,1,0,1]
Seq2[5] = [0,0,0,1]
Seq2[4] = [1,0,0,1]
Seq2[3] = [1,0,0,0]
Seq2[2] = [1,0,1,0]
Seq2[1] = [0,0,1,0]
Seq2[0] = [0,1,1,0]
 
 
GPIO.setup(motor_1_A1_pin, GPIO.OUT)
GPIO.setup(motor_1_A2_pin, GPIO.OUT)
GPIO.setup(motor_1_B1_pin, GPIO.OUT)
GPIO.setup(motor_1_B2_pin, GPIO.OUT)

GPIO.setup(motor_2_A1_pin, GPIO.OUT)
GPIO.setup(motor_2_A2_pin, GPIO.OUT)
GPIO.setup(motor_2_B1_pin, GPIO.OUT)
GPIO.setup(motor_2_B2_pin, GPIO.OUT)
 
 
def setStep(w1, w2, w3, w4):
    GPIO.output(motor_1_A1_pin, w1)
    GPIO.output(motor_1_A2_pin, w2)
    GPIO.output(motor_1_B1_pin, w3)
    GPIO.output(motor_1_B2_pin, w4)
    
def setStep2(w1, w2, w3, w4):
    GPIO.output(motor_2_A1_pin, w1)
    GPIO.output(motor_2_A2_pin, w2)
    GPIO.output(motor_2_B1_pin, w3)
    GPIO.output(motor_2_B2_pin, w4)
 
def forward(delay, steps):
    for i in list(range(steps)):
        for j in list(range(StepCount)):
            setStep(Seq1[j][0], Seq1[j][1], Seq1[j][2], Seq1[j][3])
            setStep2(Seq2[j][0], Seq2[j][1], Seq2[j][2], Seq2[j][3])
            time.sleep(delay/1000.0)
 
def backwards(delay, steps):
    for i in list(range(steps)):
        for j in reversed(list(range(StepCount))):
            setStep(Seq1[j][0], Seq1[j][1], Seq1[j][2], Seq1[j][3])
            setStep2(Seq2[j][0], Seq2[j][1], Seq2[j][2], Seq2[j][3])
            time.sleep(delay/1000.0)
 

 
