Pose Module
===========

Overview
--------
The Pose Module utilizes the MediaPipe library to estimate human pose points in real-time. It provides functionalities for detecting up to 33 body landmarks, allowing for a wide range of applications including motion analysis, fitness applications, and interactive installations.

Dependencies
------------
- cv2 (OpenCV)
- mediapipe
- math

Features
--------
- Real-time pose estimation with configurable settings.
- Supports static image mode and smooth landmark options.
- Optional segmentation for enhanced landmark visibility.
- Methods for landmark position retrieval, distance measurement between landmarks, and angle calculation among three landmarks.

Class: PoseDetector
-------------------

Initialization
~~~~~~~~~~~~~~
.. code-block:: python

    def __init__(self, staticMode=False, modelComplexity=1, smoothLandmarks=True,
                 enableSegmentation=False, smoothSegmentation=True, detectionCon=0.5,
                 trackCon=0.5):
        """
        Initializes the PoseDetector with customizable detection and tracking settings.

        :param staticMode: Boolean, operates in static mode if True.
        :param modelComplexity: Integer, model complexity level (0, 1).
        :param smoothLandmarks: Boolean, enables landmark smoothing.
        :param enableSegmentation: Boolean, enables body segmentation.
        :param smoothSegmentation: Boolean, applies smoothing to segmentation.
        :param detectionCon: Float, minimum detection confidence threshold.
        :param trackCon: Float, minimum tracking confidence threshold.
        """

Methods
-------

**findPose**
.. code-block:: python

    def findPose(self, img, draw=True):
        """
        Detects human pose landmarks in an image.

        :param img: The input BGR image.
        :param draw: Boolean, controls the overlay of landmark drawings.
        :return: The image with or without landmark drawings.
        """

**findPosition**
.. code-block:: python

    def findPosition(self, img, draw=True, bboxWithHands=False):
        """
        Retrieves landmark positions and bounding box information.

        :param img: The image from which landmarks are detected.
        :param draw: Boolean, controls the drawing of landmarks and bounding box.
        :param bboxWithHands: Boolean, includes hands in the bounding box if True.
        :return: A list of landmark positions and bounding box information.
        """

**findDistance**
.. code-block:: python

    def findDistance(self, p1, p2, img=None, color=(255, 0, 255), scale=5):
        """
        Calculates the distance between two landmarks.

        :param p1, p2: The landmark points (x, y coordinates).
        :param img: Optional, the image on which to draw.
        :param color: The line color (BGR tuple).
        :param scale: The scale of drawn circles.
        :return: The distance, optionally the image with drawn output, and line info.
        """

**findAngle**
.. code-block:: python

    def findAngle(self, p1, p2, p3, img=None, color=(255, 0, 255), scale=5):
        """
        Calculates the angle formed by three landmarks.

        :param p1, p2, p3: The points forming the angle (x, y coordinates).
        :param img: Optional, the image for drawing.
        :param color: The drawing color (BGR tuple).
        :param scale: The scale of drawn elements.
        :return: The calculated angle and optionally the image with the angle drawn.
        """

Example Usage
-------------
To utilize the Pose Module for human pose estimation:

.. code-block:: python

    if __name__ == "__main__":
        cap = cv2.VideoCapture(0)  # Initialize video capture
        detector = PoseDetector()  # Instantiate PoseDetector

        while True:
            success, img = cap.read()  # Capture image frames
            img = detector.findPose(img)  # Detect pose
            lmList, bboxInfo = detector.findPosition(img, draw=True)  # Get positions and bounding box

            if lmList:
                print(lmList)  # Process landmark positions as needed

            cv2.imshow("Pose Estimation", img)  # Display the result
            cv2.waitKey(1)  # Refresh display

This documentation provides a comprehensive guide to the Pose Module, detailing initialization parameters, method functionalities, and an example for practical implementation.
