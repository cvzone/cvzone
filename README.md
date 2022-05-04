# CVZone

[![Downloads](https://pepy.tech/badge/cvzone)](https://pepy.tech/project/cvzone)
[![Downloads](https://pepy.tech/badge/cvzone/month)](https://pepy.tech/project/cvzone)
[![Downloads](https://pepy.tech/badge/cvzone/week)](https://pepy.tech/project/cvzone)



This is a Computer vision package that makes its easy to run Image processing and AI functions. At the core it uses [OpenCV](https://github.com/opencv/opencv) and [Mediapipe](https://github.com/google/mediapipe) libraries. 

## Installation
You can  simply use pip to install the latest version of cvzone.

`pip install cvzone`

<hr>

### 60 FPS Face Detection

<hr>

<p align="center">
  <img width="640" height="360" src="https://www.computervision.zone/wp-content/uploads/2021/05/Face-Detection-2.jpg">
</p>

<pre>
from cvzone.FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)

    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

</pre>

<hr>

### Hand Tracking

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/cvzone/cvzone/blob/master/Results/Fingers-Distance.jpg">
</p>

#### Basic Code Example 
<pre>
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)

            # Find Distance between two Landmarks. Could be same hand or different hands
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
</pre>

 

<hr>

### Pose Estimation

<hr>

<p align="center">
  <img width="640" height="360" src="https://www.computervision.zone/wp-content/uploads/2021/04/vlcsnap-2021-03-27-22h34m51s546.jpg">
</p>

<pre>
from cvzone.PoseModule import PoseDetector
import cv2

cap = cv2.VideoCapture(0)
detector = PoseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
    if bboxInfo:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

</pre>


<hr>

### Face Mesh Detection

<hr>

<p align="center">
  <img width="640" height="360" src="https://www.computervision.zone/wp-content/uploads/2021/05/Face-Landmarks-2.jpg">
</p>

<pre>
from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    if faces:
        print(faces[0])
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
</pre>

<hr>

### Stack Images

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/cvzone/cvzone/blob/master/Results/ImageStack1.gif">
</p>

<pre>
import cvzone
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgList = [img, img, imgGray, img, imgGray, img,imgGray, img, img]
    stackedImg = cvzone.stackImages(imgList, 3, 0.4)

    cv2.imshow("stackedImg", stackedImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

</pre>

<hr>

### Corner Rectangle

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/cvzone/cvzone/blob/master/Results/cornerRect.jpg">
</p>

<hr>

<pre>
import cvzone
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    img = detector.findHands(img, draw=False)
    lmList, bbox = detector.findPosition(img, draw=False)
    if bbox:
        # Draw  Corner Rectangle
        cvzone.cornerRect(img, bbox)

    # Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

</pre>

### FPS

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/cvzone/cvzone/blob/master/Results/FPS.jpg">
</p>

<pre>
import cvzone
import cv2

fpsReader = cvzone.FPS()
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    fps, img = fpsReader.update(img,pos=(50,80),color=(0,255,0),scale=5,thickness=5)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
</pre>

