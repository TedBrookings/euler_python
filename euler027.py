#!/usr/bin/python


from primes import genPrimes, _primes
from math import sqrt
import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def isPrime(num):
  if num < 2:
    return False
  for p in genPrimes(maxPrime=sqrt(num)):
    if not num % p:
      return False
  return True


def genPrimeCoefficients(maxAbs_a, maxAbs_b):
  for b in genPrimes(maxPrime=maxAbs_b):
    minA = max(1 - maxAbs_a, 2 - b)
    for a in range(minA, maxAbs_a):
      n = 1 # already know b is prime!
      while isPrime(n * (n + a) + b):
        n += 1
      yield (n, (a, b), a * b)


def euler27(maxAbs_a=1000, maxAbs_b=1000):
  maxCoefs = max(genPrimeCoefficients(maxAbs_a, maxAbs_b), key = lambda x: x[0])
  print('With (a,b) = %s, n^2 + an + b is prime for n in [0,%d]. a * b = %d'
         % (str(maxCoefs[1]), maxCoefs[0], maxCoefs[2]))


if __name__ == "__main__":
  euler27()
