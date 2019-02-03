# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:58:55 2019

@author: LUI8WX
"""

import cv2
video_capture = cv2.VideoCapture(0)


#video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
#video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
#video_capture.set(cv2.CAP_PROP_FPS, 30)


while True:

    ret, frame = video_capture.read()
    left = 300
    right = 600
    top = 300
    bottom = 600
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.rectangle(frame, (700, 350), (1000, 650), (0, 0, 255), 2)
    
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, 'A handsome boy!', (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.putText(frame, 'A ugly man!', (700 + 6, 650 - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
