import cvzone
import cv2

fpsReader = cvzone.FPS()
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    fps, img = fpsReader.update(img, pos=(50, 80), color=(0, 255, 0), scale=5, thickness=5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
