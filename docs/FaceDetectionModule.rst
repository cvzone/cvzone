.. _face_detection_module:

Face Detection Module
=====================

The Face Detection Module provides a class, `FaceDetector`, to find faces in real-time using the lightweight model provided in the mediapipe library.

FaceDetector Class
------------------

.. autoclass:: FaceDetector
    :members:
    :undoc-members:
    :show-inheritance:

    Find faces in real-time using the lightweight model provided in the mediapipe library.

    :param minDetectionCon: Minimum confidence value ([0.0, 1.0]) for face detection to be considered successful. See details in https://solutions.mediapipe.dev/face_detection#min_detection_confidence.
    :param modelSelection: 0 or 1. 0 to select a short-range model that works best for faces within 2 meters from the camera, and 1 for a full-range model best for faces within 5 meters. See details in https://solutions.mediapipe.dev/face_detection#model_selection.

    .. automethod:: __init__
    .. automethod:: findFaces

Usage Example
-------------

Below is an example of how to use the `FaceDetector` class to find faces in real-time using the webcam.

.. code-block:: python

    import cv2
    from your_module_name import FaceDetector

    # Initialize the webcam
    # '2' means the third camera connected to the computer, usually 0 refers to the built-in webcam
    cap = cv2.VideoCapture(2)

    # Initialize the FaceDetector object
    # minDetectionCon: Minimum detection confidence threshold
    # modelSelection: 0 for short-range detection (2 meters), 1 for long-range detection (5 meters)
    detector = FaceDetector(minDetectionCon=0.5, modelSelection=0)

    # Run the loop to continually get frames from the webcam
    while True:
        # Read the current frame from the webcam
        # success: Boolean, whether the frame was successfully grabbed
        # img: the captured frame
        success, img = cap.read()

        # Detect faces in the image
        # img: Updated image
        # bboxs: List of bounding boxes around detected faces
        img, bboxs = detector.findFaces(img, draw=False)

        # Check if any face is detected
        if bboxs:
            # Loop through each bounding box
            for bbox in bboxs:
                # bbox contains 'id', 'bbox', 'score', 'center'

                # ---- Get Data  ---- #
                center = bbox["center"]
                x, y, w, h = bbox['bbox']
                score = int(bbox['score'][0] * 100)

                # ---- Draw Data  ---- #
                cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
                cvzone.putTextRect(img, f'{score}%', (x, y - 10))
                cvzone.cornerRect(img, (x, y, w, h))

        # Display the image in a window named 'Image'
        cv2.imshow("Image", img)
        # Wait for 1 millisecond, and keep the window open
        cv2.waitKey(1)

