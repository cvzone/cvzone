Hand Tracking Module
====================

Overview
--------
The Hand Tracking Module in cvzone utilizes the MediaPipe library to detect hands and their landmarks in real-time video streams. It not only identifies hands and their key points but also provides functionalities such as counting fingers or calculating the distance between fingers, along with hand bounding box information.

Dependencies
------------
- cv2 (OpenCV)
- mediapipe
- math (for distance calculations)
- cvzone

Usage
-----
Make sure cvzone, OpenCV, and MediaPipe are installed to use this module.

Class: HandDetector
-------------------

Initialization
~~~~~~~~~~~~~~
.. code-block:: python

    def __init__(self, staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5):
        """
        Initializes the HandDetector with configurable settings.

        :param staticMode: Bool, processes each image frame if False.
        :param maxHands: Int, the maximum number of hands to detect.
        :param modelComplexity: Int, the complexity of the model, 0 or 1.
        :param detectionCon: Float, the minimum detection confidence threshold.
        :param minTrackCon: Float, the minimum tracking confidence threshold.
        """

- **staticMode**: Detection mode flag.
- **maxHands**: Maximum detectable hands in the frame.
- **modelComplexity**: Model complexity; higher values are more accurate but slower.
- **detectionCon**: Minimum confidence value for a detection to be considered successful.
- **minTrackCon**: Minimum confidence value for the tracking to be considered successful.

Methods
-------

**findHands**
.. code-block:: python

    def findHands(self, img, draw=True, flipType=True):
        """
        Detects hands and landmarks in a BGR image.

        :param img: The input image.
        :param draw: Bool, indicates whether to draw landmarks and connections.
        :param flipType: Bool, indicates whether to flip hand type labels (left/right).
        :return: A list of detected hands with details and the processed image.
        """

**fingersUp**
.. code-block:: python

    def fingersUp(self, myHand):
        """
        Determines which fingers are up for a detected hand.

        :param myHand: Dictionary containing details of the detected hand.
        :return: A list indicating which fingers are up.
        """

**findDistance**
.. code-block:: python

    def findDistance(self, p1, p2, img=None, color=(255, 0, 255), scale=5):
        """
        Calculates the distance between two landmarks.

        :param p1: Tuple, the first point (x, y).
        :param p2: Tuple, the second point (x, y).
        :param img: Optional, the image on which to draw.
        :param color: Tuple, the color of the drawn elements.
        :param scale: Int, the scale for drawn elements.
        :return: The distance, line information, and the optional image with drawing.
        """

Example Usage
-------------
.. code-block:: python

    if __name__ == "__main__":
        cap = cv2.VideoCapture(0)  # Initialize webcam
        detector = HandDetector()  # Create HandDetector object

        while True:
            success, img = cap.read()  # Read image frame
            hands, img = detector.findHands(img)  # Detect hands

            if hands:
                # Process detected hands
                for hand in hands:
                    print(detector.fingersUp(hand))  # Example: Print which fingers are up

            cv2.imshow("Hand Tracking", img)  # Display the image
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
                break

This documentation provides insights into the Hand Tracking Module's functionalities, including initialization parameters, key methods for detecting hands, identifying raised fingers, and measuring distances between landmarks. The example demonstrates real-time hand tracking in a video stream.
