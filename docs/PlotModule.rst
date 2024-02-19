.. _live_plot_class:

LivePlot Class
==============

The LivePlot class provides real-time plotting capabilities using OpenCV.

LivePlot Class
--------------

.. autoclass:: LivePlot
    :members:
    :undoc-members:
    :show-inheritance:

    A class for real-time plotting in OpenCV.

    :param w: Width of the plotting window.
    :param h: Height of the plotting window.
    :param yLimit: Y-axis limits [y_min, y_max].
    :param interval: Time interval for updating the plot.
    :param invert: Whether to invert the y-axis.
    :param char: A character to display on the plot for annotation.

    .. automethod:: __init__
    .. automethod:: update
    .. automethod:: drawBackground

Usage Example
-------------

Below is an example of how to use the `LivePlot` class to visualize a sine wave.

.. code-block:: python

    import cv2
    import math
    from your_module_name import LivePlot

    xPlot = LivePlot(w=1200, yLimit=[-100, 100], interval=0.01)
    x = 0

    while True:
        x += 1
        if x == 360:
            x = 0
        imgPlot = xPlot.update(int(math.sin(math.radians(x)) * 100))

        cv2.imshow("Image", imgPlot)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

