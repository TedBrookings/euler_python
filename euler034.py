#!/usr/bin/python


from math import factorial
from digit_math import genDigitFuncSums
  

def euler34(base=10, display=False):
  sumVal = sum(genDigitFuncSums(factorial, base=base, display=display))
  print('Sum of numbers equal to the sum of %s of their digits (base %d) is %d'
        % ('the factorial', base, sumVal))


if __name__ == "__main__":
  import sys
  args = tuple(eval(a) for a in sys.argv[1:])
  euler34(*args)
