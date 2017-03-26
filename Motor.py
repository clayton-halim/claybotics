import RPi.GPIO as GPIO

class Motor():
    def __init__(self, pinEN, pinA, pinB):
        self.pinEN = pinEN
        self.pinA = pinA
        self.pinB = pinB
        GPIO.setup(pinEN, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(pinA, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pinB, GPIO.OUT, initial=GPIO.LOW)

    def forward(self):
        GPIO.output(self.pinB, GPIO.LOW)
        GPIO.output(self.pinA, GPIO.HIGH)
        
    def backward(self):
        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.LOW)
        
        
    
