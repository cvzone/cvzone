import cv2
import cvzone  # Importing the cvzone library

# Initialize the webcam
cap = cv2.VideoCapture(2)  # Capture video from the third webcam (0-based index)

# Main loop to continuously capture frames
while True:
    # Capture a single frame from the webcam
    success, img = cap.read()  # 'success' is a boolean that indicates if the frame was captured successfully, and 'img' contains the frame itself

    # Add a rectangle and put text inside it on the image
    img, bbox = cvzone.putTextRect(
        img, "CVZone", (50, 50),  # Image and starting position of the rectangle
        scale=3, thickness=3,  # Font scale and thickness
        colorT=(255, 255, 255), colorR=(255, 0, 255),  # Text color and Rectangle color
        font=cv2.FONT_HERSHEY_PLAIN,  # Font type
        offset=10,  # Offset of text inside the rectangle
        border=5, colorB=(0, 255, 0)  # Border thickness and color
    )

    # Show the modified image
    cv2.imshow("Image", img)  # Display the image in a window named "Image"

    # Wait for 1 millisecond between frames
    cv2.waitKey(1)  # Waits 1 ms for a key event (not being used here)
