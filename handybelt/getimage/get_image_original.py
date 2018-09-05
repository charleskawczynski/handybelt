def main():
  import argparse
  parser = argparse.ArgumentParser(description='Returns a numpy array representation of an image.')
  parser.add_argument('filename',
    type=str,
    help='Filename of image to crop')
  parser.add_argument('--grayscale',
    type=bool,
    default=False,
    help='Return a grayscale image')
  args = parser.parse_args()
  if args.grayscale:
    image = get_image_bw(args.filename)
  else:
    image = get_image(args.filename)
  return image

def is_grayscale(file_name):
  from PIL import Image
  import numpy as np
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

def get_image_bw(file_name):
  from PIL import Image
  import scipy
  import numpy as np
  image = Image.open(file_name)
  image = image.convert('L')
  image = np.asarray(image)
  return image

def get_image_color(file_name):
  from PIL import Image
  import numpy as np
  import scipy
  image = Image.open(file_name)
  image.load()
  image = np.asarray(image)
  return image

def get_image(file_name):
  grayscale = is_grayscale(file_name)
  if ():
    image = get_image_bw(file_name)
  else:
    image = get_image_color(file_name)
  return image, grayscale

if __name__ == '__main__':
  main()
