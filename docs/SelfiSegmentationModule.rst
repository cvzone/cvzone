Selfie Segmentation Module
==========================

Overview
--------
The Selfie Segmentation Module leverages the MediaPipe library for efficient and real-time background segmentation and removal in images. Primarily designed for selfies, it is versatile enough to be used in various applications requiring background manipulation.

Dependencies
------------
- cv2 (OpenCV)
- mediapipe
- numpy
- cvzone

Features
--------
- Real-time background segmentation for images.
- Supports two model types for general and landscape-oriented segmentation.
- Allows customization of the background replacement, including solid colors and images.
- Adjustable threshold for segmentation sensitivity.

Class: SelfiSegmentation
------------------------

Initialization
~~~~~~~~~~~~~~
.. code-block:: python

    def __init__(self, model=1):
        """
        Initializes the SelfiSegmentation object with a specified model.

        :param model: Integer, selects the model type (0 for general, 1 for landscape) with differing performance characteristics.
        """

- **model**: Determines the segmentation model used. Model 0 is more general-purpose, while Model 1 is optimized for landscapes and potentially faster.

Methods
-------

**removeBG**
.. code-block:: python

    def removeBG(self, img, imgBg=(255, 255, 255), cutThreshold=0.1):
        """
        Removes the background from an image, replacing it with a specified background.

        :param img: The input image from which to remove the background.
        :param imgBg: The background replacement, which can be a solid color (default: white) or another image.
        :param cutThreshold: Float, determines the threshold for segmentation sensitivity; higher values increase the background cut.
        :return: The image with the background removed or replaced.
        """

- **img**: The source image for background removal.
- **imgBg**: The new background, either a solid color given by an RGB tuple or another image of the same dimensions as **img**.
- **cutThreshold**: Adjusts the sensitivity of the segmentation process.

Example Usage
-------------
The following example demonstrates using the `SelfiSegmentation` class for background removal in a live webcam feed:

.. code-block:: python

    if __name__ == "__main__":
        cap = cv2.VideoCapture(0)  # Initialize video capture
        segmentor = SelfiSegmentation(model=0)  # Instantiate SelfiSegmentation

        while True:
            success, img = cap.read()  # Read image frame
            imgOut = segmentor.removeBG(img, imgBg=(255, 0, 255), cutThreshold=0.1)  # Remove background

            # Display the original and segmented images side by side
            imgStacked = cvzone.stackImages([img, imgOut], cols=2, scale=1)
            cv2.imshow("Image Segmentation", imgStacked)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
                break

This documentation provides a comprehensive guide to the Selfie Segmentation Module, detailing initialization parameters, functionalities, and a practical example for real-time background removal and segmentation in video streams.
