import subprocess

def main():
  parser = argparse.ArgumentParser(description='Builds a Latex file.')
  parser.add_argument('filename',
    type=str,
    default='',
    help='File to be built')
  args = parser.parse_args()

  subprocess.check_call(['xelatex', args.filename])

if __name__ == '__main__':
  main()
