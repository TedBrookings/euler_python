#!/usr/bin/python


from primes import isPrime, genPrimeFactors
import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def allowedDigitsToInt(digits, allowedDigits, base=10):
  # convert array of digits to an integer
  
  # first get an iterator to digits
  if not hasattr(digits, 'next'):
    # digits is an iterator
    digits = iter(digits)
  # now loop through digits, updating num
  num = allowedDigits[next(digits)]
  for d in digits:
    num *= base
    num += allowedDigits[d]
  return num


def genCirclePrimes(maxPrime=float('inf'), base=10):
  # get the 1-digit circular primes
  for d in range(2, base):
    if isPrime(d):
      yield d
  
  # get a set of digits that can never be in multi-digit circular primes
  baseFactors = set(genPrimeFactors(base))
  excludeDigits = {0}
  while baseFactors:
    factor = baseFactors.pop()
    digit = factor
    while(digit < base):
      excludeDigits.add(digit)
      digit += factor
  
  # get the list of digits that can be in multi-digit circular primes
  allowedDigits = [d for d in range(base) if d not in excludeDigits]
  numAllowed = len(allowedDigits)
  lastAllowed = numAllowed - 1
  
  numDigits = 2
  digits = [0] * numDigits
  num = allowedDigitsToInt(digits, allowedDigits, base)
  while num <= maxPrime:
    # check if num represents a circular prime
    if isPrime(num):
      # check if num is circular
      shiftDigits = [digits[-1]] + digits[:-1]
      if shiftDigits == digits:
        # num is automatically circular
        yield num
      else:
        circlePrimes = { num }
        shiftNum = allowedDigitsToInt(shiftDigits, allowedDigits, base)
        while isPrime(shiftNum):
          circlePrimes.add( shiftNum )
          if len(circlePrimes) == numDigits:
            for p in circlePrimes:
              yield p
            break
          shiftDigits = [shiftDigits[-1]] + shiftDigits[:-1]
          shiftNum = allowedDigitsToInt(shiftDigits, allowedDigits, base)
    
    # increment digits, ensuring that the smallest digit is digits[0]
    j = numDigits - 1
    while digits[j] == lastAllowed:
      if j == 0:
        numDigits += 1
        digits = [0] * numDigits
        j = None
        break
      digits[j] = digits[0] + 1
      j -= 1
    if j is not None:
      if j == 0:
        digits = [digits[0] + 1] * numDigits
      else:
        digits[j] += 1
    
    num = allowedDigitsToInt(digits, allowedDigits, base)


def euler35(maxPrime=10**6, base=10):
  circlePrimes = list(genCirclePrimes(maxPrime, base))
  print('There are %d circle primes (base %d) below %d'
        % (len(circlePrimes), base, maxPrime))


if __name__ == "__main__":
  import sys
  euler35(*(eval(a) for a in sys.argv[1:]))
