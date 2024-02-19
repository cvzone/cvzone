.. _face_mesh_module:

Face Mesh Module
================

The Face Mesh Module provides a class, `FaceMeshDetector`, to find 468 landmarks using the mediapipe library, helping acquire the landmark points in pixel format.

FaceMeshDetector Class
----------------------

.. autoclass:: FaceMeshDetector
    :members:
    :undoc-members:
    :show-inheritance:

    Find 468 landmarks using the mediapipe library, helping acquire the landmark points in pixel format.

    :param staticMode: In static mode, detection is done on each image: slower.
    :param maxFaces: Maximum number of faces to detect.
    :param minDetectionCon: Minimum Detection Confidence Threshold.
    :param minTrackCon: Minimum Tracking Confidence Threshold.

    .. automethod:: __init__
    .. automethod:: findFaceMesh
    .. automethod:: findDistance

Usage Example
-------------

Below is an example of how to use the `FaceMeshDetector` class to find landmarks on faces in real-time using the webcam.

.. code-block:: python

    import cv2
    from your_module_name import FaceMeshDetector

    # Initialize the webcam
    # '2' indicates the third camera connected to the computer, '0' would usually refer to the built-in webcam
    cap = cv2.VideoCapture(0)

    # Initialize FaceMeshDetector object
    # staticMode: If True, the detection happens only once, else every frame
    # maxFaces: Maximum number of faces to detect
    # minDetectionCon: Minimum detection confidence threshold
    # minTrackCon: Minimum tracking confidence threshold
    detector = FaceMeshDetector(staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5)

    # Start the loop to continually get frames from the webcam
    while True:
        # Read the current frame from the webcam
        # success: Boolean, whether the frame was successfully grabbed
        # img: The current frame
        success, img = cap.read()

        # Find face mesh in the image
        # img: Updated image with the face mesh if draw=True
        # faces: Detected face information
        img, faces = detector.findFaceMesh(img, draw=True)

        # Check if any faces are detected
        if faces:
            # Loop through each detected face
            for face in faces:
                # Get specific points for the eye
                # leftEyeUpPoint: Point above the left eye
                # leftEyeDownPoint: Point below the left eye
                leftEyeUpPoint = face[159]
                leftEyeDownPoint = face[23]

                # Calculate the vertical distance between the eye points
                # leftEyeVerticalDistance: Distance between points above and below the left eye
                # info: Additional information (like coordinates)
                leftEyeVerticalDistance, info = detector.findDistance(leftEyeUpPoint, leftEyeDownPoint)

                # Print the vertical distance for debugging or information
                print(leftEyeVerticalDistance)

        # Display the image in a window named 'Image'
        cv2.imshow("Image", img)

        # Wait for 1 millisecond to check for any user input, keeping the window open
        cv2.waitKey(1)

