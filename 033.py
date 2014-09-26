#!/usr/bin/python


import operator
from primes import getGreatestCommonDivisor


def prod(iterable):
  return reduce(operator.mul, iterable, 1)


def genDigitCancelingFractions(base, display=False):
  for c in range(1, base):
    c10 = c * base
    for d1 in range(1, base):
      dCancel1 = d1 * base + c
      dCancel2 = c10 + d1
      for n1 in range(1, d1):
        nCancel1 = n1 * base + c
        nCancel2 = c10 + n1
        if nCancel1 * d1 == n1 * dCancel1:
          if display:
            print('%d%d/%d%d == %d/%d' % (n1, c, d1, c, n1, d1))
          yield n1, d1
        if nCancel2 * d1 == n1 * dCancel1:
          if display:
            print('%d%d/%d%d == %d/%d' % (c, n1, d1, c, n1, d1))
          yield n1, d1
        if nCancel1 * d1 == n1 * dCancel2:
          if display:
            print('%d%d/%d%d == %d/%d' % (n1, c, c, d1, n1, d1))
          yield n1, d1
        if nCancel2 * d1 == n1 * dCancel2:
          if display:
            print('%d%d/%d%d == %d/%d' % (c, n1, c, d1, n1, d1))
          yield n1, d1


def euler33(base=10, display=False):
  # get the numerators and denominators of the digit-canceling fractions
  nums, denoms = zip(*list(genDigitCancelingFractions(base, display)))
  # take the product
  num, denom = prod(nums), prod(denoms)
  # find the greatest common factor of the numerator and denominator
  gcf = getGreatestCommonDivisor(num, denom)
  # put the denominator in proper form
  denom /= gcf
  
  import sys
  write = sys.stdout.write
  write('The denominator of the product of digit-canceling fractions (base %d) '
        % base)
  write('is %d when the fraction is in proper form\n' % denom)


if __name__ == "__main__":
  euler33()
