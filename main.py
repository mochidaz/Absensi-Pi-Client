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

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    elif cv2.waitKey(1) & 0xFF == ord('a'):
        cv2.imwrite("/tmp/wajah.png", frame)

        url = "http://0.0.0.0:5001"
        files = {"file":open("/tmp/wajah.png", 'rb')}

        # POST request
        r = requests.post(url, files=files).json()

        os.system(f"echo {r} >> test.json")

        if r['NIS'] == 'Unkown':
            os.system("espeak 'Mohon Ulangi kembali'")
        else:
            os.system("espeak 'Terima kasih, nis anda, {} telah diterima' ".format(r['NIS']))

        print(r)



video_capture.release()
cv2.destroyAllWindows()

