.. _classification_module:

Classification Module
=====================

This module is based on Teachable Machine: https://teachablemachine.withgoogle.com/. It uses a pre-trained Keras model to classify images.

Classifier Class
----------------

.. autoclass:: Classifier
    :members:
    :undoc-members:
    :show-inheritance:

    Classifier class that handles image classification using a pre-trained Keras model.

    :param modelPath: str, path to the Keras model
    :param labelsPath: str, path to the labels file (optional)

    .. automethod:: __init__

    .. automethod:: getPrediction

Usage Example
-------------

Below is an example of how to use the `Classifier` class for image classification.

.. code-block:: python

    import cv2
    from your_module_name import Classifier

    # Initialize video capture
    cap = cv2.VideoCapture(2)
    path = "C:/Users/USER/Documents/maskModel/"

    # Create an instance of the Classifier class
    maskClassifier = Classifier(f'{path}/keras_model.h5', f'{path}/labels.txt')

    while True:
        _, img = cap.read()  # Capture frame-by-frame
        prediction = maskClassifier.getPrediction(img)
        print(prediction)  # Print prediction result
        cv2.imshow("Image", img)
        cv2.waitKey(1)  # Wait for a key press

