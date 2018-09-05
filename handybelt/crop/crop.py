def append_to_filename_with_ext(filename, s, rename = False):
  if rename:
    f_new = filename
  else:
    temp = filename.split('.')
    f_new = '.'.join(temp[0:-1])+s+'.'+temp[-1]
  return f_new

def main():
  import argparse
  import get_image as GI
  import numpy as np
  from PIL import Image, ImageOps
  parser = argparse.ArgumentParser(description='Crops an image file, rename is optional.')
  parser.add_argument('filename',
    type=str,
    help='Filename of image to crop')
  parser.add_argument('--tol',
    default=0.008,
    type=float,
    help='Tolerance for cropping tol<<1 crops light pixels, tol~1 crops dark pixels.')
  parser.add_argument('--N_allowable_misses',
    type=int,
    default=0,
    help='Allows to crop a specified number past uniform pixels')
  parser.add_argument('--rename',
    type=bool,
    default=False,
    help='Rename original file')
  args = parser.parse_args()
  image, grayscale = GI.get_image(args.filename)
  image = auto_crop_image(image, args.tol, args.N_allowable_misses, grayscale)
  S = image.shape

  f_new = append_to_filename_with_ext(args.filename, '_cropped', args.rename)

  if any([k==0 for k in S]):
    print('shape = {}'.format(S))
    raise ValueError('Cropped image lost all of its rows or columns.')
  image = Image.fromarray(image)
  image.save(f_new)

def auto_crop_image(image, tol, N_allowable_misses, grayscale):
  import numpy as np
  if grayscale:
    removeable_rows, removeable_cols = auto_crop_image_bw(image, tol, N_allowable_misses)
  else:
    removeable_rows = []
    removeable_cols = []
    for k in range(0,3):
      r_rows, r_cols = auto_crop_image_bw(image[:,:,k], tol, N_allowable_misses)
      removeable_rows += r_rows
      removeable_cols += r_cols
    removeable_rows = sorted(list(set(removeable_rows)))
    removeable_cols = sorted(list(set(removeable_cols)))
    image = np.delete(image, removeable_rows, axis=0)
    image = np.delete(image, removeable_cols, axis=1)
  return image

def auto_crop_image_bw(image, tol, N_allowable_misses):
  import numpy as np
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
  main()
