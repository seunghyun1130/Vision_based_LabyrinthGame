import cv2
import numpy as np
#import getwebcam
import imutils
import argparse
from collections import deque

class masking():
    def __init__(self):
        super().__init__()
        #CV2 is B, G, R

        lower_White = np.array([155, 155, 155])
        upper_White = np.array([255, 255, 255])

        lower_Black = np.array([0, 0, 0])
        upper_Black = np.array([100, 100, 100])

    def toRed(self, frame, color_mode=1):
        lower_Red = np.array([0, 0, 155])
        upper_Red = np.array([0, 0, 255])
        # lower_Red_hsv = np.array([161, 155, 84])
        # upper_Red_hsv = np.array([179, 255, 255])
        lower_Red_hsv1 = np.array([0, 100, 20])
        upper_Red_hsv1 = np.array([15, 255, 255])
        lower_Red_hsv2 = np.array([160, 100, 20])
        upper_Red_hsv2 = np.array([179, 255, 255])
        # lower_Red_hsv = np.array([160, 0, 75])
        # upper_Red_hsv = np.array([179, 255, 255])
         
        if color_mode is 0:
            mask_Red = cv2.inRange(frame, lower_Red, upper_Red)
        else:            
            blurred = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv_frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
            mask_Red1 = cv2.inRange(hsv_frame, lower_Red_hsv1, upper_Red_hsv1)
            mask_Red2 = cv2.inRange(hsv_frame, lower_Red_hsv2, upper_Red_hsv2)
            mask_Red = mask_Red1 + mask_Red2
            # mask_Red = cv2.inRange(hsv_frame, lower_Red_hsv, upper_Red_hsv)
            mask_Red = cv2.erode(mask_Red, None, iterations=7)
            mask_Red = cv2.dilate(mask_Red, None, iterations=7)

        processed_Red = cv2.bitwise_and(frame, frame, mask = mask_Red)
        return processed_Red, mask_Red
        
    def toGreen(self, frame, color_mode=1):
        lower_Green = np.array([0, 155, 0])
        upper_Green = np.array([0, 255, 0])
        lower_Green_hsv = np.array([25, 52, 72])
        upper_Green_hsv = np.array([102, 255, 255])

        if color_mode is 0:
            mask_Green = cv2.inRange(frame, lower_Green, upper_Green)
        else:
            blurred = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv_frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
            mask_Green = cv2.inRange(hsv_frame, lower_Green_hsv, upper_Green_hsv)

        processed_Green = cv2.bitwise_and(frame, frame, mask = mask_Green)
        #processed_Green = cv2.cvtColor(processed_Green, cv2.COLOR_HSV2BGR)
        return processed_Green

    def toWhite(self, frame, color_mode=1, sensitivity = 15):
        lower_White = np.array([200, 200, 200])
        upper_White = np.array([255, 255, 255])
        lower_White_hsv = np.array([0, 0, 255-sensitivity])
        upper_White_hsv = np.array([255, sensitivity, 255])
        lower_White_hls = np.array([0, 200, 0])
        upper_White_hls = np.array([255, 255, sensitivity])

        if color_mode is 0:
            mask_White = cv2.inRange(frame, lower_White, upper_White)
        elif color_mode is 2:
            hls_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
            mask_White = cv2.inRange(hls_frame, lower_White_hls, upper_White_hls)
        else:            
            blurred = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv_frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
            mask_White = cv2.inRange(hsv_frame, lower_White_hsv, upper_White_hsv)

        processed_White = cv2.bitwise_and(frame, frame, mask = mask_White)
        return processed_White
    
    def toBlack(self, frame, color_mode=1):
        lower_Black = np.array([200, 200, 200])
        upper_Black = np.array([255, 255, 255])
        lower_Black_hsv = np.array([0, 0, 0])
        upper_Black_hsv = np.array([179, 100, 130])
        lower_Black_hls = np.array([0, 200, 0])
        upper_Black_hls = np.array([50, 50, 100])

        if color_mode is 0:
            mask_Black = cv2.inRange(frame, lower_Black, upper_Black)
        elif color_mode is 2:
            hls_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
            mask_Black = cv2.inRange(hls_frame, lower_Black_hls, upper_Black_hls)
        else:            
            blurred = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv_frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
            mask_Black = cv2.inRange(hsv_frame, lower_Black_hsv, upper_Black_hsv)

        processed_Black = cv2.bitwise_and(frame, frame, mask = mask_Black)
        return processed_Black

if __name__=="__main__":
    webcam = cv2.VideoCapture(1)

    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", help="path to the (optional) video file")
    ap.add_argument("-b", "--buffer", type=int, default=64,	help="max buffer size")
    args = vars(ap.parse_args())
    pts = deque(maxlen=args["buffer"])

    assert webcam.isOpened(), "Webcam is not connected"

    while webcam.isOpened():
        status, frame = webcam.read()
        
        if status:
            frame = imutils.resize(frame, height=480, width=640)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            red, mask = masking().toRed(frame)
            green = masking().toGreen(frame)
            white = masking().toWhite(frame, color_mode=1)
            black = masking().toBlack(frame, color_mode=1)
            
                # find contours in the mask and initialize the current
        # (x, y) center of the ball
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            center = None
        # only proceed if at least one contour was found
            if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            # only proceed if the radius meets a minimum size
                if radius > 10:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                    cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)
        # update the points queue
            pts.appendleft(center)
            # loop over the set of tracked points
            for i in range(1, len(pts)):
            # if either of the tracked points are None, ignore
            # them
                if pts[i - 1] is None or pts[i] is None:
                    continue
            # otherwise, compute the thickness of the line and
            # draw the connecting lines
                thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
                cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

            #cv2.imshow("grayscale", gray)
            frame_array = np.array(frame)
            #print("frame array:", frame_array.shape)
            cv2.imshow('frame', frame)
            cv2.imshow('frame_numpy', frame_array)
            #cv2.imwrite('../frame_array.PNG', frame_array)
            #break
            cv2.imshow("Red", red)
            # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
            # hsv_frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
            # print(hsv_frame)
            #cv2.imshow("Green", green)
            #cv2.imshow("White", white)
            #cv2.imshow("Black", black)
            # break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()
    cv2.destroyAllWindows()