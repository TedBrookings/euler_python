#!/usr/bin/python


from primes import getLeastCommonMultiple, getLCM, genPrimes, prod


def euler5(maxDivisor=20):
  def _getMaxPow(p, maxDivisor):
    maxPow, nextPow = p, p*p
    while nextPow < maxDivisor:
      maxPow = nextPow
      nextPow *= p
    return maxPow
  lcm = prod(_getMaxPow(p, maxDivisor)
             for p in genPrimes(maxPrime=maxDivisor))
  print('The least common multiple of integers from 1 to %d is %d'
        % (maxDivisor, lcm))
  

if __name__ == "__main__":
  import sys
  args = tuple(eval(a) for a in sys.argv[1:])
  euler5(*args)
