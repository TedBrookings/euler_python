#!/usr/bin/python


from primes import genPrimes, isPrime, genPrimeFactors
from digit_math import genDigits


def genLeftTruncatablePrimes(base=10, singleDigit=False):
  # generate left-truncatable primes in specified base
  
  leftTruncatable = list(genPrimes(maxPrime=base-1))
  if singleDigit:
    for p in leftTruncatable:
      yield p
  
  digitVal = 1
  while leftTruncatable:
    basePrimes = leftTruncatable
    leftTruncatable = list()
    digitVal *= base
    for p in basePrimes:
      for d in range(1, base):
        p += digitVal
        if isPrime(p):
          leftTruncatable.append(p)
          yield p
    

def genRightTruncatablePrimes(base=10, singleDigit=False):
  # generate right-truncatable primes in specified base
  
  rightTruncatable = list(genPrimes(maxPrime=base-1))
  if singleDigit:
    for p in rightTruncatable:
      yield p

  # get a set of digits that can never be added to right-truncatable primes
  baseFactors = set(genPrimeFactors(base))
  excludeDigits = {0}
  while baseFactors:
    factor = baseFactors.pop()
    digit = factor
    while(digit < base):
      excludeDigits.add(digit)
      digit += factor
  # get the list of digits that can be added to right-truncatable primes
  allowedDigits = [d for d in range(base) if d not in excludeDigits]
  
  while rightTruncatable:
    basePrimes = rightTruncatable
    rightTruncatable = list()
    for p in basePrimes:
      p *= base
      for d in allowedDigits:
        pTest = p + d
        if isPrime(pTest):
          rightTruncatable.append(pTest)
          yield pTest


def isLeftTruncatable(p, base=10, singleDigit=False):
  # test if a given prime p is left-truncatable
  pDigits = list(genDigits(p, base))
  if len(pDigits) == 1:
    return singleDigit
  
  # don't bother testing first digit, assume p is prime
  pDigits.pop()

  pTest = pDigits.pop(0)
  if not isPrime(pTest):
    return False
  digitVal = base
  while pDigits:
    pTest += digitVal * pDigits.pop(0)
    if not isPrime(pTest):
      return False
    digitVal *= base
  return True


def isRightTruncatable(p, base=10, singleDigit=False):
  # test if a given prime p is right-truncatable
  
  if p < base:
    return singleDigit
  p /= base
  while p > base:
    if not isPrime(p):
      return False
    p /= base
  return isPrime(p)


def euler37(base=10, display=False):
  if display:
    import sys
    pSum = 0
    for p in genRightTruncatablePrimes(base):
      if isLeftTruncatable(p, base):
        sys.stdout.write(' %d' % p)
        sys.stdout.flush()
        pSum += p
      else:
        sys.stdout.write(' ~%d' % p)
        sys.stdout.flush()
    sys.stdout.write('\n')
  else:
    pSum = sum(p for p in genRightTruncatablePrimes(base)
               if isLeftTruncatable(p, base))
  print('Sum of all left- and right-truncatable primes (base %d) is %d'
        % (base, pSum))


if __name__ == "__main__":
  import sys
  args = (eval(a) for a in sys.argv[1:])
  #print(list(genRightTruncatablePrimes(*args)))
  euler37(*args)
