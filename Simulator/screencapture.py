import cv2
import numpy as np
import pyautogui
import imutils

#cv2.namedWindow("Result")
#cv2.moveWindow("Result", 0, 500)

class InputControl:
    def __init__(self):
        pass
        
    def VideoCapture():
        webcam = cv2.VideoCapture(1)

        assert webcam.isOpened(), "Webcam is not connected"

        status, frame = webcam.read()
        
        if status:
            frame = imutils.resize(frame, height=480, width=640)
            cv2.imshow('frame', frame)
            return frame

            
    def ScreenCapture():
        capt = pyautogui.screenshot(region=(0,0,640,480))    
        img_frame = np.array(capt)
        img_frame = cv2.cvtColor(img_frame, cv2.COLOR_RGB2BGR)
        cv2.imshow('frame', img_frame)
        return img_frame

if __name__ =="__main__":
    while 1:
        InputControl.ScreenCapture()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


