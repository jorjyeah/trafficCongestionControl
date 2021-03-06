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
import multiprocessing

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

def cam1Stream():
    #define connections
    server_ip = '192.168.43.133'

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip,8498))
    connection = client_socket.makefile('wb')

    #count = 0
    interval = 10
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]



    while True:
        ret1, frame1 = cap1.read()
        #ret2, frame2 = cap2.read()
        
        ret1, buffer1 = cv2.imencode("dummy"+".jpg",frame1, encode_param)
        
        data1 = pickle.dumps(buffer1,0)
        size1 = len(data1)
        
        #print("{}: {}".format(cam1, size1))
        print("dadawdaw")
        client_socket.sendall(struct.pack(">L", size1) + data1)
        print("wewe")
        #cv2.imshow("frame1",frame1)
        #cv2.imshow("frame2",frame2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #sleep(5)
        
    cap1.release()
    #cap2.release()
    #cv2.destroyAllWindows()

def cam2Stream():
    #define connections
    server_ip = '192.168.43.133'

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip,8499))
    connection = client_socket.makefile('wb')

    #count = 0
    interval = 10
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]



    while True:
        #ret1, frame1 = cap2.read()
        ret2, frame2 = cap2.read()
        
        ret1, buffer1 = cv2.imencode("dummy"+".jpg",frame2, encode_param)
        
        data1 = pickle.dumps(buffer1,0)
        size1 = len(data1)
        
        #print("{}: {}".format(cam1, size1))
        print("dadawdaw")
        client_socket.sendall(struct.pack(">L", size1) + data1)
        print("wewe")
        #cv2.imshow("frame1",frame1)
        #cv2.imshow("frame2",frame2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #sleep(5)
        
    #cap1.release()
    cap2.release()
    #cv2.destroyAllWindows()


jobs = []
if __name__ == "__main__":
    pros1 = multiprocessing.Process(target = cam1Stream)
    pros2 = multiprocessing.Process(target = cam2Stream)
    jobs.append(pros1)
    jobs.append(pros2)
    pros1.start()
    pros2.start()