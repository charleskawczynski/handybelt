import argparse
import os
import subprocess

def main(**kwargs):
  filename = kwargs['filename']
  dpi      = kwargs['dpi']
  filename = filename.replace('/',os.sep) if '\\'==os.sep else filename.replace('\\',os.sep)
  path = os.path.dirname(filename)
  path = '.' if path=='' else path
  p, ext = os.path.splitext(filename)
  subprocess.run('python -m buildlatex '+filename)
  subprocess.run('python -m pdf2img '+filename.replace(ext,'.pdf'))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Make an image from a pdf file.')
  parser.add_argument('filename',
    type=str,
    help='Filename of image to convert')
  parser.add_argument('--dpi',
    type=int,
    default=300,
    help='dpi for generated image')
  args = parser.parse_args()
  main(**vars(args))
