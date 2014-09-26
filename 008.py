#!/usr/bin/python


import operator


def prod(iterable):
  return reduce(operator.mul, iterable, 1)


def genFileDigits(fileName):
  with open(fileName, 'r') as fIn:
    digit = fIn.read(1)
    while digit:
      yield int(digit)
      digit = fIn.read(1)
      while digit == '\n':
        digit = fIn.read(1)
    

def genDigitProductLists(fileName, numDigits=5):
  digit = genFileDigits(fileName)
  digitList = [next(digit) for n in range(numDigits)]
  while True:
    yield digitList
    digitList = digitList[1:] + [next(digit)]


def euler8(numDigits=5, numberFile='data/euler008.txt'):
  digitProductList = genDigitProductLists(numberFile, numDigits)
  maxDigits = max(digitProductList, key=lambda x: prod(x))
  maxDigitStr = '{' + ' '.join('%d' % d for d in maxDigits) + '}'
  print('Max product of %d digits in number is %d, from the digits %s'
        % (numDigits, prod(maxDigits), maxDigitStr))
  

if __name__ == "__main__":
  euler8()
