import cvzone
import cv2

cap = cv2.VideoCapture(0)
detector = cvzone.FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    print(bboxs)
    cv2.imshow("Image", img)
    cv2.waitKey(1)