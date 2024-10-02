from PIL import ImageGrab
import numpy as np
import cv2
import datetime
import time
import winsound
import json

width, height= 1920, 1080
fps, prev = 10, 0 

timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')


fourcc = cv2.VideoWriter_fourcc(*"XVID")
captured_video = cv2.VideoWriter(f'D:\Virtual Assistant\Recording Datas\{timestamp}.avi', fourcc, 20.0, (width, height))

webcam = cv2.VideoCapture(0)

while True:
        with open('D:\Virtual Assistant\Database\ScreenRecord.json', 'r') as f:
                stopRecordCalled = json.load(f)

        if stopRecordCalled["stopRecordCalled"] == "True":
                winsound.PlaySound('D:\Virtual Assistant\Database\AlarmSound.wav', winsound.SND_FILENAME)
                break

        
        time_elapsed = time.time() - prev

        if time_elapsed > 1.0/fps:

                prev = time.time()

                img = ImageGrab.grab(bbox=(0, 0, width, height))
                img_np = np.array(img)
                img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
                _, frame = webcam.read()
                fr_height, fr_width, _ = frame.shape
                img_final[0:fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :]

                captured_video.write(img_final)

        cv2.waitKey(10)
        


        # cv2.imshow('Capture', img_final)
        # if cv2.waitKey(10) == ord('q'):
        #         break

cv2.destroyAllWindows()
captured_video.release()
