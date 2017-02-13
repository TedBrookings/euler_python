#!/usr/bin/python


from digit_math import isPalindrome
import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def genPalindromeProducts(numProdDigits, base=10):
  upperLimit = base**numProdDigits
  start = upperLimit / base
  for n1 in range(start, upperLimit):
    prodNs = n1 * n1
    if isPalindrome(prodNs, base):
      yield (prodNs, n1, n2)
    for n2 in range(n1 + 1, upperLimit):
      prodNs += n1
      if isPalindrome(prodNs, base):
        yield (prodNs, n1, n2)
  

def euler4(numProdDigits=3, base=10):
  maxPalindrome = max(genPalindromeProducts(numProdDigits, base=base),
                      key=lambda x: x[0])
  print('Largest palindrome product of two %d-digit numbers (base %d) is: '
        '%d = %d * %d' % ((numProdDigits, base) + maxPalindrome))
  

if __name__ == "__main__":
  euler4()
