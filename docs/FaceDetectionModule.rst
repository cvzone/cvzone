Face Detection Module
=====================

Overview
--------
The Face Detection Module in cvzone is an efficient real-time solution for detecting faces in images or video streams. It utilizes the lightweight model provided by the MediaPipe library, offering high detection accuracy with minimal computational resources.

Dependencies
------------
- cv2 (OpenCV)
- mediapipe
- cvzone

Usage
-----
Ensure you have installed cvzone along with OpenCV and MediaPipe.

Class: FaceDetector
-------------------

Initialization
~~~~~~~~~~~~~~
.. code-block:: python

    def __init__(self, minDetectionCon=0.5, modelSelection=0):
        """
        Initializes the FaceDetector with configurable confidence and model selection.

        :param minDetectionCon: Minimum confidence for detections ([0.0, 1.0]).
        :param modelSelection: Model selection, where 0 is for short-range and 1 for full-range detection.
        """

- **minDetectionCon**: Float. The threshold for minimum detection confidence.
- **modelSelection**: Integer. Chooses between short-range (0) and full-range (1) model.

Methods
-------

**findFaces**
.. code-block:: python

    def findFaces(self, img, draw=True):
        """
        Detects faces in an image and optionally draws bounding boxes and confidence scores.

        :param img: The input image.
        :param draw: Boolean, specifies whether to draw bounding boxes and scores on the output image.
        :return: The image with drawn detections (optional) and a list of bounding box information.
        """

- **img**: Image in which to detect faces.
- **draw**: If True, draws bounding boxes and confidence scores on the detected faces.

Example Usage
-------------
.. code-block:: python

    if __name__ == "__main__":
        cap = cv2.VideoCapture(0)  # Initialize video capture on the default camera

        detector = cvzone.FaceDetector(minDetectionCon=0.5, modelSelection=0)  # Create FaceDetector

        while True:
            success, img = cap.read()  # Read frame from camera

            img, bboxs = detector.findFaces(img, draw=True)  # Detect faces and draw bounding boxes

            cv2.imshow("Face Detection", img)  # Display the result

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit loop on 'q' key press
                break

This example demonstrates initializing the `FaceDetector` class and using it to detect faces in a video stream, with the option to draw bounding boxes and confidence scores on the detected faces.
