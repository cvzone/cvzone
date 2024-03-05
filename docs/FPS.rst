FPS Module
==========

Overview
--------
The FPS (Frames Per Second) Module in cvzone is a utility designed for calculating and displaying the frames per second in a video stream. It is useful for performance analysis and optimization in computer vision applications.

Dependencies
------------
- cv2 (OpenCV)
- cvzone
- time

Usage
-----
Ensure cvzone and its dependencies are correctly installed.

Class: FPS
----------

Initialization
~~~~~~~~~~~~~~
.. code-block:: python

    def __init__(self, avgCount=30):
        """
        Initializes the FPS class.

        :param avgCount: Integer, optional. The number of frames over which to average the FPS, default is 30.
        """

- **avgCount**: Number of frames to consider for averaging FPS. Higher values result in a smoother FPS calculation but may introduce lag in the FPS display.

Methods
-------

**update**
.. code-block:: python

    def update(self, img=None, pos=(20, 50), bgColor=(255, 0, 255),
               textColor=(255, 255, 255), scale=3, thickness=3):
        """
        Updates the frame rate calculation and optionally displays it on the image.

        :param img: Image to display FPS on. If None, only returns the FPS value.
        :param pos: Tuple, the position to display FPS on the image.
        :param bgColor: Tuple, background color of the FPS text.
        :param textColor: Tuple, text color of the FPS display.
        :param scale: Integer, font scale of the FPS text.
        :param thickness: Integer, thickness of the FPS text.
        :return: Float, the current FPS value, and optionally the image with FPS drawn on it.
        """

- **img**: Image on which to draw the FPS. Optional.
- **pos**: Position on the image to draw the FPS.
- **bgColor**: Background color for the text display.
- **textColor**: Color of the FPS text.
- **scale**: Scale of the font used for displaying FPS.
- **thickness**: Thickness of the text.

Example Usage
-------------
.. code-block:: python

    if __name__ == "__main__":
        fpsReader = cvzone.FPS(avgCount=30)  # Initialize FPS calculator

        cap = cv2.VideoCapture(0)  # Open default camera
        cap.set(cv2.CAP_PROP_FPS, 30)  # Optional: Set camera FPS

        while True:
            success, img = cap.read()  # Read frame

            fps, img = fpsReader.update(img, pos=(20, 50), bgColor=(255, 0, 255),
                                        textColor=(255, 255, 255), scale=3, thickness=3)
            cv2.imshow("Image with FPS", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q'
                break

This example demonstrates how to use the FPS module to calculate and display the frames per second on a video stream captured from the default camera.
