Utils Module
============

Overview
--------
The Utils module provides a collection of utility functions designed to facilitate common operations in computer vision projects using OpenCV. These utilities include image stacking, contour finding, image rotation, text rendering with background, and more. 

Dependencies
------------
- cv2 (OpenCV)
- numpy
- copy
- urllib.request

Functions
---------

stackImages
-----------
.. code-block:: python

    def stackImages(_imgList, cols, scale):
        """
        Stacks multiple images in a grid layout.

        :param _imgList: List of images to stack.
        :param cols: Number of columns in the grid.
        :param scale: Scale factor for resizing images.
        :return: Single image with the input images stacked.
        """

cornerRect
----------
.. code-block:: python

    def cornerRect(img, bbox, l=30, t=5, rt=1, colorR=(255, 0, 255), colorC=(0, 255, 0)):
        """
        Draws a rectangle with decorated corners.

        :param img: Input image.
        :param bbox: Bounding box specification [x, y, w, h].
        :param l: Length of the corner lines.
        :param t: Thickness of the corner lines.
        :param rt: Rectangle thickness.
        :param colorR: Rectangle color.
        :param colorC: Corner color.
        :return: Image with the decorated rectangle.
        """

findContours
------------
.. code-block:: python

    def findContours(img, imgPre, minArea=1000, filter=None, drawCon=True):
        """
        Finds and optionally filters contours based on area and corner points.

        :param img: Image to draw contours on.
        :param imgPre: Pre-processed image for contour detection.
        :param minArea: Minimum area of contours to consider.
        :param filter: List of corner counts to filter contours.
        :param drawCon: Whether to draw the contours on the image.
        :return: Image with contours and list of contour information.
        """

overlayPNG
----------
.. code-block:: python

    def overlayPNG(imgBack, imgFront, pos=[0, 0]):
        """
        Overlays a PNG image with transparency over another image.

        :param imgBack: Background image.
        :param imgFront: Foreground PNG image.
        :param pos: Position to place the foreground image.
        :return: Composite image.
        """

rotateImage
-----------
.. code-block:: python

    def rotateImage(imgInput, angle, scale=1, keepSize=False):
        """
        Rotates an image around its center.

        :param imgInput: Image to rotate.
        :param angle: Rotation angle in degrees.
        :param scale: Scale factor for the image.
        :param keepSize: Whether to keep the original image size.
        :return: Rotated image.
        """

putTextRect
-----------
.. code-block:: python

    def putTextRect(img, text, pos, scale=3, colorT=(255, 255, 255), colorR=(255, 0, 255)):
        """
        Renders text with a rectangular background on an image.

        :param img: Image to draw on.
        :param text: Text to render.
        :param pos: Position for the text.
        :param scale: Text scale.
        :param colorT: Text color.
        :param colorR: Background rectangle color.
        :return: Image with text and rectangle.
        """

downloadImageFromUrl
---------------------
.. code-block:: python

    def downloadImageFromUrl(url, keepTransparency=False):
        """
        Downloads an image from a URL.

        :param url: URL of the image.
        :param keepTransparency: Whether to keep the alpha channel.
        :return: Downloaded image.
        """

Example Usage
-------------
The provided `main` function demonstrates the use of several utilities from this module, including stacking images, finding and filtering contours, overlaying PNG images with transparency, and drawing text with rectangular backgrounds. 

These utilities enhance the capabilities of OpenCV projects, streamlining tasks such as image preprocessing, display, and analysis.
