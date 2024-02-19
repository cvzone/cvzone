.. _fps_module:

FPS Module
==========

The FPS Module provides a class, `FPS`, for calculating and displaying the Frames Per Second (FPS) in a video stream.

FPS Class
---------

.. autoclass:: FPS
    :members:
    :undoc-members:
    :show-inheritance:

    Class for calculating and displaying the Frames Per Second (FPS) in a video stream.

    :param avgCount: Number of frames over which to average the FPS, default is 30.
    :ivar pTime: Previous time stamp.
    :ivar frameTimes: List to keep track of frame times.
    :ivar avgCount: Number of frames over which to average the FPS.

    .. automethod:: __init__
    .. automethod:: update

Usage Example
-------------

Below is an example of how to use the `FPS` class to calculate and display the FPS in a video stream.

.. code-block:: python

    import cv2
    from your_module_name import FPS

    # Initialize the FPS class with an average count of 30 frames for smoothing
    fpsReader = FPS(avgCount=30)

    # Initialize the webcam and set it to capture at 60 FPS
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 30)  # Set the frames per second to 30

    # Main loop to capture frames and display FPS
    while True:
        # Read a frame from the webcam
        success, img = cap.read()

        # Update the FPS counter and draw the FPS on the image
        # fpsReader.update returns the current FPS and the updated image
        fps, img = fpsReader.update(img, pos=(20, 50),
                                    bgColor=(255, 0, 255), textColor=(255, 255, 255),
                                    scale=3, thickness=3)

        # Display the image with the FPS counter
        cv2.imshow("Image", img)

        # Wait for 1 ms to show this frame, then continue to the next frame
        cv2.waitKey(1)

