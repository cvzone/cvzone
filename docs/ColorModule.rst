Color Module
============

Overview
--------
The Color Module in cvzone is designed for color detection within images based on HSV (Hue, Saturation, Value) values. It supports dynamic adjustment of HSV values through OpenCV trackbars, facilitating the identification of the right color range for various applications.

Features
--------
- Finds colors in images based on HSV values.
- Option to use OpenCV trackbars for dynamic HSV value adjustment.
- Can be used standalone to find relevant HSV values for specific colors.

Dependencies
------------
- cv2 (OpenCV)
- numpy
- cvzone

Usage
-----
First, ensure you have cvzone along with its dependencies installed. 

Class: ColorFinder
------------------

Initialization
~~~~~~~~~~~~~~
.. code-block:: python

    def __init__(self, trackBar=False):
        """
        Initializes the ColorFinder.

        :param trackBar: Boolean, optional. Enables OpenCV trackbars for dynamic HSV adjustment.
        """

- **trackBar**: Boolean. If True, initializes OpenCV trackbars for live HSV value adjustment.

Methods
-------

**update**
.. code-block:: python

    def update(self, img, myColor=None):
        """
        Detects a specified color in an image.

        :param img: Image in which to find the color.
        :param myColor: Dictionary containing HSV values or None. If None and trackBar is True, uses trackbar values.

        :return: Masked image with the specified color, and the mask used for color detection.
        """

- **img**: The image to process.
- **myColor**: Dictionary specifying the HSV range to detect. Optional if trackBar is enabled.

Example Usage
-------------
.. code-block:: python

    if __name__ == "__main__":
        # Initialize the ColorFinder with trackBar enabled
        myColorFinder = cvzone.ColorFinder(trackBar=True)

        # Initialize video capture
        cap = cv2.VideoCapture(0)  # Adjust camera index if necessary

        while True:
            success, img = cap.read()

            # Specify HSV values for color detection or use trackbars
            hsvVals = {'hmin': 0, 'smin': 0, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}

            # Detect color and obtain mask
            imgColor, mask = myColorFinder.update(img, hsvVals)

            # Stack and display the images
            imgStack = cvzone.stackImages([img, imgColor, mask], 3, 0.6)
            cv2.imshow("Stacked Images", imgStack)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

This example demonstrates how to initialize the ``ColorFinder`` class with the trackBar option enabled, allowing for real-time HSV adjustments to find the desired color within a video stream.
