#!/usr/bin/python


import scipy.misc


def euler15(numRows=20, numCols=20):
  numPaths = scipy.misc.comb(numRows + numCols, numRows, exact=True)
  print('In %dx%d grid, there are %d paths' % (numRows, numCols, numPaths))


if __name__ == "__main__":
  euler15()
