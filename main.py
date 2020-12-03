import face_recognition
import cv2
import numpy as np
import _thread
import time
from datetime import datetime as dt
import requests
import os
import requests
import pyttsx3
from database import Database
from datetime import datetime as dt
import busio
import board
import adafruit_amg88xx
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

db = Database()
video_capture = cv2.VideoCapture(0)

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
engine = pyttsx3.init()

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            name = "Unknown"

            face_names.append(name)
            

    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        #cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        #cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #font = cv2.FONT_HERSHEY_DUPLEX

    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('a'):
        cv2.imwrite("/tmp/wajah.png", frame)

        url = "http://192.168.6.201:5001"
        files = {"file":open("/tmp/wajah.png", 'rb')}

        # POST request
        r = requests.post(url, files=files).json()
        print(r)
        try:
            #q = db.getAll(r['NIS'])
            #print(q)
            #arr = []
            #count = 0
            #for i in q[0]:
            #    arr.append(i)
            #print("Data diri: ", arr)

            #nama = arr[0]
            #kelas = arr[1]
            #umur = arr[2]
            #nis = arr[3]
            #foto = arr[4]
            nama = r['Nama']
            kelas = r['Kelas']
            nis = r['NIS']
            timestamp = dt.now()

            while 0.0 in amg.pixels[0]:
                pass
            else:
                suhu = max(amg.pixels[0])
            # Insert ke database Kehadiran
            db.Kehadiran((nama, nis, kelas,suhu, timestamp))

            os.system(f"echo {r} >> test.json")
        except Exception as e:
            continue

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



video_capture.release()
cv2.destroyAllWindows()

