
import numpy as np
import cv2
haar_cascade = cv2.CascadeClassifier('C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
# if u want to collect the data from the video then pass the url
# of the video in video capture fxn or if u want to collect the data from
# internal cam then pass 0 and for external cam write 1
cap = cv2.VideoCapture(0)
data = []


while cap.isOpened():
    # cap read is used to capture the single frame from the direct stream or video.
    _, img = cap.read()
    # convert BGR frame to Gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect the face in the frame.
    haar_faces = haar_cascade.detectMultiScale(gray,1.1, 4)
    for (x,y,w,h) in haar_faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        face = img[y:y+h,x:x+w,:]
        face = cv2.resize(face,  (50,50))
        print(len(data))
        if len(data) < 1000:
            data.append(face)

    cv2.imshow('result', img)
    # this program will end once it collect the 500 sample u can also change the size of the sample
    if cv2.waitKey(1) == 13 or len(data) >=500:

        break
# save all the collected data
np.save('with_mask111', data)
cap.release()

