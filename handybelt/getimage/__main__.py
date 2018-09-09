import argparse
from PIL import Image
import numpy as np
import scipy

def is_grayscale(file_name):
  image = Image.open(file_name)
  image.load()
  image_data = np.asarray(image)
  S = image_data.shape
  if len(S) == 3:
    return False
  elif len(S) == 2:
    return True
  else:
    ValueError('Uncaught shape in is_grayscale')

def getimage_bw(file_name):
  image = Image.open(file_name)
  image = image.convert('L')
  image = np.asarray(image)
  return image

def getimage_color(file_name):
  image = Image.open(file_name)
  image.load()
  image = np.asarray(image)
  return image

def getimage(file_name):
  grayscale = is_grayscale(file_name)
  if (grayscale):
    image = getimage_bw(file_name)
  else:
    image = getimage_color(file_name)
  return image, grayscale

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Returns a numpy array representation of an image.')
  parser.add_argument('filename',
    type=str,
    help='Filename of image to crop')
  parser.add_argument('--grayscale',
    type=bool,
    default=False,
    help='Return a grayscale image')
  parser.add_argument('--rename',
    type=bool,
    default=False,
    help='Rename original file')
  args = parser.parse_args()
  getimage(**vars(args))
