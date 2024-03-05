Classification Module
=====================

Overview
--------
The Classification Module in cvzone facilitates image classification tasks using pre-trained Keras models. It provides an easy-to-use interface for classifying images with high accuracy, leveraging the power of machine learning for computer vision applications.

Dependencies
------------
- OpenCV (cv2)
- NumPy
- TensorFlow

Installation
------------
To use the Classification Module, ensure the following dependencies are installed. TensorFlow can be installed using pip:

.. code-block:: bash

    pip install tensorflow numpy opencv-python

Class: Classifier
-----------------
The ``Classifier`` class is responsible for loading the Keras model and performing image classification.

Constructor
-----------
.. code-block:: python

    def __init__(self, modelPath, labelsPath=None):
        """
        Initializes the Classifier with a model and optional labels file.

        :param modelPath: Path to the Keras model file.
        :param labelsPath: Optional path to the text file containing labels.
        """

- **modelPath**: String. Path to the Keras model file.
- **labelsPath**: String (optional). Path to the text file containing labels, with each label on a separate line.

Methods
-------
**getPrediction**
.. code-block:: python

    def getPrediction(self, img, draw=True, pos=(50, 50), scale=2, color=(0, 255, 0)):
        """
        Classifies an image and optionally draws the classification result.

        :param img: The input image for classification.
        :param draw: Boolean, specifies whether to draw the prediction result on the image.
        :param pos: Tuple specifying the position to draw the prediction text.
        :param scale: Font scale for the prediction text.
        :param color: Color of the prediction text.
        :return: A list of predictions and the index of the most likely prediction.
        """

- **img**: Image to classify.
- **draw**: If True, draws the prediction result on the image.
- **pos**: Position for drawing text (if `draw` is True).
- **scale**: Font scale for drawing text.
- **color**: Text color.

Example Usage
-------------
Below is an example demonstrating how to initialize the ``Classifier``, classify an image, and display the results:

.. code-block:: python

    if __name__ == "__main__":
        cap = cv2.VideoCapture(2)  # Initialize video capture
        path = "C:/path/to/model/"
        classifier = Classifier(f'{path}/keras_model.h5', f'{path}/labels.txt')

        while True:
            success, img = cap.read()  # Capture frame-by-frame
            prediction, index = classifier.getPrediction(img)
            print(f'Prediction: {prediction}, Index: {index}')
            cv2.imshow("Image", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit on 'q' key press
                break
