import argparse
import subprocess
import os
from cleartempfiles.__main__ import cleartempfiles as CTF

def main():
  parser = argparse.ArgumentParser(description='Builds a Latex file.')
  parser.add_argument('filename',
    type=str,
    default='',
    help='File to be built')
  args = parser.parse_args()

  subprocess.check_call(['xelatex', args.filename])
  path = os.path.dirname(args.filename)
  path = '.' if path=='' else path
  CTF(path)

if __name__ == '__main__':
  main()
