#!/usr/bin/python


from primes import *
  

def getTriangleDivisors(n):
  # get the number of divisors of the nth triangle number
  triangle = n * (n + 1) / 2
  divisors = getDivisors(triangle)
  numTriangle = len(divisors)
  return triangle, divisors, numTriangle


def euler12(numDivisors=500, printDivisors=False):
  n = 1
  numTriangle = 1
  while numTriangle < numDivisors:
    n = n + 1
    triangle, divisors, numTriangle = getTriangleDivisors(n)
  
  if printDivisors:
    print('Triangle %d has %d divisors: %s'
        % (triangle, numTriangle, ' '.join('%d' % d for d in sorted(divisors))))
  else:
    print('Triangle %d has %d divisors' % (triangle, numTriangle))


if __name__ == "__main__":
  euler12()
