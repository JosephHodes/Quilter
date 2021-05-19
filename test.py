import cv2 as cv
import pandas as pd
import glob
import numpy as np
from matplotlib import pyplot as plt

images = [cv.imread(file) for file in glob.glob(
    "/Users/joseph/Downloads/18-2/*.png")]


def stitch(images=images):
    img1 = images[0]
    img2 = images[1]
    grey1 = cv.cvtColor(images[0], cv.COLOR_RGB2GRAY)
    grey2 = cv.cvtColor(images[1], cv.COLOR_RGB2GRAY)
    corners = cornerdetection(grey1, img1)
    corners2 = cornerdetection(grey2, img2)

    lw, lh = grey1.shape
    offsetx = int((lw * .90)+lw)
    offsety = (lh * .90)+lh
    newimage = np.zeros((lw*2, lh), np.uint8)
    newimage = cv.merge((newimage, newimage, newimage))
    newimage = cv.cvtColor(newimage, cv.COLOR_RGB2RGBA)
    corners[:, :, 3] = 200
    corners2[:, :, 3] = 200

    newimage[0: lw, 0: lh] = corners[0: lw, 0: lh]
    newimage[offsetx:lw+lw,
             0: lh] = (newimage[offsetx:lw+lw, 0: lh] + corners2[:, :])/2
    cv.imwrite("owo1.png", newimage)


def cornerdetection(gray, img):
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 5, 3, .1)
    print(len(dst))
    dst = cv.dilate(dst, None)

    img[dst > 0.01*dst.max()] = [0, 0, 255]
    img = cv.cvtColor(img, cv.COLOR_RGB2RGBA)
    return img


stitch()

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
