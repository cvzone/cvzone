Face Mesh Module
================

Overview
--------
The Face Mesh Module in cvzone leverages the MediaPipe library to detect 468 facial landmarks in real-time. This module is designed to provide detailed landmark detection, facilitating applications that require high precision in facial feature tracking.

Dependencies
------------
- cv2 (OpenCV)
- mediapipe
- math (for calculations)
- cvzone

Usage
-----
Before using this module, ensure that cvzone, OpenCV, and MediaPipe are installed in your environment.

Class: FaceMeshDetector
-----------------------

Initialization
~~~~~~~~~~~~~~
.. code-block:: python

    def __init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):
        """
        Initializes the FaceMeshDetector with customizable parameters.

        :param staticMode: Bool, whether detection is performed on every image.
        :param maxFaces: Integer, the maximum number of faces to detect.
        :param minDetectionCon: Float, the minimum detection confidence.
        :param minTrackCon: Float, the minimum tracking confidence.
        """

- **staticMode**: Operates in static mode if True, otherwise processes each frame for detection.
- **maxFaces**: Sets the maximum number of faces the detector should identify.
- **minDetectionCon**: The threshold for considering a detection successful.
- **minTrackCon**: The threshold for considering the tracking of a face successful.

Methods
-------

**findFaceMesh**
.. code-block:: python

    def findFaceMesh(self, img, draw=True):
        """
        Detects facial landmarks in an image.

        :param img: The image to detect facial landmarks in.
        :param draw: Boolean, specifies whether to draw the landmarks on the image.
        :return: The image with drawn landmarks (if specified) and a list of detected faces with landmarks.
        """

- **img**: The input image for landmark detection.
- **draw**: If True, overlays the detected landmarks on the input image.

**findDistance**
.. code-block:: python

    def findDistance(self, p1, p2, img=None):
        """
        Calculates the distance between two landmark points.

        :param p1: The first point (x, y coordinates).
        :param p2: The second point (x, y coordinates).
        :param img: Optional image on which to draw the points and line.
        :return: The distance between the two points, additional info, and optionally the image with the line drawn.
        """

- **p1**, **p2**: The landmark points between which the distance is measured.
- **img**: The image on which to illustrate the measurement.

Example Usage
-------------
.. code-block:: python

    if __name__ == "__main__":
        cap = cv2.VideoCapture(0)  # Initialize video capture
        detector = FaceMeshDetector(maxFaces=2)  # Create FaceMeshDetector object

        while True:
            success, img = cap.read()  # Read a frame
            img, faces = detector.findFaceMesh(img)  # Detect face mesh

            # Optional: Handle face data
            if faces:
                for face in faces:
                    # Example: Access the landmark point for left eye
                    leftEye = face[130]
                    # Further processing...

            cv2.imshow("Face Mesh", img)  # Display the frame
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
                break

This example demonstrates how to use the `FaceMeshDetector` to identify facial landmarks in a video stream and display the results in real-time. The landmarks can be accessed for each detected face, enabling detailed analysis and applications.
