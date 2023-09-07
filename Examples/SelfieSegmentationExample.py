import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import cv2

# Initialize the webcam. '2' indicates the third camera connected to the computer.
# '0' usually refers to the built-in camera.
cap = cv2.VideoCapture(2)

# Set the frame width to 640 pixels
cap.set(3, 640)
# Set the frame height to 480 pixels
cap.set(4, 480)

# Initialize the SelfiSegmentation class. It will be used for background removal.
# model is 0 or 1 - 0 is general 1 is landscape(faster)
segmentor = SelfiSegmentation(model=0)

# Infinite loop to keep capturing frames from the webcam
while True:
    # Capture a single frame
    success, img = cap.read()

    # Use the SelfiSegmentation class to remove the background
    # Replace it with a magenta background (255, 0, 255)
    # imgBG can be a color or an image as well. must be same size as the original if image
    # 'cutThreshold' is the sensitivity of the segmentation.
    imgOut = segmentor.removeBG(img, imgBg=(255, 0, 255), cutThreshold=0.1)

    # Stack the original image and the image with background removed side by side
    imgStacked = cvzone.stackImages([img, imgOut], cols=2, scale=1)

    # Display the stacked images
    cv2.imshow("Image", imgStacked)

    # Check for 'q' key press to break the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
