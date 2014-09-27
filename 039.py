#!/usr/bin/python


from pythagorean import genPythagoreanWithPerimeter, genPythagorean
import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def numTripletsWithPerimeter(perimeter):
  return sum(1 for triplet in genPythagoreanWithPerimeter(perimeter))

def euler39Old(maxPerimeter=1000):
  maxNum, maxP = max(
    ((numTripletsWithPerimeter(p), p) for p in range(12, maxPerimeter + 1)),
    key=lambda t:t[0]
  )
  print('For perimeter <= %d, the maximum number of pythagorean triplets '
        'occurs with p == %d (%d triplets)' % (maxPerimeter, maxP, maxNum))

def euler39(maxPerimeter=1000):
  sums =  [0 for p in range(1 + maxPerimeter)]
  for trip in genPythagorean(maxC=maxPerimeter):
    p = sum(trip)
    if p <= maxPerimeter:
      sums[p] += 1
  maxP, maxNum = max(((p, s) for p, s in enumerate(sums)), key=lambda t: t[1])
  print('For perimeter <= %d, the maximum number of pythagorean triplets '
        'occurs with p == %d (%d triplets)' % (maxPerimeter, maxP, maxNum))


if __name__ == "__main__":
  args = tuple(eval(a) for a in sys.argv[1:])
  euler39(*args)
  #euler39Old(*args)
