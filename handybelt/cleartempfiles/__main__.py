import argparse
import os

def cleartempfiles(path):
  temp_extensions = ['.aux','.txt','.out','.log','.blg','.gz','.toc','.lof','.lot','.bcf','.synctex.gz','.gz(busy)','.nav','.xml','.snm']
  for f in os.listdir(path):
    f_full = path+os.sep+f
    for e in temp_extensions:
      if f.endswith(e):
        if os.path.isfile(f_full):
          try:
            os.remove(f_full)
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
