#!/usr/bin/env python
import cv2 as cv
import numpy as np
import sys
from joblib import dump, load

def load_model(fname):
  with open(fname, 'rb') as f:
    return pickle.load(f)
  return None

if len(sys.argv) == 2:
  img_src = cv.imread(sys.argv[1], cv.IMREAD_GRAYSCALE)
  if img_src is None:
    sys.exit('Error: Could not read the image.')
  img_src = cv.resize(img_src, (66, 81))
  cv.imshow('Input Image', img_src)
  mlp = load('mlp.joblib')
  y_predict = mlp.predict(np.array([(img_src / 255).flatten()]))
  output_img = (y_predict * 255).reshape(81, 66)
  output_img[output_img > 255] = 255
  output_img = output_img.astype(np.uint8)
  cv.imshow('Output Image', output_img)
  print('Press enter in a graphics window to exit.')
  cv.waitKey()
else:
  print('Error: Invalid number of arguments.')

