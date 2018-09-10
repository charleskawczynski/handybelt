import argparse
import numpy as np
from getimage.__main__ import getimage
from PIL import Image, ImageOps

def append_to_filename_with_ext(filename, s, rename = False):
  if rename:
    f_new = filename
  else:
    temp = filename.split('.')
    f_new = '.'.join(temp[0:-1])+s+'.'+temp[-1]
  return f_new

def transparentizeBG(**kwargs):
  filename           = kwargs['filename']
  rename             = kwargs['rename']
  image, grayscale = getimage(filename)
  f_new = append_to_filename_with_ext(filename, '_transparentBG', rename)
  image = Image.fromarray(image)
  image = image.convert("RGBA")
  datas = image.getdata()
  newData = []
  for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
      newData.append((255, 255, 255, 0))
    else:
      newData.append(item)
  image.putdata(newData)
  image.save(f_new, "PNG")

def auto_invert_image(image, tol, N_allowable_misses, grayscale):
  if grayscale:
    removeable_rows, removeable_cols = auto_invert_image_bw(image, tol, N_allowable_misses)
  else:
    removeable_rows = []
    removeable_cols = []
    for k in range(0,3):
      r_rows, r_cols = auto_invert_image_bw(image[:,:,k], tol, N_allowable_misses)
      removeable_rows += r_rows
      removeable_cols += r_cols
    removeable_rows = sorted(list(set(removeable_rows)))
    removeable_cols = sorted(list(set(removeable_cols)))
    image = np.delete(image, removeable_rows, axis=0)
    image = np.delete(image, removeable_cols, axis=1)
  return image

def auto_invert_image_bw(image, tol, N_allowable_misses):
  S = image.shape
  removeable_cols = []
  N_misses = 0
  MIN = np.min(image)
  MAX = np.max(image)
  RANGE = MAX-MIN
  tol_normalized = (MAX-MIN)*tol
  for i in range(0, S[1]):
    if np.mean(np.diff(image[:,i])) < tol_normalized:
      removeable_cols.append(i)
    else:
      N_misses+=1
      if N_misses>=N_allowable_misses:
        break
  for i in reversed(range(0, S[1])):
    if np.mean(np.diff(image[:,i])) < tol_normalized:
      removeable_cols.append(i)
    else:
      N_misses+=1
      if N_misses>=N_allowable_misses:
        break

  N_misses = 0
  removeable_rows = []
  for i in range(0, S[0]):
    if np.mean(np.diff(image[i,:])) < tol_normalized:
      removeable_rows.append(i)
    else:
      N_misses+=1
      if N_misses>=N_allowable_misses:
        break
  for i in reversed(range(0, S[0])):
    if np.mean(np.diff(image[i,:])) < tol_normalized:
      removeable_rows.append(i)
    else:
      N_misses+=1
      if N_misses>=N_allowable_misses:
        break
  return removeable_rows, removeable_cols

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Converts image to have transparent background at white pixels.')
  parser.add_argument('filename',
    type=str,
    help='Filename of image to invert')
  parser.add_argument('--rename',
    type=bool,
    default=False,
    help='Rename original file')
  args = parser.parse_args()
  transparentizeBG(**vars(args))
