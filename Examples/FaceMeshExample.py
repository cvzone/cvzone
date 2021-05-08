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
    cv2.waitKey(1)