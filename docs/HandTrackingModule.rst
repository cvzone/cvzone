.. _hand_tracking_module:

Hand Tracking Module
====================

The Hand Tracking Module provides a class, `HandDetector`, using the mediapipe library. It exports the landmarks in pixel format and adds extra functionalities like finding how many fingers are up or the distance between two fingers. It also provides bounding box info for the detected hand.

HandDetector Class
------------------

.. autoclass:: HandDetector
    :members:
    :undoc-members:
    :show-inheritance:

    Finds hands using the mediapipe library. Exports the landmarks in pixel format. Adds extra functionalities like finding how many fingers are up or the distance between two fingers. Also provides bounding box info of the hand found.

    :param staticMode: In static mode, detection is done on each image: slower.
    :param maxHands: Maximum number of hands to detect.
    :param modelComplexity: Complexity of the hand landmark model: 0 or 1.
    :param detectionCon: Minimum Detection Confidence Threshold.
    :param minTrackCon: Minimum Tracking Confidence Threshold.

    .. automethod:: __init__
    .. automethod:: findHands
    .. automethod:: fingersUp
    .. automethod:: findDistance

Usage Example
-------------

Below is an example of how to use the `HandDetector` class to track hands and perform actions such as counting fingers and measuring distances between landmarks.

.. code-block:: python

    import cv2
    from your_module_name import HandDetector

    # Initialize the webcam to capture video
    # The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
    cap = cv2.VideoCapture(0)

    # Initialize the HandDetector class with the given parameters
    detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

    # Continuously get frames from the webcam
    while True:
        # Capture each frame from the webcam
        # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
        success, img = cap.read()

        # Find hands in the current frame
        # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
        # The 'flipType' parameter flips the image, making it easier for some detections
        hands, img = detector.findHands(img, draw=True, flipType=True)

        # Check if any hands are detected
        if hands:
            # Information for the first hand detected
            hand1 = hands[0]  # Get the first hand detected
            lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
            bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
            center1 = hand1['center']  # Center coordinates of the first hand
            handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

            # Count the number of fingers up for the first hand
            fingers1 = detector.fingersUp(hand1)
            print(f'H1 = {fingers1.count(1)}', end=" ")  # Print the count of fingers that are up

            # Calculate distance between specific landmarks on the first hand and draw it on the image
            length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[12][0:2], img, color=(255, 0, 255),
                                                      scale=10)

            # Check if a second hand is detected
            if len(hands) == 2:
                # Information for the second hand
                hand2 = hands[1]
                lmList2 = hand2["lmList"]
                bbox2 = hand2["bbox"]
                center2 = hand2['center']
                handType2 = hand2["type"]

                # Count the number of fingers up for the second hand
                fingers2 = detector.fingersUp(hand2)
                print(f'H2 = {fingers2.count(1)}', end=" ")

                # Calculate distance between the index fingers of both hands and draw it on the image
                length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img, color=(255, 0, 0),
                                                          scale=10)

            print(" ")  # New line for better readability of the printed output

        # Display the image in a window
        cv2.imshow("Image", img)

        # Keep the window open and update it for each frame; wait for 1 millisecond between frames
        cv2.waitKey(1)

