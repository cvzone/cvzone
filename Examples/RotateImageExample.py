import cv2
from cvzone.Utils import rotateImage  # Import rotateImage function from cvzone.Utils

# Initialize the video capture
cap = cv2.VideoCapture(2)  # Capture video from the third webcam (index starts at 0)

# Start the loop to continuously get frames from the webcam
while True:
    # Read a frame from the webcam
    success, img = cap.read()  # 'success' will be True if the frame is read successfully, 'img' will contain the frame

    # Rotate the image by 60 degrees without keeping the size
    imgRotated60 = rotateImage(img, 60, scale=1,
                               keepSize=False)  # Rotate image 60 degrees, scale it by 1, and don't keep original size

    # Rotate the image by 60 degrees while keeping the size
    imgRotated60KeepSize = rotateImage(img, 60, scale=1,
                                       keepSize=True)  # Rotate image 60 degrees, scale it by 1, and keep the original size

    # Display the rotated images
    cv2.imshow("imgRotated60", imgRotated60)  # Show the 60-degree rotated image without keeping the size
    cv2.imshow("imgRotated60KeepSize", imgRotated60KeepSize)  # Show the 60-degree rotated image while keeping the size

    # Wait for 1 millisecond between frames
    cv2.waitKey(1)  # Wait for 1 ms, during which any key press can be detected (not being used here)
