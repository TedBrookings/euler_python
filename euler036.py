#!/usr/bin/python


from digit_math import genPalindromes, isPalindrome
    

def euler36(maxNumber=10**6, baseBig=10, baseSmall=2):
  if baseBig < baseSmall:
    # same answer, but slightly faster this way
    baseBig, baseSmall = baseSmall, baseBig
  
  pSum = sum(p for p in genPalindromes(maxNumber=maxNumber, base=baseSmall)
             if isPalindrome(p, baseBig))
  print('Sum of palindromic (base %d and %d) numbers less than %d  is %d'
        % (baseBig, baseSmall, maxNumber, pSum))


if __name__ == "__main__":
  import sys
  args = tuple(eval(a) for a in sys.argv[1:])
  euler36(*args)
