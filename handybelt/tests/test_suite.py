import sys
import subprocess

def main():
  # command-line tests
  subprocess.run('python -m screenshot --filename screenshot_test.png')
  subprocess.run('python -m resize screenshot_test.png .5')
  subprocess.run('python -m crop screenshot_test.png')
  subprocess.run('python -m buildlatex main.tex')
  subprocess.run('python -m buildlatex latex/main.tex')
  subprocess.run('python -m cleartempfiles latex') # already called inside buildlatex, but works
  subprocess.run('python -m buildlatex latexPPT/main.tex')

  subprocess.run('python -m pdf2img graph.pdf')
  subprocess.run('python -m pdf2img graph/graph.pdf')

  subprocess.run('python -m latex2img main.tex')
  subprocess.run('python -m latex2img latex/main.tex')

  # module tests
  # from cleartempfiles.__main__ import cleartempfiles as CTF
  # from screenshot.__main__ import cleartempfiles as CTF
  # from getimage.__main__ import get_image
  # from crop.__main__ import get_image

if __name__ == '__main__':
  main()
