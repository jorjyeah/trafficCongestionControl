import numpy as np
import cv2
import base64
import requests
import socket
import struct
import pickle
import zlib
import time
import RPi.GPIO as GPIO
from time import sleep

#API_ENDPOINT = "http://192.168.43.47/traffic_congestion"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.137.1',8485))
connection = client_socket.makefile('wb')


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(3, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3, False)
    pwm.ChangeDutyCycle(0)
    
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
count = 0
interval = 10
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

def Capture(count,cam1,cam2):
    r, frame1 = cap1.read()
    l, frame2 = cap2.read()
    if r:
        nama_file1 = "cam_"+str(cam1)+"_"+str(count)
        print(nama_file1)
        #cv2.imwrite(nama_file1+".jpg",frame1)
        r, buffer1 = cv2.imencode(nama_file1+".jpg",frame1, encode_param)
        print(buffer1)
        #jpg_as_text1 = base64.b64encode(buffer1)
        #print(jpg_as_text1)

        print(str(cam1))
        print(str(count))
        
        data1 = pickle.dumps(buffer1,0)
        size1 = len(data1)
        
        print("{}: {}".format(cam1, size1))
        client_socket.sendall(struct.pack(">L", size1) + data1)
        
        #data1 = {'selector_camera' : str(cam1),'iteration' : str(count),'image' : buffer1}
        #print(data1)
        #response1 = requests.post(url = API_ENDPOINT, data = data1)
        #print(response1.status_code, response1.reason, response1.text)
        #pastebin_url = response1.text
        
    if l:
        nama_file2 = "cam_"+str(cam2)+"_"+str(count)
        print(nama_file2)
        #cv2.imwrite(nama_file2+".jpg",frame2)
        l, buffer2 = cv2.imencode(nama_file2+".jpg",frame2, encode_param)
        print(buffer2)
        #jpg_as_text2 = base64.b64encode(buffer2)
        #print(jpg_as_text2)
        
        print(str(cam2))
        print(str(count))
        
        data2 = pickle.dumps(buffer2,0)
        size2 = len(data2)
        
        print("{}: {}".format(cam2, size2))
        client_socket.sendall(struct.pack(">L", size2) + data2)
        
        #data2 = {'selector_camera':str(cam2),'iteration': str(count),'image' : buffer2}
        #print(data2)
        #response2 = requests.post(url = API_ENDPOINT, data = data2)
        #print(response2.status_code, response2.reason, response2.text)
        #pastebin_url = response2.text
        
          
while(True):
    print(count)
    
    SetAngle(90)
    Capture(count,1,2)
    sleep(2)
    
    SetAngle(160)
    Capture(count,3,4)
    sleep(2)
    
    count+=1