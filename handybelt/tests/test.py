import argparse

def main(**kwargs):
  print('------ main')
  # print(args)
  print(kwargs)
  print('------')
  # print(a1)
  print('------')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Test')
  parser.add_argument('a1',type=int,help='a1')
  parser.add_argument('a2',type=int,help='a2')
  parser.add_argument('--a3',type=int,help='a3')
  parser.add_argument('--a4',type=int,help='a4')
  args = parser.parse_args()
  V = vars(args)
  main(**V)

# Test:
# python test.py 1 2 --a3 3
