#!/usr/bin/python


from primes import getDivisors


def divisorSum(n):
  # return the sum of the proper divisors of n (divisors that are less than n)
  return sum(getDivisors(n, proper=True))


def isAmicable(a, divSums):
  # return true if a is amicable
  if a in divSums:
    aPair = divSums[a]
  else:
    aPair = divisorSum(a)
    divSums[a] = aPair
  
  if aPair in divSums:
    aPrime = divSums[aPair]
  else:
    aPrime = divisorSum(aPair)
    divSums[aPair] = aPrime
  
  return aPrime == a


def euler21(maxNum=10000):
  divSums = {}
  amicableSum = sum(a for a in range(4, maxNum) if isAmicable(a, divSums))
  print('Sum of amicable numbers less than %d is %d' % (maxNum, amicableSum))


if __name__ == "__main__":
  euler21()
