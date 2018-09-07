from PIL import Image,ImageOps
import os
import numpy as np
import subprocess

def main():
  import clear_temp_files as CTF
  import build_latex_file as BLF
  import crop as C
  # CTF.main()
  # CTF.main()
  # file_name = 'MOONS'
  # build_latex_file(file_name)
  # build_eps_from_latex(file_name)
  # eps_to_png(file_name)
  # delete_auxiliary_files_present_dir(['.aux','.txt','.dvi','.out','.log','.blg','.gz','.synctex.gz'])
  # auto_crop(file_name+'.png',0.9)

def build_eps_from_latex(file_name):
  subprocess.run('latex --jobname='+file_name+' '+file_name+'.tex')
  subprocess.run('dvips '+file_name+'.dvi')

def eps_to_png(file_name):
  subprocess.run('gswin64c -sDEVICE=png256 -r600 -o '+file_name+'.png '+file_name+'.ps')

if __name__ == '__main__':
  main()
