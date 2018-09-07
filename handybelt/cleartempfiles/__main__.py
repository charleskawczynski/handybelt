import argparse
import os

def cleartempfiles(path):
  temp_extensions = ['.aux','.txt','.out','.log','.blg','.gz','.toc','.lof','.lot','.bcf','.synctex.gz','.gz(busy)','.nav','.xml','.snm']
  for e in temp_extensions:
    for f in os.listdir(path):
      if f.endswith(e):
        if os.path.isfile(f):
          try:
            os.remove(f)
          except:
            pass

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Deletes frequently generated temporary files.')
  parser.add_argument('path',
    type=str,
    default='',
    help='path where temporary files are deleted')
  args = parser.parse_args()

  cleartempfiles(args.path)
