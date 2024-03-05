PID Module
================================

Overview
--------
This document describes the implementation of a PID (Proportional, Integral, Derivative) controller for face tracking in video streams using the `cvzone` library. The system utilizes a face detection module to find faces in the video feed and a PID controller to adjust the camera's focus or position, aiming to keep the detected face centered in the frame.

Dependencies
------------
- cv2 (OpenCV)
- numpy
- time
- cvzone

Components
----------

Class: PID
----------
The PID class implements a simple PID controller that calculates an output value to minimize the error between a desired setpoint (the target value for the face's position) and a measured process variable (the current position of the face).

Initialization
~~~~~~~~~~~~~~
.. code-block:: python

    def __init__(self, pidVals, targetVal, axis=0, limit=None):
        """
        Initializes the PID controller.

        :param pidVals: Tuple or list of PID coefficients (P, I, D).
        :param targetVal: The target value the PID controller seeks to achieve.
        :param axis: Determines whether the PID controller operates on the X (0) or Y (1) axis.
        :param limit: Optional tuple specifying the minimum and maximum output values.
        """

Methods
~~~~~~~
**update**
.. code-block:: python

    def update(self, cVal):
        """
        Calculates the control variable based on the current error.

        :param cVal: The current value of the process variable.
        :return: The output of the PID controller, adjusted by the PID coefficients.
        """

**draw**
.. code-block:: python

    def draw(self, img, cVal):
        """
        Visualizes the target and current values on the image.

        :param img: The image on which to draw.
        :param cVal: The current value (position) of the process variable.
        :return: The image with the visualization drawn on it.
        """

Main Function
-------------
The `main` function demonstrates the integration of the `FaceDetector` and the PID controller to track a face in real-time video. It adjusts the PID controller's output based on the face's position to keep the detected face centered in the frame.

.. code-block:: python

    def main():
        """
        Main function to run the face tracking system.
        """

Example Usage
-------------
To run the PID controller for face tracking:

1. Ensure all dependencies are installed.
2. Execute the script. The system will open the webcam feed, detect faces, and use the PID controller to track the face, attempting to keep it centered.

This system can be adapted for applications requiring real-time tracking of objects or faces, such as automated camera control for video conferencing, surveillance, or interactive installations.
