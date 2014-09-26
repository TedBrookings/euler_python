#!/usr/bin/python


from math import sqrt, log, log1p, ceil


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
  # Compute the term number of the first Fibonacci number with n digits
  # should check when approximation becomes accurate for base != 10
  if n == 1:
    return 1
  root5 = sqrt(5)
  a = (1.0 + root5) / 2.0
  termNum = 1 + int( (n - 1 + log(root5, base)) / log(a, base) )
  return termNum


def genFibonacci(maxFibonacci=float('inf')):
  # Generate the Fibonacci sequence
  f1 = 1
  yield f1
  f2 = 1
  while f2 < maxFibonacci:
    yield f2
    f1, f2 = f2, f1 + f2


def demoFibonacci(calcTerm=50, numDigitsTerm=10**6, firstDigits=10**20):  
  # Demo some of the functions
  print('%d term of Fibonacci sequence is %d'
        % (calcTerm, getNthFibonacci(calcTerm)))
  print('Number of digits in %d term is %d'
        % (numDigitsTerm, getNumDigitsFibonacci(numDigitsTerm)))
  print('First term with %d digits is term %d'
        % (firstDigits, firstFibonacciTermWithNDigits(firstDigits)))
  
  
if __name__ == "__main__":
  demoFibonacci()
