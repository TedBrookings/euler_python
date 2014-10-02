#!/usr/bin/python


import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def directlyComputeDiagonalSum(numLevels):
  diagonalSum = 1 # start with the middle as a given, call this level 0
  largestDiagonalNum = 1
  for level in range(1, numLevels):
    # loop over level 1, level 2, ... level (numLevels - 1)
    diagonalSum += 4 * largestDiagonalNum + 20 * level
    largestDiagonalNum += 8 * level
  return diagonalSum


def euler28(spiralWidth=1001, directlyCompute=False):
  numLevels = (spiralWidth + 1) / 2
  if directlyCompute:
    s = directlyComputeDiagonalSum(numLevels)
  else:
    # this sum is of quadratic elements, so there's a closed-form formula
    s = numLevels * (numLevels * (numLevels * 16 - 18) + 14) / 3 - 3
  
  print('Sum of the diagonal elements of %dx%d spiral is %d'
        % (spiralWidth, spiralWidth, s))
  

if __name__ == "__main__":
  euler28()
