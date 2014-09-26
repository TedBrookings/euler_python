#!/usr/bin/python

import operator
from math import sqrt, ceil
import sys
write = sys.stdout.write


_primes = [2, 3, 5]


def prod(iterable):
  return reduce(operator.mul, iterable, 1)


def isPrime(num):
  for p in genPrimes(maxPrime=sqrt(num)):
    if not num % p:
      return False
  return num > 1


def genPrimes(maxPrime=float('Inf')):
  global _primes
  for p in _primes:
    if p > maxPrime:
      raise StopIteration()
    yield p
  
  def _isPrime(num):
    # use special _isNotPrime because here we know enough primes have been
    #  found to only check the array _primes
    _maxPrime = sqrt(num)
    #iPrime = iter(_primes) ; next(iPrime) ; next(iPrime)
    #for pt in iPrime:
    for pt in _primes:
      if not num % pt:
        return False
      elif pt > _maxPrime:
        return True
    return True
     
  p = _primes[-1] + 2
  if p > maxPrime:
    raise StopIteration()
  
  if p % 3:
    if _isPrime(p):
      _primes.append(p)
      yield p
    p += 4
  else:
    p += 2
  
  while p <= maxPrime:
    if _isPrime(p):
      _primes.append(p)
      yield p
    p += 2
    
    if p > maxPrime:
      raise StopIteration()
    if _isPrime(p):
      _primes.append(p)
      yield p
    p += 4


def genPrimeFactors(num):
  maxP = sqrt(num)
  for p in genPrimes(maxPrime=maxP):
    if p > maxP:
      break
    if num % p == 0:
      yield p
      if num == p:
        raise StopIteration()
      num /= p
      while num % p == 0:
        yield p
        if num == p:
          raise StopIteration()
        num /= p
      maxP = sqrt(num)
  if num > 1:
    yield num


def getDivisors(num, proper=False):
  # return set of all the divisors of num
  # if proper is True, don't include num in set of divisors
  divisors = set()
  maxDivisor = num
  if proper:
    maxDivisor -= 1
  maxP = sqrt(num)
  for p in genPrimes(maxPrime=maxP):
    if p > maxP:
      break
    while num % p == 0:
      newDivisors = [p * d for d in divisors]
      divisors.update(newDivisors)
      divisors.add(p)
      num /= p
      maxP = num**0.5
  newDivisors = [num] + [num * d for d in divisors]
  divisors.update(nd for nd in newDivisors if nd <= maxDivisor)
  divisors.add(1) # 1 is a divisor
  return divisors


def getLCM(n1, n2, *numList):
  gcd = getGreatestCommonDivisor(n1, n2)
  lcm = n1 * (n2 / gcd)
  for n in numList:
    gcd = getGreatestCommonDivisor(lcm, n)
    lcm *= (n / gcd)
  return lcm
  

def getLeastCommonMultiple(*numList):
  if len(numList) == 2:
    n1, n2 = numList[:]
    return n1 * (n2 / getGreatestCommonDivisor(n1, n2))
  
  factorMap = {}
  for num in numList:
    numMap = {}
    for f in genPrimeFactors(num):
      if f in numMap:
        numMap[f] += 1
      else:
        numMap[f] = 1
    
    for f, power in numMap.items():
      if f not in factorMap:
        factorMap[f] = power
      else:
        factorMap[f] = max(power, factorMap[f])
  
  f, power = factorMap.popitem()
  lcm = f ** power
  for f, power in factorMap.items():
    lcm *= f ** power
  return lcm

  factors = []
  maxP = sqrt(num)
  for p in genPrimes(maxPrime=maxP):
    if p > maxP:
      break
    while num % p == 0:
      factors.append(p)
      num /= p
      maxP = sqrt(num)
  factors.append(num)
  return factors


  
def getGreatestCommonDivisor(n1, n2, *numList):
  if n1 == 0:
    return n2
  elif n2 == 0:
    return n1
  
  # remove all common powers of two from n1 and n2
  numPowersOfTwo = 0
  while (n1 | n2) & 1 == 0:
    n1 >>= 1 ; n2 >>= 1
    numPowersOfTwo += 1
  
  # now either n1 is odd, n2 is odd, or both are odd
  # 2 is not a common divisor, so remove any factors of 2 from n1
  while n1 & 1 == 0:
    n1 >>= 1
  # now n1 is odd
  
  while n2 != 0:
    # remove all factors of 2 from n2, since n1 is definitely odd
    while n2 & 1 == 0:
      n2 >>= 1
    
    # now n1 and n2 are both odd
    if n1 > n2:
      n1, n2 = n2, n1 - n2
    else:
      n2 -= n1
  
  if numList:
    gcd = n1 << numPowersOfTwo
    for n in numList:
      gcd = getGreatestCommonDivisor(gcd, n)
    return gcd
  else:
    return n1 << numPowersOfTwo
  
  

def testPrimes(mag=12):
  import random
  random.seed()
  minNum = 10**((mag-1)/2)
  maxNum = 10**((mag)/ 2)
  num1, num2, numProd = (random.randint(minNum, maxNum) for n in range(3))
  num1 *= numProd
  num2 *= numProd
  factors = list(genPrimeFactors(num1))
  factorStr = ' '.join('%d' % f for f in factors)
  if num1 == prod(factors):
    # it worked!
    print('Prime factors of %d are %s' % (num1, factorStr))
    divisorStr = ' '.join('%d' % d for d in sorted(getDivisors(num1)))
    print('Divisors of %d are %s' % (num1, divisorStr))
  else:
    print('Failure. Incorrectly reports prime factors of %d are %s'
      % (num1, factorStr))
  
  gcd = getGreatestCommonDivisor(num1, num2)
  lcm = getLeastCommonMultiple(num1, num2)
  if num1 * num2 / gcd == lcm:
    print('Greatest common divisor of %d and %d is %d' % (num1, num2, gcd))
    print('Least common multiple of %d and %d is %d' % (num1, num2, lcm))
  else:
    print('Failure: found greatest common divisor of %d and %d is %d'
          % (num1, num2, gcd))
    print('Failure: found least common multiple of %d and %d is %d'
          % (num1, num2, lcm))
    factors = list(genPrimeFactors(num2))
    factorStr = ' '.join('%d' % f for f in factors)
    print('Prime factors of %d are %s' % (num2, factorStr))


def primeTestRandom(mag=11, numTest=10**5):
  import random
  random.seed()
  dFact = {}
  minNum = 10**mag
  maxNum = 10 * minNum
  for nTest in range(numTest):
    num = random.randint(minNum, maxNum)
    divisors = getDivisors(num)
    for d in divisors:
      if d in dFact:
        dFact[d] += 1
      else:
        dFact[d] = 1
  nFloat = float(nTest)
  for key, val in dFact.items():
    if key < 1000:
      ratio = val/nFloat * key
      print('%d: %g' % (key, ratio))
    
if __name__ == "__main__":
  testPrimes()
  #primeTestRandom()
