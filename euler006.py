#!/usr/bin/python


from primes import *


def sumSquares(n):
  # 1^2 + 2^2 + ... + n^2
  return n * (n + 1) * (2 * n + 1) / 6


def squareOfSum(n):
  # (1 + 2 + ... + n)^2
  s = n * (n + 1) / 2
  return s * s


def sumSquareDiff(n):
  # sum(1 + 2 + ... + n)^2 - (1^2 + 2^2 + ... + n^2)
  return n * (n + 1) * (n - 1) * (3 * n + 2) / 12


def euler6(n=100):
  print('Sum of square for first %d natural numbers is %d' % (n, sumSquares(n)))
  print('Square of sum for first %d natural numbers is %d' %(n, squareOfSum(n)))
  print('Sum of squares difference for first %d natural numbers is %d'
        % (n, sumSquareDiff(n)))
  

if __name__ == "__main__":
  euler6()
