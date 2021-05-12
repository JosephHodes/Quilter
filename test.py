import cv2 as cv
import pandas as pd
import glob
import numpy as np
from matplotlib import pyplot as plt

images = [cv.imread(file) for file in glob.glob(
    "/Users/joseph/Downloads/18-2/*.png")]


def stitch(images=images):
    grey1 = cv.cvtColor(images[0], cv.COLOR_RGB2GRAY)
    grey2 = cv.cvtColor(images[1], cv.COLOR_RGB2GRAY)
    corners = cornerdetection(grey1)
    corners2 = cornerdetection(grey2)
    size = grey1.shape()
    print(size[1])


def cornerdetection(grey1):
    corners = cv.goodFeaturesToTrack(grey1, 25, 0.01, 10)
    corners = np.int0(corners)
    for i in corners:
        x, y = i.ravel()
        cv.circle(grey1, (x, y), 3, 255, -1)
        return (x, y)


stitch()
