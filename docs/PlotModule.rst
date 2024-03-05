Plot Module
===============

Overview
--------
The `LivePlot` module is designed to provide real-time plotting capabilities within OpenCV displays. It allows for the dynamic plotting of values over time, useful for visualizing data streams in applications such as signal processing, performance monitoring, or any scenario requiring the live graphical representation of data.

Dependencies
------------
- cv2 (OpenCV)
- numpy
- math
- time

Features
--------
- Customizable plot dimensions and y-axis limits.
- Real-time updating with a specified interval.
- Optional y-axis inversion and character annotation.
- Background grid and labels for easy reference.

Class: LivePlot
---------------

Initialization
~~~~~~~~~~~~~~
.. code-block:: python

    def __init__(self, w=640, h=480, yLimit=[0, 100], interval=0.001, invert=True, char='Y'):
        """
        Initializes a LivePlot instance.

        :param w: Width of the plot window.
        :param h: Height of the plot window.
        :param yLimit: List specifying the minimum and maximum values on the y-axis.
        :param interval: Time interval in seconds for updating the plot.
        :param invert: Boolean to determine if the y-axis should be inverted.
        :param char: Character for annotation purposes on the plot.
        """

- **w**: The width of the plotting window in pixels.
- **h**: The height of the plotting window in pixels.
- **yLimit**: The range of values to display along the y-axis.
- **interval**: The update interval for refreshing the plot with new data.
- **invert**: Whether to invert the plot along the y-axis.
- **char**: A single character to annotate the plot, typically representing the plotted variable.

Methods
-------

**update**
.. code-block:: python

    def update(self, y, color=(255, 0, 255)):
        """
        Updates the plot with a new data point.

        :param y: The new y-value to be plotted.
        :param color: The color of the plot line (BGR tuple).
        :return: An image of the updated plot.
        """

- **y**: The new value to add to the plot.
- **color**: The color used for the plot line.

**drawBackground**
.. code-block:: python

    def drawBackground(self):
        """
        Draws static elements of the plot, such as the background, grid lines, and axis labels.
        """

Example Usage
-------------
The following example demonstrates how to use the `LivePlot` class to plot a sine wave in real-time:

.. code-block:: python

    if __name__ == "__main__":
        xPlot = LivePlot(w=1200, yLimit=[-100, 100], interval=0.01)
        x = 0
        while True:
            x += 1
            if x == 360: x = 0
            imgPlot = xPlot.update(int(math.sin(math.radians(x)) * 100))
            cv2.imshow("Image", imgPlot)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

This script creates a `LivePlot` instance with a width of 1200 pixels and y-axis limits from -100 to 100. It then enters an infinite loop, updating the plot with the sine of an incrementing angle and displaying it in real-time. The loop exits upon pressing 'q'.
