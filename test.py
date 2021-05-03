import cv2 as cv
import tensorflow as tf
import pandas as pd
import pillow as pil
import glob 

images = [cv2.imread(file) for file in glob.glob("/Users/joseph/Downloads/18-2/*.png")]
cv.imshow(images[1])
