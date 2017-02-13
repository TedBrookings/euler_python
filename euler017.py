#!/usr/bin/python


from number_words import intToWord      
import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def genNumLetters(maxInt):
  for n in range(1, maxInt+1):
    numLetters = sum(1 for d in intToWord(n, useAnd=True) if d not in {' ','-'})
    yield numLetters


def euler17(maxInt=1000):
  numLetters = sum(genNumLetters(maxInt))
  print('There are %d letters in the numbers from 1 to %d written out as words.'
        % (numLetters, maxInt))


if __name__ == "__main__":
  euler17()

