#!/usr/bin/python


from primes import getLeastCommonMultiple, getLCM, genPrimes, prod


def euler5(maxDivisor=20):
  #divisors = range(2, maxDivisor + 1)
  #print('The least common multiple of integers from 1 to %d is %d'
  #      % (maxDivisor, getLeastCommonMultiple(*divisors)))
  #print('The least common multiple of integers from 1 to %d is %d'
  #      % (maxDivisor, getLCM(*divisors)))
  
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
  args = (eval(a) for a in sys.argv[1:])
  euler5(*args)
