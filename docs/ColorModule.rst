.. _color_module:

Color Module
============

The Color Module finds color in an image based on HSV values and can run as a stand-alone script to find relevant HSV values.

ColorFinder Class
-----------------

.. autoclass:: ColorFinder
    :members:
    :undoc-members:
    :show-inheritance:

    Class that handles finding a specified color in an image using HSV values.

    :param trackBar: Whether to use OpenCV trackbars to dynamically adjust HSV values. Default is False.

    .. automethod:: __init__
    .. automethod:: empty
    .. automethod:: initTrackbars
    .. automethod:: getTrackbarValues
    .. automethod:: update

Usage Example
-------------

Below is an example of how to use the `ColorFinder` class to find a specified color in an image.

.. code-block:: python

    import cv2
    from your_module_name import ColorFinder

    # Create an instance of the ColorFinder class with trackBar set to True.
    myColorFinder = ColorFinder(trackBar=True)

    # Initialize the video capture using OpenCV.
    # Using the third camera (index 2). Adjust index if you have multiple cameras.
    cap = cv2.VideoCapture(2)

    # Set the dimensions of the camera feed to 640x480.
    cap.set(3, 640)
    cap.set(4, 480)

    # Custom color values for detecting orange.
    # 'hmin', 'smin', 'vmin' are the minimum values for Hue, Saturation, and Value.
    # 'hmax', 'smax', 'vmax' are the maximum values for Hue, Saturation, and Value.
    hsvVals = {'hmin': 10, 'smin': 55, 'vmin': 215, 'hmax': 42, 'smax': 255, 'vmax': 255}

    # Main loop to continuously get frames from the camera.
    while True:
        # Read the current frame from the camera.
        success, img = cap.read()

        # Use the update method from the ColorFinder class to detect the color.
        # It returns the masked color image and a binary mask.
        imgOrange, mask = myColorFinder.update(img, hsvVals)

        # Stack the original image, the masked color image, and the binary mask.
        imgStack = cvzone.stackImages([img, imgOrange, mask], 3, 1)

        # Show the stacked images.
        cv2.imshow("Image Stack", imgStack)

        # Break the loop if the 'q' key is pressed.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

