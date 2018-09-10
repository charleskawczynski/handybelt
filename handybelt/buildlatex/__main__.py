import argparse
import subprocess
import os
from cleartempfiles.__main__ import cleartempfiles

def buildlatex(**kwargs):
  filename = kwargs['filename']
  BT = kwargs['BT']

  filename = filename.replace('/',os.sep) if '\\'==os.sep else filename.replace('\\',os.sep)
  path = os.path.dirname(filename)
  path = '.' if path=='' else path
  p, ext = os.path.splitext(filename)
  temp = p.split(os.sep)
  p, f = ['.',temp[0]] if len(temp)==1 else p.split(os.sep)
  f = f+ext

  s = BT+' -output-directory='+p+' -quiet '+f
  subprocess.check_call(s)
  cleartempfiles(path)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Builds a Latex file.')
  parser.add_argument('filename',
    type=str,
    default='',
    help='File to be built')
  parser.add_argument('BT',
    type=str,
    default='pdflatex',
    choices=['pdflatex', 'xelatex'],
    help='Build type.')
  args = parser.parse_args()
  buildlatex(**vars(args))
