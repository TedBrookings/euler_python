#!/usr/bin/python


from digit_math import digitSum, getNumDigits, digitsToStr



def getNumbersEasy(fileName):
  # read in numbers, using python's built-in support for arbitrary length
  # integers
  numbers = []
  with open(fileName, 'r') as fIn:
    for line in fIn:
      numbers.append(int(line))
  return numbers
    

def euler13(numberFile='data/euler013.txt', numDigits=10):
  # compute sum, using python's built-in support for arbitrary length integers
  print('Doing sum the easy way ' 
    + "(using python's built-in arbitrary precision ints):")
  s = sum( getNumbersEasy(numberFile) )
  numDigits_S = getNumDigits(float(s))
  if numDigits_S > numDigits:
    s /= 10**(numDigits_S - numDigits)
  print('First %d digits of sum: %d' % (numDigits, s))
    

def getNumbersHard(fileName):
  # read in numbers as digits
  with open(fileName, 'r') as fIn:
    for line in fIn:
      yield [int(d) for d in line.strip()]


def euler13Hard(numberFile = 'data/euler013.txt', numDigits=10):
  print('Doing sum the hard way ' 
    + '(writing own array-based arbitrary precision ints):')
  # compute sum
  s = digitSum( getNumbersHard(numberFile) )
  print('First %d digits of sum: %s' % (numDigits, digitsToStr(s[:numDigits])))

if __name__ == "__main__":
  euler13()
  euler13Hard()
