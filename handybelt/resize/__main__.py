from getimage.__main__ import getimage
import scipy.misc
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import imageio

def append_to_filename_with_ext(filename, s, rename = False):
  if rename:
    f_new = filename
  else:
    temp = filename.split('.')
    f_new = '.'.join(temp[0:-1])+s+'.'+temp[-1]
  return f_new

def restricted_float(x):
  x = float(x)
  x_min, x_max = 0.0, 1.0
  if x < x_max or x > x_min:
    raise argparse.ArgumentTypeError("{} not in range [{}, {}]".format(x, x_min, x_max))
  return x

def resize(**kwargs):
  filename = kwargs['filename']
  res = kwargs['res']
  rename = kwargs['rename']

  image, grayscale = getimage(filename)

  S = image.shape
  NX, NY = S[1], S[0]
  NY_new = int(res*NY)
  NX_new = int(res*NX)
  image = scipy.misc.imresize(image, (NY_new, NX_new))
  f_new = append_to_filename_with_ext(filename, '_resized', rename)
  imageio.imwrite(f_new, image)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Resize image file.')
  parser.add_argument('filename',
    type=str,
    help='Image to resize')
  parser.add_argument('res',
    type=float,
    default=1.0,
    help='Normalized resolution')
  parser.add_argument('--rename',
    type=bool,
    default=False,
    help='Defines whether file is renamed or not')
  args = parser.parse_args()
  resize(**vars(args))
