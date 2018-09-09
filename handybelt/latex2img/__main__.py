from pdf2image import convert_from_path
import argparse
import os
import imageio
import numpy as np
import subprocess
from cleartempfiles.__main__ import cleartempfiles
from crop.__main__ import crop

def main(**kwargs):
  filename = kwargs['filename']
  dpi      = kwargs['dpi']
  filename = filename.replace('/',os.sep) if '\\'==os.sep else filename.replace('\\',os.sep)
  path = os.path.dirname(filename)
  path = '.' if path=='' else path
  p, ext = os.path.splitext(filename)
  data = convert_from_path(filename, dpi)
  data = np.asarray(data[0])
  image_file = p+'.png'
  imageio.imwrite(image_file, data)
  subprocess.run('python -m crop --tol 1e-6 --N_allowable_misses 0 --rename True '+image_file)

  # build_latex_file(file_name)
  # build_eps_from_latex(f)
  # build_eps_from_pdf(p)
  # eps_to_png(f)
  # crop(args.filename)

  cleartempfiles(path)

def build_eps_from_latex(file_name):
  subprocess.run('latex --jobname='+file_name+' '+file_name+'.tex')
  subprocess.run('dvips '+file_name+'.dvi')

def build_eps_from_pdf(file_name):
  subprocess.run('dvips '+file_name+'.dvi')

def eps_to_png(file_name):
  subprocess.run('gswin64c -sDEVICE=png256 -r600 -o '+file_name+'.png '+file_name+'.ps')

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
