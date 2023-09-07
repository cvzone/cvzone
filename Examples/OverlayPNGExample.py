import cv2
import cvzone

# Initialize camera capture
cap = cv2.VideoCapture(2)

imgPNG = cvzone.downloadImageFromUrl(
    url='https://github.com/cvzone/cvzone/blob/master/Results/cvzoneLogo.png?raw=true',
    keepTransparency=True)

while True:
    # Read image frame from camera
    success, img = cap.read()

    imgOverlay = cvzone.overlayPNG(img, imgPNG, pos=[-30, 50])
    imgOverlay = cvzone.overlayPNG(img, imgPNG, pos=[200, 200])
    imgOverlay = cvzone.overlayPNG(img, imgPNG, pos=[500, 400])

    cv2.imshow("imgOverlay", imgOverlay)
    cv2.waitKey(1)