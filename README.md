# CVZone


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
import cvzone
import cv2

cap = cv2.VideoCapture(0)
detector = cvzone.FaceDetector()
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
import cvzone
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = cvzone.HandDetector(detectionCon=0.5, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    # Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
</pre>

#### Finding How many finger are up
<pre>
if lmList:
        # Find how many fingers are up
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers:{totalFingers}', (bbox[0] + 200, bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
</pre>

#### Finding distance between two fingers
<pre>                 
if lmList:
        # Find Distance Between Two Fingers
        distance, img, info = detector.findDistance(8, 12, img)
        cv2.putText(img, f'Dist:{int(distance)}', (bbox[0] + 400, bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
</pre>

#### Find Hand Type - i.e. Left or Right 
<p align="center">
  <img width="320" height="180" src="https://github.com/cvzone/cvzone/blob/master/Results/LeftHand.jpg"> <img width="320" height="180" src="https://github.com/cvzone/cvzone/blob/master/Results/RightHand.jpg">
</p>



<pre>
if lmList:
        # Find Hand Type
        myHandType = detector.handType()
        cv2.putText(img, f'Hand:{myHandType}', (bbox[0], bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

</pre>

<hr>

### Pose Estimation

<hr>

<p align="center">
  <img width="640" height="360" src="https://www.computervision.zone/wp-content/uploads/2021/04/vlcsnap-2021-03-27-22h34m51s546.jpg">
</p>

<pre>
import cvzone
import cv2

cap = cv2.VideoCapture(0)
detector = cvzone.PoseDetector(upBody=True)
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
import cvzone
import cv2

cap = cv2.VideoCapture(0)
detector = cvzone.FaceMeshDetector(maxFaces=2)
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
import cv2

cap = cv2.VideoCapture(0)
detector = cvzone.HandDetector()

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
    cv2.waitKey(1)
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
    cv2.waitKey(1)
</pre>

