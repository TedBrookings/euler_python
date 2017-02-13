#!/usr/bin/python


from digit_math import genDigits, digitsToInt, digitsToStr
import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def genConcatenatedPandigitalProducts(base, maxDigit):
  # generate concatenated pan-digital products, and yield a tuple with:
  #   pandigitalValue,
  #   pandigital string (in correct base),
  #   starting number string (in correct base),
  #   n, the max concatenated product integer
  maxPandigital = list(range(maxDigit, 0, -1))
  maxStartDigits = maxDigit / 2
  maxStartVal = digitsToInt(range(maxDigit, maxDigit - maxStartDigits, -1),
                            base)
  for startVal in range(1, maxStartVal):
    digits = list(genDigits(startVal, base, leastFirst=False))
    for n in range(2, maxDigit + 1):
      digits += list(genDigits(startVal * n, base, leastFirst=False))
      if sorted(digits, reverse=True) == maxPandigital:
        pandigitalValue = digitsToInt(digits, base)
        pandigitalStr = digitsToStr(digits, base)
        startValStr = digitsToStr(genDigits(startVal, base=base), base=base)
        yield pandigitalValue, pandigitalStr, startValStr, n
      elif len(digits) >= maxDigit:
        break


def euler38(base=10, maxDigit=None):
  if maxDigit is None:
    maxProd = max(genConcatenatedPandigitalProducts(base, base-1),
                  key=lambda x:x[0])
    print('Maximal pandigital product (base %d) is %s = %s * (1 - %d)'
          % ((base,) +  maxProd[1:]))
  else:
    maxProd = max(genConcatenatedPandigitalProducts(base, maxDigit),
                  key=lambda x:x[0])
    print('Maximal 1-%d (base %d) pandigital product is %s = %s * (1 - %d)'
          % ((maxDigit, base) + maxProd[1:]))


if __name__ == '__main__':
  args = tuple(eval(a) for a in sys.argv[1:])
  euler38(*args)
