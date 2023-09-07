import cv2
import cvzone

# Initialize camera capture
cap = cv2.VideoCapture(2)

# Start an infinite loop to continually capture frames
while True:
    # Read image frame from camera
    success, img = cap.read()

    # Convert the image to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize the image to be smaller (0.1x of original size)
    imgSmall = cv2.resize(img, (0, 0), None, 0.1, 0.1)

    # Resize the image to be larger (3x of original size)
    imgBig = cv2.resize(img, (0, 0), None, 3, 3)

    # Apply Canny edge detection on the grayscale image
    imgCanny = cv2.Canny(imgGray, 50, 150)

    # Convert the image to HSV color space
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create a list of all processed images
    imgList = [img, imgGray, imgCanny, imgSmall, imgBig, imgHSV]

    # Stack the images together using cvzone's stackImages function
    stackedImg = cvzone.stackImages(imgList, 3, 0.7)

    # Display the stacked images
    cv2.imshow("stackedImg", stackedImg)

    # Wait for 1 millisecond; this also allows for keyboard inputs
    cv2.waitKey(1)