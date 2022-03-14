# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:20:54 2022

@author: havci
"""

import cv2 as cv


capture = cv.VideoCapture(0)
while True:
    ret, frame = capture.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("frame", frame)
    if cv.waitKey(1)==ord('q'):
        break
capture.release()
cv.destroyAllWindows()