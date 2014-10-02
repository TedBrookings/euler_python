#!/usr/bin/python


from pythagorean import genPythagoreanWithPerimeter


def euler39(maxPerimeter=1000):
  sums = [0] * (1 + maxPerimeter)
  for trip in genPythagoreanWithPerimeter(maxPerimeter=maxPerimeter):
    perimeter = trip[-1]
    sums[perimeter] += 1
  maxP, maxNum = max(((p, s) for p, s in enumerate(sums)), key=lambda t: t[1])
  print('For perimeter <= %d, the maximum number of pythagorean triplets '
        'occurs with p == %d (%d triplets)' % (maxPerimeter, maxP, maxNum))


if __name__ == "__main__":
  import sys
  args = tuple(eval(a) for a in sys.argv[1:])
  euler39(*args)
