import cvzone
import cv2

cap = cv2.VideoCapture(0)
detector = cvzone.PoseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if lmList:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
