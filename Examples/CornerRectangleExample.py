import cv2
import cvzone  # Importing the cvzone library


def open_camera(max_index=4):
    # Camera indices are assigned by the operating system and may differ by machine.
    for index in range(max_index):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print(f"Using camera index {index}")
            return cap
        cap.release()

    raise RuntimeError(
        f"No camera could be opened at indices 0-{max_index - 1}. "
        "Check that a camera is connected and that this app has permission to use it."
    )


cap = open_camera()

try:
    # Main loop to continuously capture frames
    while True:
        # Capture a single frame from the webcam
        success, img = cap.read()  # 'success' indicates whether the frame was captured successfully
        if not success or img is None:
            print("Could not read a frame from the camera.")
            break

        # Add a rectangle with styled corners to the image
        img = cvzone.cornerRect(
            img,  # The image to draw on
            (200, 200, 300, 200),  # Position and dimensions: x, y, width, height
            l=30,  # Length of the corner edges
            t=5,  # Thickness of the corner edges
            rt=1,  # Thickness of the rectangle
            colorR=(255, 0, 255),  # Color of the rectangle
            colorC=(0, 255, 0)  # Color of the corner edges
        )

        cv2.imshow("Image", img)  # Display the image in a window named "Image"

        # Wait for 1 millisecond between frames; press q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
