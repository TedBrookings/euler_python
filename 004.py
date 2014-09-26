#!/usr/bin/python


from digit_math import isPalindrome


def genPalindromeProducts(numProdDigits):
  for n1 in range(10**(numProdDigits-1), 10**numProdDigits):
    for n2 in range(n1, 10**numProdDigits):
      prodNs = n1 * n2
      if isPalindrome(prodNs):
        yield (prodNs, n1, n2)
  

def euler4(numProdDigits=3):
  import sys
  maxPalindrome = max(genPalindromeProducts(numProdDigits), key=lambda x: x[0])
  sys.stdout.write('Largest palindrome product of two %d-digit numbers is:'
                   % numProdDigits)
  print(' %d = %d * %d' % maxPalindrome)
  

if __name__ == "__main__":
  euler4()
