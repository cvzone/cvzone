"""
Hand Tracking Module
By: Computer Vision Zone
Website: https://www.computervision.zone/
"""

import cv2
import mediapipe as mp
import math
import numpy as np


class HandDetector:
    """
    Finds Hands using the mediapipe library. Exports the landmarks
    in pixel format. Adds extra functionalities like finding how
    many fingers are up or the distance between two fingers. Also
    provides bounding box info of the hand found.
    """
    
    """The 21 hand landmarks.
    """
    WRIST = 0
    THUMB_CMC = 1
    THUMB_MCP = 2
    THUMB_IP = 3
    THUMB_TIP = 4
    INDEX_FINGER_MCP = 5
    INDEX_FINGER_PIP = 6
    INDEX_FINGER_DIP = 7
    INDEX_FINGER_TIP = 8
    MIDDLE_FINGER_MCP = 9
    MIDDLE_FINGER_PIP = 10
    MIDDLE_FINGER_DIP = 11
    MIDDLE_FINGER_TIP = 12
    RING_FINGER_MCP = 13
    RING_FINGER_PIP = 14
    RING_FINGER_DIP = 15
    RING_FINGER_TIP = 16
    PINKY_MCP = 17
    PINKY_PIP = 18
    PINKY_DIP = 19
    PINKY_TIP = 20
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, minTrackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower
        :param maxHands: Maximum number of hands to detect
        :param detectionCon: Minimum Detection Confidence Threshold
        :param minTrackCon: Minimum Tracking Confidence Threshold
        """
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.minTrackCon = minTrackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.minTrackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []

    def findHands(self, img, draw=True, flipType=True):
        """
        Finds hands in a BGR image.
        :param img: Image to find the hands in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        allHands = []
        h, w, c = img.shape
        if self.results.multi_hand_landmarks:
            for handType, handLms in zip(self.results.multi_handedness, self.results.multi_hand_landmarks):
                myHand = {}
                ## lmList
                mylmList = []
                xList = []
                yList = []
                for id, lm in enumerate(handLms.landmark):
                    px, py, pz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                    mylmList.append([px, py, pz])
                    xList.append(px)
                    yList.append(py)

                ## bbox
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                boxW, boxH = xmax - xmin, ymax - ymin
                bbox = xmin, ymin, boxW, boxH
                cx, cy = bbox[0] + (bbox[2] // 2), \
                         bbox[1] + (bbox[3] // 2)

                myHand["lmList"] = mylmList
                myHand["bbox"] = bbox
                myHand["center"] = (cx, cy)

                if flipType:
                    if handType.classification[0].label == "Right":
                        myHand["type"] = "Left"
                    else:
                        myHand["type"] = "Right"
                else:
                    myHand["type"] = handType.classification[0].label
                allHands.append(myHand)

                ## draw
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
                    cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                                  (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20),
                                  (255, 0, 255), 2)
                    cv2.putText(img, myHand["type"], (bbox[0] - 30, bbox[1] - 30), cv2.FONT_HERSHEY_PLAIN,
                                2, (255, 0, 255), 2)
        if draw:
            return allHands, img
        else:
            return allHands

    def fingersUp(self, myHand):
        """
        Finds how many fingers are open and returns in a list.
        Considers left and right hands separately
        :return: List of which fingers are up
        """
        myHandType = myHand["type"]
        myLmList = myHand["lmList"]
        if self.results.multi_hand_landmarks:
            '''
            Start Region MJ:
            These codes writed by Mohammad Javadpur (@mjavadpur)
            '''
            zeroPointX = myLmList[HandDetector.WRIST][0]
            zeroPointY = myLmList[HandDetector.WRIST][1]
            
            ninePointX = myLmList[HandDetector.MIDDLE_FINGER_MCP][0]
            ninePointY = myLmList[HandDetector.MIDDLE_FINGER_MCP][1]
            
            angle = self.angle_from_vertical(zeroPointX, zeroPointY, ninePointX, ninePointY)
            angle2Rotate = 180 - abs(angle)
            
            clockWise = False
            if angle < 0:
                clockWise = True
                
            # print(lmList[1])
            xyList = np.zeros((21,2))
            i = 0 
            for lm in myLmList:
                xyList[i] = lm[0:2]
                i+=1
                
            
            # Define Vertical Line
            p1 = [zeroPointX, zeroPointY] #[0, 0]
            p2 = [ninePointX, ninePointY]#[0, 1]
            
            xyList = self.rotate_points_around_line(xyList, p1, p2, angle2Rotate, clockWise)
            
            i = 0 
            for xy in xyList:
                myLmList[i][0:2] = xy
                i+=1

            self.lmList = myLmList
            palm = self.detectPalmOrBackAftreRotation(myLmList,myHandType)
            
            fingers = []
            # Thumb
            if (myHandType == 'Right' and palm) or (myHandType == 'Left' and not palm):
                if self.lmList[self.tipIds[0]][0] < self.lmList[self.tipIds[0]-1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if self.lmList[self.tipIds[0]][0] > self.lmList[self.tipIds[0]-1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
       
            '''
            End Region MJ
            '''
            # Thumb
            # if myHandType == "Right":
            #     if myLmList[self.tipIds[0]][0] > myLmList[self.tipIds[0] - 1][0]:
            #         fingers.append(1)
            #     else:
            #         fingers.append(0)
            # else:
            #     if myLmList[self.tipIds[0]][0] < myLmList[self.tipIds[0] - 1][0]:
            #         fingers.append(1)
            #     else:
            #         fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if myLmList[self.tipIds[id]][1] < myLmList[self.tipIds[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers

    '''
    This method writed by @mjavadpur
    '''
    def rotate_points_around_line(self, points, p1, p2, angle, clockwise=True):
        '''
        Rotates lmList around a line passing through points p1 and p2 by angle=angle.
        :param points: lmList X, Y values.
        :param p1: The starting point of the line that is the axis of rotation.
        :param p2: The ending point of the line that is the axis of rotation.
        :param angle: Specifies the rotation angle.
        :param clockwise: Specifies the direction of rotation.
        :return: Rotated X , Y values of lmList
        '''
		# Convert the angle to radians
        angle = math.radians(angle)

		# Translate the line to the origin
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        trans_matrix = np.array([[1, 0, -p1[0]],
                                [0, 1, -p1[1]],
                                [0, 0, 1]])

        # Rotate the line to the x-axis
        theta = math.atan2(dy, dx)
        rot_matrix = np.array([[math.cos(theta), -math.sin(theta), 0],
                            [math.sin(theta), math.cos(theta), 0],
                            [0, 0, 1]])

        # Rotate the points around the x-axis
        if clockwise:
            angle = -angle
        rot_matrix_2 = np.array([[math.cos(angle), math.sin(angle), 0],
                                [-math.sin(angle), math.cos(angle), 0],
                                [0, 0, 1]])

        # Rotate the line back to its original position
        rot_matrix_inv = np.linalg.inv(rot_matrix)
        trans_matrix_inv = np.linalg.inv(trans_matrix)
        transformation = np.dot(np.dot(rot_matrix_inv, np.dot(rot_matrix_2, rot_matrix)), trans_matrix_inv)

        # Create an empty array to hold the rotated points
        rotated_points = np.empty_like(points)

        # Loop through each point
        for i in range(points.shape[0]):
            # Apply the transformation matrix to each point
            x, y, _ = np.dot(transformation, np.array([points[i, 0], points[i, 1], 1]))
            
            # Add the rotated point to the output array
            rotated_points[i, 0] = x
            rotated_points[i, 1] = y

        return rotated_points
    
    '''
    This method writed by @mjavadpur
    '''    
    def angle_from_vertical(self, x1, y1, x2, y2):
        """
        Calculates the angle between the vertical axis and the line with the given coordinates (x1,x2) and (x2,y2).
        :param x1: X value of first point.
        :param y1: Y value of first point.
        :param x2: X value of second point.
        :param y2: Y value of second point.
        :return: Angle by degree
        """
        dx = x2 - x1
        dy = y2 - y1
        return math.atan2(dx, dy) * 180 / math.pi

    '''
    This method writed by @mjavadpur
    '''
    def detectPalmOrBackAftreRotation(self, lmList, HandType = 'Right'):
        '''
        This method detects whether it is the palm or the back of the hand
        :param lmList: Land Mark List
        :param HandType: Str, 'Right' or 'Left'
        :return: Returns True for the palm and False for the back of the hand
        '''
        Palm = True
        if HandType == 'Right':
        
            try:
                y9 = lmList[9][1]
                y0 = lmList[0][1]
                x17 = lmList[17][0]
                x5 = lmList[5][0]

                if lmList:
                    if (y9 < y0 and x17 < x5) or (y0 < y9 and x5 < x17):
                        Palm = False
            except Exception as e:
                # Code to handle the exception
                print('An error occurred:', e)
            return Palm
        else: # Left Hand
            try:
                y9 = lmList[9][1]
                y0 = lmList[0][1]
                x17 = lmList[17][0]
                x5 = lmList[5][0]

                if lmList:
                    if (y9 < y0 and x17 > x5) or (y0 < y9 and x5 > x17):
                        Palm = False
            except Exception as e:
                # Code to handle the exception
                print('An error occurred:', e)
            return Palm
        
    def findDistance(self, p1, p2, img=None):
        """
        Find the distance between two landmarks based on their
        index numbers.
        :param p1: Point1
        :param p2: Point2
        :param img: Image to draw on.
        :param draw: Flag to draw the output on the image.
        :return: Distance between the points
                 Image with output drawn
                 Line information
        """

        x1, y1 = p1
        x2, y2 = p2
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)
        info = (x1, y1, x2, y2, cx, cy)
        if img is not None:
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            return length, info, img
        else:
            return length, info


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.8, maxHands=2)
    totalFingers = 0
    while True:
        # Get image frame
        success, img = cap.read()
        if success:
            # Find the hand and its landmarks
            hands, img = detector.findHands(img, flipType=False)  # with draw
            # hands = detector.findHands(img, draw=False)  # without draw

            if hands:
                # Hand 1
                hand1 = hands[0]
                lmList1 = hand1["lmList"]  # List of 21 Landmark points
                bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
                centerPoint1 = hand1['center']  # center of the hand cx,cy
                handType1 = hand1["type"]  # Handtype Left or Right

                fingers1 = detector.fingersUp(hand1)
                totalFingers = fingers1.count(1)
                if len(hands) == 2:
                    # Hand 2
                    hand2 = hands[1]
                    lmList2 = hand2["lmList"]  # List of 21 Landmark points
                    bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
                    centerPoint2 = hand2['center']  # center of the hand cx,cy
                    handType2 = hand2["type"]  # Hand Type "Left" or "Right"

                    fingers2 = detector.fingersUp(hand2)
                    totalFingers += fingers2.count(1)

                    # Find Distance between two Landmarks. Could be same hand or different hands
                    # length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img)  # with draw
                    # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
            # Display
            cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
            cv2.imshow("Image", img)
            cv2.waitKey(1)


if __name__ == "__main__":
    main()
