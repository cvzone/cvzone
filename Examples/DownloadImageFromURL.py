import cv2
import cvzone

imgNormal = cvzone.downloadImageFromUrl(
    url='https://github.com/cvzone/cvzone/blob/master/Results/shapes.png?raw=true')

imgPNG = cvzone.downloadImageFromUrl(
    url='https://github.com/cvzone/cvzone/blob/master/Results/cvzoneLogo.png?raw=true',
    keepTransparency=True)
imgPNG =cv2.resize(imgPNG,(0,0),None,3,3)

cv2.imshow("Image Normal", imgNormal)
cv2.imshow("Transparent Image", imgPNG)
cv2.waitKey(0)
