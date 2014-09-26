#!/usr/bin/python


from primes import genPrimes


def euler10(maxPrime=2000000):
  s = sum(genPrimes(maxPrime=maxPrime))
  print('Sum of primes less than %d = %d' % (maxPrime, s))
  

if __name__ == "__main__":
  import sys
  args = (int(float(a)) for a in sys.argv[1:])
  euler10(*args)
