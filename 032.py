#!/usr/bin/python


from digit_math import genDigits, intToStr
import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def genDigitsFromList(digitList, maxNumber, maxDigits, base):
  # yield digits, intValue, digitsRemaining
  
  for n, d in enumerate(digitList):
    if d > maxNumber:
      raise StopIteration()
    yield [d], d, digitList[:n] + digitList[(n+1):]

  passMaxDigits = maxDigits - 1
  if passMaxDigits:
    for n, d in enumerate(digitList):
      passRemain = digitList[:n] + digitList[(n+1):]
      passMaxNumber = (maxNumber - d) / base
      genSubDigits = genDigitsFromList(passRemain, passMaxNumber,
                                       passMaxDigits, base)
      for digits, val, digRemain in genSubDigits:
        yieldDigits = digits + [d]
        yieldVal = base * val + d
        if yieldVal > maxNumber:
          raise StopIteration()
        yield yieldDigits, yieldVal, digRemain
  

def genPanDigitalProducts(maxDigit=9, displayResults=False, base=10):
  allDigits = list(range(1, maxDigit+1))
  maxDigits1 = (maxDigit - 1) / 2
  maxDigits1p2 = (maxDigit + 1) / 2
  maxVal1 = base**maxDigits1 - 1
  for digits1, d1, remain1 in genDigitsFromList(allDigits, maxVal1, maxDigits1,
                                                base):
    maxDigits2 = min(len(digits1), maxDigits1p2 - len(digits1))
    for digits2, d2, remain2 in genDigitsFromList(remain1, d1, maxDigits2,
                                                  base):
      # form product
      prod = d1 * d2
      # test if expression is pan-digital (no digits should remain)
      digitsProd = sorted(genDigits(prod, base))
      if digitsProd == remain2:
        if displayResults:
          if base == 10:
            print('%d x %d == %d' % (d1, d2, prod))
          else:
            print('%s x %s == %s (base %d)'
                  % (intToStr(d1, base), intToStr(d2, base),
                     intToStr(prod, base), base)
                 )
        yield prod


def euler32(maxDigit=9, base=10, displayResults=False):
  prods = set(genPanDigitalProducts(maxDigit, displayResults, base))
  prodSum = sum(prods)
  print('Sum of all products in 1-%d pan-digital expressions (base %d) is %d'
        % (maxDigit, base, prodSum))


if __name__ == "__main__":
  args = tuple(eval(a) for a in sys.argv[1:])
  euler32(*args)
