#!/usr/bin/python


from primes import *


def euler3(testNum=600851475143):
  print('Largest prime factor of %d is %d'
        % (testNum, max(genPrimeFactors(testNum))))
  

if __name__ == "__main__":
  euler3()
