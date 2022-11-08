#!/usr/bin/env python
import cv2 as cv
import os

list_imgs = open('list.txt', 'r')
names = list_imgs.read().splitlines()

# Open image, convert to grayscale, resize and save
def prepare_img(fname):
  # read image, convert to grayscale 
  output_img = cv.imread('dataset/' + fname, cv.IMREAD_GRAYSCALE)
  output_img = cv.resize(output_img, (66, 81))
  otsu_thresh_val, unused = cv.threshold(output_img, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
  input_img = cv.Canny(output_img, int(otsu_thresh_val * 0.5), otsu_thresh_val)
  cv.imwrite('dataset2/output-' + fname, output_img)
  cv.imwrite('dataset2/input-' + fname, 255-input_img)

if not os.path.exists('dataset2'):
  os.mkdir('dataset2')

for name in names:
  print(name)
  prepare_img(name)

