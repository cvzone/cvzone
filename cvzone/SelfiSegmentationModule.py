import cv2
import mediapipe as mp
import numpy as np

import cvzone


class SelfiSegmentation():

    def __init__(self, model=1):
        """
        :param model: model type 0 or 1. 0 is general 1 is landscape(faster)
        """
        self.model = model
        self.mpDraw = mp.solutions.drawing_utils
        self.mpSelfieSegmentation = mp.solutions.selfie_segmentation
        self.selfieSegmentation = self.mpSelfieSegmentation.SelfieSegmentation(model_selection=self.model)

    def removeBG(self, img, imgBg=(255, 255, 255), cutThreshold=0.1):
        """

        :param img: image to remove background from
        :param imgBg: Background Image. can be a color (255,0,255) or an image . must be same size
        :param cutThreshold: higher = more cut, lower = less cut
        :return:
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.selfieSegmentation.process(imgRGB)
        condition = np.stack(
            (results.segmentation_mask,) * 3, axis=-1) > cutThreshold
        if isinstance(imgBg, tuple):
            _imgBg = np.zeros(img.shape, dtype=np.uint8)
            _imgBg[:] = imgBg
            imgOut = np.where(condition, img, _imgBg)
        else:
            imgOut = np.where(condition, img, imgBg)
        return imgOut


def main():
    # Initialize the webcam. '2' indicates the third camera connected to the computer.
    # '0' usually refers to the built-in camera.
    cap = cv2.VideoCapture(0)

    # Set the frame width to 640 pixels
    cap.set(3, 640)
    # Set the frame height to 480 pixels
    cap.set(4, 480)

    # Initialize the SelfiSegmentation class. It will be used for background removal.
    # model is 0 or 1 - 0 is general 1 is landscape(faster)
    segmentor = SelfiSegmentation(model=0)

    # Infinite loop to keep capturing frames from the webcam
    while True:
        # Capture a single frame
        success, img = cap.read()

        # Use the SelfiSegmentation class to remove the background
        # Replace it with a magenta background (255, 0, 255)
        # imgBG can be a color or an image as well. must be same size as the original if image
        # 'cutThreshold' is the sensitivity of the segmentation.
        imgOut = segmentor.removeBG(img, imgBg=(255, 0, 255), cutThreshold=0.1)

        # Stack the original image and the image with background removed side by side
        imgStacked = cvzone.stackImages([img, imgOut], cols=2, scale=1)

        # Display the stacked images
        cv2.imshow("Image", imgStacked)

        # Check for 'q' key press to break the loop and close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()
