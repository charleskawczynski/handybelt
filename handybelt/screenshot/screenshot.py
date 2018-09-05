import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import scipy.misc
import imageio

def screenshot():
  parser = argparse.ArgumentParser(description='Take a screen-shot and save a sub-window to file.')
  parser.add_argument('--L',
    default='C',
    type=str,
    help='Position of cropped screen-shot: [L, R, LU, LD, RU, RD]')
  parser.add_argument('--filename',
    default='screenshot.png',
    type=str,
    help='Size of cropped screen-shot, measured by percentage of screen from center')
  parser.add_argument('--preview',
    type=bool,
    default=False,
    help='Defines whether preview should be displayed or not')
  parser.add_argument('--res',
    type=float,
    default=1,
    help='Normalized resolution')
  args = parser.parse_args()

  data = pyautogui.screenshot()
  data = np.asarray(data)
  S = data.shape
  NX, NY = S[1], S[0]

  x_start, x_stop = 0, NX
  y_start, y_stop = 0, NY
  if 'L' in args.L and 'R' in args.L:
    raise ValueError('Cannot screen left and right side of screen simultaneously. Pass no args to get whole screen.')
  if 'U' in args.L and 'D' in args.L:
    raise ValueError('Cannot screen top and bottom side of screen simultaneously. Pass no args to get whole screen.')

  if 'L' in args.L: x_stop = int(.5*NX)
  elif 'R' in args.L: x_start = int(.5*NX)

  if 'U' in args.L: y_stop = int(.5*NY)
  elif 'D' in args.L: y_start = int(.5*NY)

  data = data[y_start:y_stop, x_start:x_stop,:]
  NY_new = int(args.res*(y_stop-y_start+1))
  NX_new = int(args.res*(x_stop-x_start+1))
  image = scipy.misc.imresize(data, (NY_new, NX_new))
  imageio.imwrite(args.filename, image)

  if args.preview:
    plt.figure(figsize=(30, 15))
    plt.imshow(image)
    plt.gray()
    plt.title('Screenshot')
    plt.show()

# if __name__ == '__main__':
#   screenshot()
