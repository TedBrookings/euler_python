#!/usr/bin/python


from fibonacci import genFibonacci


def euler2(maxFib=4000000):
  sumOfEvenFibs = sum(f for f in genFibonacci(maxFib) if f & 1 == 0)
  print('Sum of even Fibonnaci numbers less or equal to %d = %d'
        % (maxFib, sumOfEvenFibs))
  

def _parseArgs():
  import sys
  arguments = sys.argv
  if len(arguments) >= 2:
    maxFib = int(float(arguments[1]))
  else:
    maxFib = 4000000
  return maxFib


if __name__ == "__main__":
  maxFib = _parseArgs()
  euler2(maxFib)
