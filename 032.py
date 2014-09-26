#!/usr/bin/python


from digit_math import genDigits


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
          print('%d x %d == %d' % (d1, d2, prod))
        yield prod
  

def euler32(maxDigit=9, displayResults=False, base=10):
  prods = set(genPanDigitalProducts(maxDigit, displayResults, base))
  prodSum = sum(prods)
  print('Sum of all products in 1-%d pan-digital expressions is %d'
        % (maxDigit, prodSum))


if __name__ == "__main__":
  euler32()
