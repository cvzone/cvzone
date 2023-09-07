import cv2
import cvzone  # Importing the cvzone library

# Initialize the webcam
cap = cv2.VideoCapture(2)  # Capture video from the third webcam (0-based index)

# Main loop to continuously capture frames
while True:
    # Capture a single frame from the webcam
    success, img = cap.read()  # 'success' is a boolean that indicates if the frame was captured successfully, and 'img' contains the frame itself

    # Add a rectangle with styled corners to the image
    img = cvzone.cornerRect(
        img,  # The image to draw on
        (200, 200, 300, 200),  # The position and dimensions of the rectangle (x, y, width, height)
        l=30,  # Length of the corner edges
        t=5,  # Thickness of the corner edges
        rt=1,  # Thickness of the rectangle
        colorR=(255, 0, 255),  # Color of the rectangle
        colorC=(0, 255, 0)  # Color of the corner edges
    )

    # Show the modified image
    cv2.imshow("Image", img)  # Display the image in a window named "Image"

    # Wait for 1 millisecond between frames
    cv2.waitKey(1)  # Waits 1 ms for a key event (not being used here)
