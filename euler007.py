#!/usr/bin/python


import itertools
from primes import genPrimes
from number_words import getRankName


def euler7(n=10001):
  p = next(itertools.islice(genPrimes(), n - 1, n))
  print('%s prime is %d' % (getRankName(n), p))
  

if __name__ == "__main__":
  euler7()
