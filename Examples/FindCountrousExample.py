import cv2           # Importing the OpenCV library for computer vision tasks
import cvzone       # Importing the cvzone library for additional functionalities
import numpy as np  # Importing NumPy library for numerical operations

# Download an image containing shapes from a given URL
imgShapes = cvzone.downloadImageFromUrl(
    url='https://github.com/cvzone/cvzone/blob/master/Results/shapes.png?raw=true')

# Perform edge detection using the Canny algorithm
imgCanny = cv2.Canny(imgShapes, 50, 150)

# Dilate the edges to strengthen the detected contours
imgDilated = cv2.dilate(imgCanny, np.ones((5, 5), np.uint8), iterations=1)

# Find contours in the image without any corner filtering
imgContours, conFound = cvzone.findContours(
    imgShapes, imgDilated, minArea=1000, sort=True,
    filter=None, drawCon=True, c=(255, 0, 0), ct=(255, 0, 255),
    retrType=cv2.RETR_EXTERNAL, approxType=cv2.CHAIN_APPROX_NONE)

# Find contours in the image and filter them based on corner points (either 3 or 4 corners)
imgContoursFiltered, conFoundFiltered = cvzone.findContours(
    imgShapes, imgDilated, minArea=1000, sort=True,
    filter=[3, 4], drawCon=True, c=(255, 0, 0), ct=(255, 0, 255),
    retrType=cv2.RETR_EXTERNAL, approxType=cv2.CHAIN_APPROX_NONE)

# Display the image with all found contours
cv2.imshow("imgContours", imgContours)

# Display the image with filtered contours (either 3 or 4 corners)
cv2.imshow("imgContoursFiltered", imgContoursFiltered)

# Wait until a key is pressed to close the windows
cv2.waitKey(0)
