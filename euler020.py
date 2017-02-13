#!/usr/bin/python


from math import factorial
from digit_math import genDigits


def euler20(factNum=100):
  digitSum = sum(genDigits(factorial(factNum)))
  print('Sum of digits in %d! is %d' % (factNum, digitSum))
  

if __name__ == "__main__":
  euler20()
