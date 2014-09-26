#!/usr/bin/python


from digit_math import genDigitFuncSums
from number_words import getRankName


def euler30(digitPower=5, base=10, display=False):
  func = lambda x: x**digitPower
  sumVal = sum(genDigitFuncSums(func, base=base, display=display))
  funcName = getRankName(digitPower) + ' power'
  print('Sum of all numbers equal to sum of %s of their digits (base %d) is %d'
        % (funcName, base, sumVal))


if __name__ == "__main__":
  euler30()
