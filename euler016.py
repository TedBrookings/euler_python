#!/usr/bin/python


from digit_math import genDigits


def euler16(pow2=1000):
  digitSum = sum(genDigits(2**pow2))
  print('Sum of the digits of 2^%d is %d' % (pow2, digitSum))


if __name__ == "__main__":
  euler16()
