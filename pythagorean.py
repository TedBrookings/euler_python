#!/usr/bin/python


def genPythagorean(maxRadius=float('inf'), maxB=None):
  n = 1
  nSqrd = 1
  if maxB is None:
    maxB = maxRadius
  maxNSqrd = maxB/2
  while nSqrd < maxNSqrd:
    m = n + 1
    mSqrd = m * m
    c = nSqrd + mSqrd
    b = 2 * m * n
    while c <= maxRadius and b <= maxB:
      a = mSqrd - nSqrd
      yield (a, b, c)
      m += 1
      mSqrd = m * m
      c = nSqrd + mSqrd
      b = 2 * m * n    
    n += 1
    nSqrd = n * n


def isPythagorean(a, b=None, c=None):
  if type(a) is tuple:
    return a[0]**2 + a[1]**2 == a[2]**2
  else:
    return a*a + b*b == c*c


if __name__ == "__main__":
  for triple in genPythagorean(maxRadius = 1000):
    if isPythagorean(triple):
      print('%d^2 + %d^2 == %d^2' % triple)
    else:
      print('Failed: %d^2 + %d^2 != %d^2' % triple)
