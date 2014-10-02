#!/usr/bin/python


import operator
from collections import deque
import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def prod(iterable):
  return reduce(operator.mul, iterable, 1)


def genFileDigits(fileName):
  """
  Open specified file and generate sequence of digits (as integers)
  """
  with open(fileName, 'r') as fIn:
    digit = fIn.read(1)
    while digit:
      yield int(digit)
      digit = fIn.read(1)
      while digit == '\n':
        digit = fIn.read(1)
    

def genDigitProducts(fileName, numDigits=5):
  """
  Open specified file and generate all possible sequences of numDigits digits.
  for each sequence of digits: yield prod(digits), digits
  """
  genDigit = genFileDigits(fileName)
  digits = deque([next(genDigit) for n in range(numDigits)])
  digitsProd = prod(digits)
  while True:
    yield digitsProd, digits
    oldDigit = digits.popleft()
    if oldDigit:
      digitsProd /= oldDigit
    else:
      digitsProd = prod(digits)
    nextDigit = next(genDigit)
    digitsProd *= nextDigit
    digits.append(next(genDigit))


def euler8(numDigits=5, numberFile='data/euler008.txt'):
  maxProd, maxDigits = max(genDigitProducts(numberFile, numDigits),
                           key=lambda p: p[0])
  maxDigitStr = '{' + ' '.join('%d' % d for d in maxDigits) + '}'
  print('Max product of %d digits in number is %d, from the digits %s'
        % (numDigits, maxProd, maxDigitStr))
  

if __name__ == "__main__":
  args = tuple(eval(a) for a in sys.argv[1:])
  euler8(*args)
