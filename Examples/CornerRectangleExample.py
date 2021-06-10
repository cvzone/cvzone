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
    cv2.waitKey(1)
