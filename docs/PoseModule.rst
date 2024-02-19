.. _pose_detector_class:

PoseDetector Class
==================

The PoseDetector class provides human body pose estimation using the mediapipe library.

PoseDetector Class
------------------

.. autoclass:: PoseDetector
    :members:
    :undoc-members:
    :show-inheritance:

    Estimates Pose points of a human body using the mediapipe library.

    :param staticMode: In static mode, detection is done on each image: slower.
    :param modelComplexity: Complexity of the pose model (0, 1, or 2).
    :param smoothLandmarks: Smoothness Flag for landmarks.
    :param enableSegmentation: Flag to enable segmentation.
    :param smoothSegmentation: Flag for smooth segmentation.
    :param detectionCon: Minimum Detection Confidence Threshold.
    :param trackCon: Minimum Tracking Confidence Threshold.

    .. automethod:: __init__
    .. automethod:: findPose
    .. automethod:: findPosition
    .. automethod:: findDistance
    .. automethod:: findAngle
    .. automethod:: angleCheck

Usage Example
-------------

Below is an example of how to use the `PoseDetector` class to estimate human body pose.

.. code-block:: python

    import cv2
    from your_module_name import PoseDetector

    # Initialize the webcam and set it to the third camera (index 2)
    cap = cv2.VideoCapture(2)

    # Initialize the PoseDetector class with the given parameters
    detector = PoseDetector(staticMode=False,
                            modelComplexity=1,
                            smoothLandmarks=True,
                            enableSegmentation=False,
                            smoothSegmentation=True,
                            detectionCon=0.5,
                            trackCon=0.5)

    # Loop to continuously get frames from the webcam
    while True:
        # Capture each frame from the webcam
        success, img = cap.read()

        # Find the human pose in the frame
        img = detector.findPose(img)

        # Find the landmarks, bounding box, and center of the body in the frame
        # Set draw=True to draw the landmarks and bounding box on the image
        lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)

        # Check if any body landmarks are detected
        if lmList:
            # Get the center of the bounding box around the body
            center = bboxInfo["center"]

            # Draw a circle at the center of the bounding box
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

            # Calculate the distance between landmarks 11 and 15 and draw it on the image
            length, img, info = detector.findDistance(lmList[11][0:2],
                                                      lmList[15][0:2],
                                                      img=img,
                                                      color=(255, 0, 0),
                                                      scale=10)

            # Calculate the angle between landmarks 11, 13, and 15 and draw it on the image
            angle, img = detector.findAngle(lmList[11][0:2],
                                            lmList[13][0:2],
                                            lmList[15][0:2],
                                            img=img,
                                            color=(0, 0, 255),
                                            scale=10)

            # Check if the angle is close to 50 degrees with an offset of 10
            isCloseAngle50 = detector.angleCheck(myAngle=angle,
                                                 targetAngle=50,
                                                 offset=10)

            # Print the result of the angle check
            print(isCloseAngle50)

        # Display the frame in a window
        cv2.imshow("Image", img)

        # Wait for 1 millisecond between each frame
        cv2.waitKey(1)

