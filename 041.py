#!/usr/bin/python


from digit_math import digitsToInt, genDigits
from permutation import genPermutation
from primes import isPrime, genPrimeFactors
from math import factorial
import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def genPandigitalNums(numDigits, base=10, skipImpossible=True):
  # generate all pandigital numbers with a given number of digits in specified
  # base
  digits = list(range(numDigits, 0, -1))
  if skipImpossible:
    # skip testing digits that can't possibly work
    dSum = sum(digits)
    while dSum >= base:
      sumDigits = list(genDigits(dSum, base=base))
      dSum = sum(sumDigits)
    if any(dSum % f == 0 for f in set(genPrimeFactors(base-1))):
      # sum of digits evenly is a multiple of a factor of base-1, so all
      # pandigital numbers will be multiples of some factor of base-1
      raise StopIteration()
  for permuteIndex in range(factorial(numDigits)):
    yield digitsToInt(genPermutation(permuteIndex, elements=digits), base=base)


def euler41(base=10, skipImpossible=True):
  foundPrime = False
  if skipImpossible:
    nStart = base-3
  else:
    nStart = base-1
  for n in range(nStart, 1, -1):
    for pd in genPandigitalNums(n, base=base, skipImpossible=skipImpossible):
      if isPrime(pd):
        foundPrime = True
        break
    if foundPrime:
      break
  
  if not foundPrime:
    print("No prime pandigital numbers (base %d)" % base)
    return None
  elif base == 10:
    print('%d is the largest pandigital prime (base 10)' % pd)
  else:
    from digit_math import intToStr
    pdStr = intToStr(pd, base=base)
    print('%s is the largest pandigital prime (base %d)' % (pdStr, base))
  return pd


def _parseArguments():
  import argparse
  parser = argparse.ArgumentParser(description=
    "Compute the solution to Project Euler problem # 41",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--base", "-b", help="specify base", default=10,type=int)
  parser.add_argument("--try-impossible", "-s", action='store_false',
                      help="try to find primes for n even if no n-digit "
                           "pandigital could be prime", dest='skipImpossible')
  return parser.parse_args()


if __name__ == "__main__":
  options = _parseArguments()
  euler41(base=options.base, skipImpossible=options.skipImpossible)
