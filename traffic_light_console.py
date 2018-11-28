import RPi.GPIO as GPIO
import pickle
from time import sleep

M1 = 11
K1 = 13
H1 = 15

M2 = 16
K2 = 18
H2 = 22

M3 = 33
K3 = 35
H3 = 37

M4 = 36
K4 = 38
H4 = 40

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(M1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(K1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(H1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(M2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(K2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(H2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(M3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(K3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(H3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(M4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(K4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(H4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

class isc:
    M = 0
    K = 0
    H = 0
    
    def red(self):
        GPIO.output(self.M, GPIO.HIGH)
        GPIO.output(self.K, GPIO.LOW)
        GPIO.output(self.H, GPIO.LOW)
        #print("red")
    
    def yellow(self):
        GPIO.output(self.M, GPIO.LOW)
        GPIO.output(self.K, GPIO.HIGH)
        GPIO.output(self.H, GPIO.LOW)
        #print("yellow")
    
    def green(self):
        GPIO.output(self.M, GPIO.LOW)
        GPIO.output(self.K, GPIO.LOW)
        GPIO.output(self.H, GPIO.HIGH)
        #print("green")

    def __init__(self, pM, pK, pH):
        self.M = pM
        self.K = pK
        self.H = pH

isc1 = isc(M1, K1, H1)
isc1.green()
isc2 = isc(M2, K2, H2)
isc2.red()
isc3 = isc(M3, K3, H3)
isc3.red()
isc4 = isc(M4, K4, H4)
isc4.red()
next = isc(0, 0, 0)
prev = isc1

def toggle_isc(next_isc, prev_isc):
    next_isc.yellow()
    prev_isc.yellow()
    sleep(2)
    next_isc.green()
    prev_isc.red()

##while True:
##    try:
##        b = 1
##        _in = int(input())
##        
##        #fl = open("lampstate.pickle", "rb")
##        #_in = pickle.load(fl)
##        
##        if _in == 1:
##            next = isc1
##        elif _in == 2:
##            next = isc2
##        elif _in == 3:
##            next = isc3
##        elif _in == 4:
##            next = isc4
##        else:
##            b = 0
##            pass
##        
##        if b == 1:
##            #print("intersection " + str(_in) + " -> ON")
##            toggle_isc(next, prev)
##            prev = next
##    
##    except:
##        print("salah")
    
while True:
    toggle_isc(isc2, isc1)
    sleep(30)
    toggle_isc(isc3, isc2)
    sleep(45)
    toggle_isc(isc4, isc3)
    sleep(35)
    toggle_isc(isc1, isc4)
    sleep(40)
    
        
