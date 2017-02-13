#!/usr/bin/python


from operator import mul
from digit_math import genDigits


def prod(iterable):
  return reduce(mul, iterable, 1)


def genChampernowneDigitsSlow(digits, base=10):
  # generate a requested list of digits from Champernowne's constant
  #   This way is slow, kept around for debugging purposes
  
  # sort the digits to get them in one pass
  sDigits = sorted(digits)

  n = 0; dTop = 0 ; n_digits = 0; check_n = 1 ; chapDigits = []
  for d in sDigits:
    # get each requested digit place, d
    if dTop < d:
      # d is large enough that n must be increased
      n += 1
      if n >= check_n:
        check_n *= base ; n_digits += 1
      #assert n_digits == len(list(genDigits(n, base=base, leastFirst=False))), \
      #   'for %d: %d != len(%s)' % (n, n_digits, str(list(genDigits(n, base=base, leastFirst=False))))
      dTop += n_digits
      while d > dTop:
        n += 1
        if n >= check_n:
          check_n *= base ; n_digits += 1
        #assert n_digits == len(list(genDigits(n, base=base, leastFirst=False))), \
        # 'for %d: %d != len(%s)' % (n, n_digits, str(list(genDigits(n, base=base, leastFirst=False))))
        dTop += n_digits
      # compute the digits of n
      chapDigits = list(genDigits(n, base=base, leastFirst=False))
    # yield the requested digit
    yield chapDigits[d - dTop - 1]


def genChampernowneDigits(digits, base=10):
  # generate a requested list of digits from Champernowne's constant
  
  # sort the digits to get them in one pass
  sDigits = sorted(digits)
  
  n = 1; dBot = 1 ; dTop = 1 ; nDigits = 1; dCheck = base; nCheck = base
  _genChap = genDigits(1, base=base, leastFirst=False)
  for d in sDigits:
    # get each requested digit place, d
    if dTop < d:
      # d is large enough that n must be increased
      while dCheck <= d:
        # d is far enough away that the number of digits of n will increase
        #  - move to check location (where # of digits increases)
        n = nCheck ; dBot = dCheck ; nDigits += 1 ; dTop = dBot + nDigits - 1
        #  - compute next check location
        nCheck *= base ; dCheck += nDigits * (nCheck - n)

      deltaN = (d - dTop + nDigits - 1) / nDigits
      if deltaN > 0:
        # need to increase n until d lies somewhere in n's digits
        n += deltaN
        dTop += nDigits * deltaN ; dBot = dTop + 1 - nDigits
      
      _genChap = genDigits(n, base=base, leastFirst=False)
    while dBot < d:
      # loop through digits of n, excluding ones that aren't needed
      dBot += 1 ; next(_genChap)
    # yield requested digit
    dBot += 1 ;
    yield next(_genChap)


def euler40(base=10, digitList=[1, 10, 100, 1000, 10000, 100000, 1000000]):
  digitProd = prod(genChampernowneDigits(digitList, base=base))
  print("Product of digits %s in Champernowne's constant (base %d) = %d"
        % (str(digitList), base, digitProd))
  return digitProd


def _parseArguments():
  import argparse
  parser = argparse.ArgumentParser(description=
    "Compute the solution to Project Euler problem # 40",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--base", "-b", help="specify base", default=10, type=int)
  parser.add_argument("digitList", nargs="*", type=int,
                      default=[1, 10, 100, 1000, 10000, 100000, 1000000],
                      help="specify digits to check")
  return parser.parse_args()


if __name__ == "__main__":
  options = _parseArguments()
  euler40(base=options.base, digitList=options.digitList)
