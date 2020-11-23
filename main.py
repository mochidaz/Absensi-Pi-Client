import face_recognition
import cv2
import numpy as np
import _thread
import time

video_capture = cv2.VideoCapture(2)

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

def wait(delay):
    time.sleep(delay)
    print("Hello world")

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        if len(face_encodings) > 0:
            _thread.start_new_thread(wait, (5,))
            cv2.imwrite('/tmp/wajah.jpg',frame)

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
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    face_encodings.clear()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

from datetime import datetime as dt
import requests


url = "http://0.0.0.0:5001"
files = {"file":open("/tmp/wajah.jpg", 'rb')}

# POST request
r = requests.post(url, files=files).json()

print(r)

video_capture.release()
cv2.destroyAllWindows()

