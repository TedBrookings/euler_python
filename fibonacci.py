#!/usr/bin/python


from math import sqrt, log, log1p, ceil
from unitTests import testAssert
import sys


def getNthFibonacci(n):
  # Directly compute the nth Fibonacci number
  root5 = sqrt(5.0)
  a = (1.0 + root5) / 2.0
  b = a - root5
  nthFib = int(round((a**n - b**n) / root5))
  return nthFib


def logNthFibonacci(n, base=None):
  # Compute the log of the nth Fibonacci number (default is natural log)
  root5 = sqrt(5.0)
  a = (1.0 + root5) / 2.0
  b = a - root5
  # note log1p(x) compute log(1 + x) accurately for small x
  logNthFib = n * log(a) + log1p( -(b/a)**n ) - log(root5)
  if base is None:
    return logNthFib
  else:
    return logNthFib / log(base)


def getNumDigitsFibonacci(n, base=10):
  # Compute the number of digits in the nth term of the Fibonacci sequence
  # should check when approximation becomes accurate for base != 10
  if n < 10:
    if n == 1:
      return 1
    else:
      return int(1 + logNthFibonacci(n, base))
  root5 = sqrt(5)
  a = (1.0 + root5) / 2.0
  numDigits = int(1 + n * log(a, base) - log(root5, base))
  return numDigits


def firstFibonacciTermWithNDigits(n, base=10):
  """
  Compute the term number of the first Fibonacci number with n digits
  should check when approximation becomes accurate for base != 10
  """
  if n == 1:
    return 1
  root5 = sqrt(5)
  a = (1.0 + root5) / 2.0
  termNum = 1 + int( (n - 1 + log(root5, base)) / log(a, base) )
  return termNum


def genFibonacci(maxFibonacci=float('inf')):
  """
  generate the numbers of the Fibonacci sequence
  """
  if maxFibonacci < 1:
    raise StopIteration()
  f1 = 1
  yield f1
  f2 = 1
  while f2 < maxFibonacci:
    yield f2
    f1, f2 = f2, f1 + f2
  if f2 == maxFibonacci:
    yield f2


def test(maxFibDigits=10000, testBases=[2, 10, 12], maxAccurateCalcTerm=70):
  """
  Test the functions in fibonacci.py
  """
  from number_words import getRankName
  sys.stdout.write('Testing fibonacci... ')
  sys.stdout.flush()

  for base in testBases:
    n = 0
    numFibDigits = 1
    nextFibCheck = base
    for fib in genFibonacci():
      n += 1
      rankName = getRankName(n)
      while fib >= nextFibCheck:
        numFibDigits += 1
        nextFibCheck *= base
      if n <= maxAccurateCalcTerm:
        fibCalc = getNthFibonacci(n)
        testAssert( fibCalc == fib,
                    "Generated %s fibonacci as %d, calculated as %d (err=%d)"
                    % (rankName, fib, fibCalc, fibCalc - fib)
                  )
      calcNumFibDigits = getNumDigitsFibonacci(n, base=base)
      testAssert( calcNumFibDigits == numFibDigits,
                  "%s fibonacci number has %d digits, but calculated %d"
                  % (rankName, numFibDigits, calcNumFibDigits)
                )
      if numFibDigits >= maxFibDigits:
        break
  
    stopTermNum = firstFibonacciTermWithNDigits(maxFibDigits, base=base)
    testAssert( stopTermNum == n,
                "Calculated first term with %d digits was %s, however first term"
                " was actually %s"
                % (maxFibDigits, getRankName(stopTermNum), rankName)
              )
    
  print('passed')    
  

if __name__ == "__main__":
  args = tuple(eval(a) for a in sys.argv[1:])
  test()
