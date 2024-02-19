.. _pid_module:

PID Module
==========

The PID (Proportional-Integral-Derivative) module provides a class, `PID`, for implementing PID control. This module is used for tracking a target value with a given set of PID parameters.

PID Class
---------

.. autoclass:: PID
    :members:
    :undoc-members:
    :show-inheritance:

    The PID class implements the Proportional-Integral-Derivative (PID) control algorithm. It takes target values, current values, and PID parameters as input and provides control outputs based on the error between the target and current values.

    :param pidVals: List containing PID parameters [Kp, Ki, Kd].
    :param targetVal: Target value to be tracked.
    :param axis: The axis along which the PID control is applied (0 for X-axis, 1 for Y-axis).
    :param limit: Limits the output of the PID controller within a specified range [min, max].

    .. automethod:: __init__
    .. automethod:: update
    .. automethod:: draw

Usage Example
-------------

Below is an example of how to use the `PID` class for tracking a target value using face detection coordinates from the `FaceDetector` class.

.. code-block:: python

    import cv2
    from your_module_name import PID
    from cvzone.FaceDetectionModule import FaceDetector

    cap = cv2.VideoCapture(2)
    detector = FaceDetector(minDetectionCon=0.8)
    # For a 640x480 image, the center target is (320, 240)
    xPID = PID([1, 0.000000000001, 1], 640 // 2)
    yPID = PID([1, 0.000000000001, 1], 480 // 2, axis=1, limit=[-100, 100])

    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)
        if bboxs:
            x, y, w, h = bboxs[0]["bbox"]
            cx, cy = bboxs[0]["center"]
            xVal = int(xPID.update(cx))
            yVal = int(yPID.update(cy))

            xPID.draw(img, [cx, cy])
            yPID.draw(img, [cx, cy])

            cv2.putText(img, f'x:{xVal} , y:{yVal} ', (x, y - 100), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

