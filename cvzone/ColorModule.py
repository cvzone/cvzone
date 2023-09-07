"""
Color Module
Finds color in an image based on hsv values
Can run as stand alone to find relevant hsv values

"""

import cv2
import numpy as np

import cvzone


class ColorFinder:
    def __init__(self, trackBar=False):
        """
        :param trackBar: Whether to use OpenCV trackbars to dynamically adjust HSV values. Default is False.
        """
        self.trackBar = trackBar
        if self.trackBar:
            self.initTrackbars()

    def empty(self, a):
        """An empty function to pass as a parameter when creating trackbars."""
        pass

    def initTrackbars(self):
        """Initialize the OpenCV trackbars for dynamic HSV value adjustment."""
        cv2.namedWindow("TrackBars")
        cv2.resizeWindow("TrackBars", 640, 240)
        cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, self.empty)
        cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, self.empty)
        cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, self.empty)
        cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, self.empty)
        cv2.createTrackbar("Val Min", "TrackBars", 0, 255, self.empty)
        cv2.createTrackbar("Val Max", "TrackBars", 255, 255, self.empty)

    def getTrackbarValues(self):
        """
         Get the current HSV values set by the trackbars.

         :return: A dictionary containing the current HSV values from the trackbars.
         """
        hmin = cv2.getTrackbarPos("Hue Min", "TrackBars")
        smin = cv2.getTrackbarPos("Sat Min", "TrackBars")
        vmin = cv2.getTrackbarPos("Val Min", "TrackBars")
        hmax = cv2.getTrackbarPos("Hue Max", "TrackBars")
        smax = cv2.getTrackbarPos("Sat Max", "TrackBars")
        vmax = cv2.getTrackbarPos("Val Max", "TrackBars")

        hsvVals = {"hmin": hmin, "smin": smin, "vmin": vmin,
                   "hmax": hmax, "smax": smax, "vmax": vmax}
        print(hsvVals)
        return hsvVals

    def update(self, img, myColor=None):
        """
        Find a specified color in the given image.

        :param img: The image in which to find the color.
        :param myColor: The color to find, can be a string or None.

        :return: A tuple containing a mask image with only the specified color, and the original image masked to only show the specified color.
        """
        imgColor = []
        mask = []

        if self.trackBar:
            myColor = self.getTrackbarValues()

        if isinstance(myColor, str):
            myColor = self.getColorHSV(myColor)

        if myColor is not None:
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            lower = np.array([myColor['hmin'], myColor['smin'], myColor['vmin']])
            upper = np.array([myColor['hmax'], myColor['smax'], myColor['vmax']])
            mask = cv2.inRange(imgHSV, lower, upper)
            imgColor = cv2.bitwise_and(img, img, mask=mask)

        return imgColor, mask


if __name__ == "__main__":
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
