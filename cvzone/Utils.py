"""
Supporting Functions for Computer vision using OpenCV
By: Computer Vision Zone
Website: https://www.computervision.zone/
"""

import cv2
import numpy as np
import copy


def stackImages(_imgList, cols, scale):
    """
    Stack Images together to display in a single window
    :param _imgList: list of images to stack
    :param cols: the num of img in a row
    :param scale: bigger~1+ ans smaller~1-
    :return: Stacked Image
    """
    imgList = copy.deepcopy(_imgList)

    # make the array full by adding blank img, otherwise the openCV can't work
    totalImages = len(imgList)
    rows = totalImages // cols if totalImages // cols * cols == totalImages else totalImages // cols + 1
    blankImages = cols * rows - totalImages

    width = imgList[0].shape[1]
    height = imgList[0].shape[0]
    imgBlank = np.zeros((height, width, 3), np.uint8)
    imgList.extend([imgBlank] * blankImages)

    # resize the images
    for i in range(cols * rows):
        imgList[i] = cv2.resize(imgList[i], (0, 0), None, scale, scale)
        if len(imgList[i].shape) == 2:
            imgList[i] = cv2.cvtColor(imgList[i], cv2.COLOR_GRAY2BGR)

    # put the images in a board
    hor = [imgBlank] * rows
    for y in range(rows):
        line = []
        for x in range(cols):
            line.append(imgList[y * cols + x])
        hor[y] = np.hstack(line)
    ver = np.vstack(hor)
    return ver


def cornerRect(img, bbox, l=30, t=5, rt=1,
               colorR=(255, 0, 255), colorC=(0, 255, 0)):
    """
    :param img: Image to draw on.
    :param bbox: Bounding box [x, y, w, h]
    :param l: length of the corner line
    :param t: thickness of the corner line
    :param rt: thickness of the rectangle
    :param colorR: Color of the Rectangle
    :param colorC: Color of the Corners
    :return:
    """
    x, y, w, h = bbox
    x1, y1 = x + w, y + h
    if rt != 0:
        cv2.rectangle(img, bbox, colorR, rt)
    # Top Left  x,y
    cv2.line(img, (x, y), (x + l, y), colorC, t)
    cv2.line(img, (x, y), (x, y + l), colorC, t)
    # Top Right  x1,y
    cv2.line(img, (x1, y), (x1 - l, y), colorC, t)
    cv2.line(img, (x1, y), (x1, y + l), colorC, t)
    # Bottom Left  x,y1
    cv2.line(img, (x, y1), (x + l, y1), colorC, t)
    cv2.line(img, (x, y1), (x, y1 - l), colorC, t)
    # Bottom Right  x1,y1
    cv2.line(img, (x1, y1), (x1 - l, y1), colorC, t)
    cv2.line(img, (x1, y1), (x1, y1 - l), colorC, t)

    return img


def findContours(img, imgPre, minArea=1000, sort=True, filter=0, drawCon=True, c=(255, 0, 0)):
    """
    Finds Contours in an image
    :param img: Image on which we want to draw
    :param imgPre: Image on which we want to find contours
    :param minArea: Minimum Area to detect as valid contour
    :param sort: True will sort the contours by area (biggest first)
    :param filter: Filters based on the corner points e.g. 4 = Rectangle or square
    :param drawCon: draw contours boolean
    :return: Foudn contours with [contours, Area, BoundingBox, Center]
    """
    conFound = []
    imgContours = img.copy()
    contours, hierarchy = cv2.findContours(imgPre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > minArea:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            # print(len(approx))
            if len(approx) == filter or filter == 0:
                if drawCon: cv2.drawContours(imgContours, cnt, -1, c, 3)
                x, y, w, h = cv2.boundingRect(approx)
                cx, cy = x + (w // 2), y + (h // 2)
                cv2.rectangle(imgContours, (x, y), (x + w, y + h), c, 2)
                cv2.circle(imgContours, (x + (w // 2), y + (h // 2)), 5, c, cv2.FILLED)
                conFound.append({"cnt": cnt, "area": area, "bbox": [x, y, w, h], "center": [cx, cy]})

    if sort:
        conFound = sorted(conFound, key=lambda x: x["area"], reverse=True)

    return imgContours, conFound


def overlayPNG(imgBack, imgFront, pos=[0, 0]):
    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape
    *_, mask = cv2.split(imgFront)
    maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
    maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    imgRGBA = cv2.bitwise_and(imgFront, maskBGRA)
    imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)

    imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
    imgMaskFull[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = imgRGB
    imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
    maskBGRInv = cv2.bitwise_not(maskBGR)
    imgMaskFull2[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = maskBGRInv

    imgBack = cv2.bitwise_and(imgBack, imgMaskFull2)
    imgBack = cv2.bitwise_or(imgBack, imgMaskFull)

    return imgBack


def rotateImage(img, angle, scale=1):
    h, w = img.shape[:2]
    center = (w / 2, h / 2)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=scale)
    img = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(w, h))

    return img


def textWithBackground(img, text, font, fontScale, textPos, textThickness=1,textColor=(0,255,0), bgColor=(0,0,0), pad_x=3, pad_y=3, bgOpacity=0.5):
    """
    Draws text with background, with  control transparency
    @param img:(mat) which you want to draw text
    @param text: (string) text you want draw
    @param font: fonts face, like FONT_HERSHEY_COMPLEX, FONT_HERSHEY_PLAIN etc.
    @param fontScale: (double) the size of text, how big it should be.
    @param textPos: tuple(x,y) position where you want to draw text
    @param textThickness:(int) fonts weight, how bold it should be
    @param textPos: tuple(x,y) position where you want to draw text
    @param textThickness:(int) fonts weight, how bold it should be.
    @param textColor: tuple(BGR), values -->0 to 255 each
    @param bgColor: tuple(BGR), values -->0 to 255 each
    @param pad_x: int(pixels)  padding of in x direction
    @param pad_y: int(pixels) 1 to 1.0 (), controls transparency of  text background 
    @return: img(mat) with draw with background
    """
    (t_w, t_h), _= cv2.getTextSize(text, font, fontScale, textThickness) # getting the text size
    x, y = textPos
    overlay = img.copy() # coping the image
    cv2.rectangle(overlay, (x-pad_x, y+ pad_y), (x+t_w+pad_x, y-t_h-pad_y), bgColor,-1) # draw rectangle 
    new_img = cv2.addWeighted(overlay, bgOpacity, img, 1 - bgOpacity, 0) # overlaying the rectangle on the image.
    cv2.putText(new_img,text, textPos,font, fontScale, textColor,textThickness ) # draw in text
    img = new_img

    return img


def textBlurBackground(img, text, font, fontScale, textPos, textThickness=1,textColor=(0,255,0),kneral=(33,33) , pad_x=3, pad_y=3):
    """
    
    Draw text with background blured,  control the blur value, with kernal(odd, odd)
    @param img:(mat) which you want to draw text
    @param text: (string) text you want draw
    @param font: fonts face, like FONT_HERSHEY_COMPLEX, FONT_HERSHEY_PLAIN etc.
    @param fontScale: (double) the size of text, how big it should be.
    @param textPos: tuple(x,y) position where you want to draw text
    @param textThickness:(int) fonts weight, how bold it should be.
    @param textColor: tuple(BGR), values -->0 to 255 each
    @param kneral: tuple(3,3) int as odd number:  higher the value, more blurry background would be
    @param pad_x: int(pixels)  padding of in x direction
    @param pad_y: int(pixels)  padding of in y direction
    @return: img mat, with text drawn, with background blured
    
    call the function: 
     img =textBlurBackground(img, 'Blured Background Text', cv2.FONT_HERSHEY_COMPLEX, 0.9, (20, 60),2, (0,255, 0), (49,49), 13, 13 )
    """
    
    (t_w, t_h), _= cv2.getTextSize(text, font, fontScale, textThickness) # getting the text size
    x, y = textPos
    blur_roi = img[y-pad_y-t_h: y+pad_y, x-pad_x:x+t_w+pad_x] # croping Text Background
    img[y-pad_y-t_h: y+pad_y, x-pad_x:x+t_w+pad_x]=cv2.blur(blur_roi, kneral)  # merging the blured background to img
    cv2.putText(img,text, textPos,font, fontScale, textColor,textThickness )          
    # cv2.imshow('blur roi', blur_roi)
    # cv2.imshow('blured', img)
    return img

def main():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        textBlurBackground(img, 'Blured Background Text', cv2.FONT_HERSHEY_COMPLEX, 0.9, (20, 60),2, (0,255, 0), (49,49), 13, 13 )
        img=textWithBackground(img, 'Colored Background Texts', cv2.FONT_HERSHEY_COMPLEX, 0.6, (20,100), textThickness=2, textColor=(0,0, 0),bgColor=(0,255,0), bgOpacity=0.6, pad_x=10, pad_y=10)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgList = [img, img, imgGray, img, imgGray]
        imgStacked = stackImages(imgList, 2, 0.5)

        cv2.imshow("stackedImg", imgStacked)
        if cv2.waitKey(1) ==ord('q'):
            break


if __name__ == "__main__":
    main()
