#!/usr/bin/python


def euler1(maxInt=1000, primeSet={3, 5}):
  multiples = [n for n in range(1, maxInt) if any(n % p == 0 for p in primeSet)]
  setStr = ' '.join('%s' % p for p in primeSet)
  print('Sum of multiples of [%s] less than %d = %d' %
        (setStr, maxInt, sum(multiples)))


def _parseArguments():
  import sys
  arguments = sys.argv
  if len(arguments) >= 2:
    maxInt = int(arguments[1])
  else:
    maxInt = 1000
  if len(arguments) >= 3:
    primeSet = {int(a) for a in arguments[2:]}
  else:
    primeSet = {3, 5}
  return maxInt, primeSet


if __name__ == "__main__":
  maxInt, primeSet = _parseArguments()
  euler1(maxInt, primeSet)
