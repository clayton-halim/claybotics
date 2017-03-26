# import the necessary packages
import RPi.GPIO as GPIO
import numpy as np
import argparse
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import Motor

GPIO.setmode(GPIO.BCM)

Motor1EN = 13
Motor1A = 19
Motor1B = 26

Motor2EN = 16
Motor2A = 20
Motor2B = 21

motorRight = Motor.Motor(Motor1EN, Motor1A, Motor1B)
motorLeft = Motor.Motor(Motor2EN, Motor2A, Motor2B)

"""
GPIO.setup(Motor1EN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Motor1A, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor1B, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(Motor2EN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Motor2A, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor2B, GPIO.OUT, initial=GPIO.LOW)
"""
# initialize the current frame of the video, along with the list of
# ROI points along with whether or not this is input mode
frame = None
roiPts = []
inputMode = False
"""
def move_forward():
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1A, GPIO.HIGH)

    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.HIGH)

def move_backward():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
"""

def selectROI(event, x, y, flags, param):
    # grab the reference to the current frame, list of ROI
    # points and whether or not it is ROI selection mode
    global frame, roiPts, inputMode
 
    # if we are in ROI selection mode, the mouse was clicked,
    # and we do not already have four points, then update the
    # list of ROI points with the (x, y) location of the click
    # and draw the circle
    if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts) < 4:
        roiPts.append((x, y))
        cv2.circle(frame, (x, y), 4, (0, 255, 0), 2)
        cv2.imshow("frame", frame)

def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video",
        help = "path to the (optional) video file")
    args = vars(ap.parse_args())
 
    # grab the reference to the current frame, list of ROI
    # points and whether or not it is ROI selection mode
    global frame, roiPts, inputMode
 
    # if the video path was not supplied, grab the reference to the
    # camera
    if not args.get("video", False):
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))
        time.sleep(0.1)
 
    # otherwise, load the video
    else:
        camera = cv2.VideoCapture(args["video"])
 
    # setup the mouse callback
    cv2.namedWindow("frame")
    cv2.setMouseCallback("frame", selectROI)
 
    # initialize the termination criteria for cam shift, indicating
    # a maximum of ten iterations or movement by a least one pixel
    # along with the bounding box of the ROI
    termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    roiBox = None

    # keep looping over the frames
    for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the current frame
        frame = image.array
     
        
     
        # if the see if the ROI has been computed
        if roiBox is not None:
            # convert the current frame to the HSV color space
            # and perform mean shift
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            backProj = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1)
     
            # apply cam shift to the back projection, convert the
            # points to a bounding box, and then draw them
            (r, roiBox) = cv2.CamShift(backProj, roiBox, termination)
            
            # handle horizontal movement
            if roiBox[0] < 260:
                print("left")
            elif roiBox[0] > 300:
                print("right")
            else:
                print("center")
            
            # handle vertical movement
            if roiBox[1] < 200:
                print("up")
                motorRight.forward()
                motorLeft.forward()
            elif roiBox[1] > 250:
                print("down")
                motorRight.backward()
                motorLeft.backward()
            else:
                print("center")
                motorLeft.stop()
                motorRight.stop()
 
            pts = np.int0(cv2.boxPoints(r))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
    
        # show the frame and record if the user presses a key
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1) & 0xFF
         
        # handle if the 'i' key is pressed, then go into ROI
        # selection mode
        if key == ord("i") and len(roiPts) < 4:
            # indicate that we are in input mode and clone the
            # frame
            inputMode = True
            orig = frame.copy()
         
            # keep looping until 4 reference ROI points have
            # been selected; press any key to exit ROI selction
            # mode once 4 points have been selected
            while len(roiPts) < 4:
                cv2.imshow("frame", frame)
                cv2.waitKey(0)
         
            # determine the top-left and bottom-right points
            roiPts = np.array(roiPts)
            s = roiPts.sum(axis = 1)
            tl = roiPts[np.argmin(s)]
            br = roiPts[np.argmax(s)]
         
            # grab the ROI for the bounding box and convert it
            # to the HSV color space
            roi = orig[tl[1]:br[1], tl[0]:br[0]]
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            #roi = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB)
         
            # compute a HSV histogram for the ROI and store the
            # bounding box
            roiHist = cv2.calcHist([roi], [0], None, [16], [0, 180])
            roiHist = cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
            roiBox = (tl[0], tl[1], br[0], br[1])
         
        # if the 'q' key is pressed, stop the loop
        elif key == ord("q"):
            break

        rawCapture.truncate(0)

    # cleanup the camera and close any open windows
    motorLeft.stop()
    motorRight.stop()
    GPIO.cleanup()
    camera.release()
    cv2.destroyAllWindows()


     
if __name__ == "__main__":
    main()
    GPIO.cleanup()
