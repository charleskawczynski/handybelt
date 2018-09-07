import argparse
import subprocess

def main():
  from handybelt.cleartempfiles.__main__ import cleartempfiles as CTF
  parser = argparse.ArgumentParser(description='Builds a Latex file.')
  parser.add_argument('filename',
    type=str,
    default='',
    help='File to be built')
  args = parser.parse_args()

  subprocess.check_call(['xelatex', args.filename])
  CTF()

if __name__ == '__main__':
  main()
