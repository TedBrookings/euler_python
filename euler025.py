#!/usr/bin/python


from fibonacci import genFibonacci, firstFibonacciTermWithNDigits
from number_words import getRankName

def euler25(minDigits=1000, base=10, bruteForce=False):
  if bruteForce:
    minNum = base**(minDigits - 1)
    fibonacci = genFibonacci()
    n, f = 1, next(fibonacci)
    while f < minNum:
      n += 1 ; f = next(fibonacci)
  else:
    n = firstFibonacciTermWithNDigits(minDigits, base=base)
  print('%s term in Fibonacci sequence is the first with at least %d digits'
        % (getRankName(n), minDigits))


if __name__ == "__main__":
  import sys
  args = tuple(eval(a) for a in sys.argv[1:])
  euler25(*args)
