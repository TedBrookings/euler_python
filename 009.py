#!/usr/bin/python


from pythagorean import *
import sys


def euler9(pythagoreanSum=1000):
  triple = None
  for triple in genPythagorean(maxC=pythagoreanSum):
    if sum(triple) == pythagoreanSum:
      break
  
  if triple is None:
    print('Did not find a pythagorean triple that summed to %d'
          % pythagoreanSum)
  else:
    sys.stdout.write('%d^2 + %d^2 == %d^2' % triple)
    sys.stdout.write(' and %d + %d + %d' % triple)
    sys.stdout.write(' == %d\n' % pythagoreanSum)
    print('Product abc = %d' % (triple[0] * triple[1] * triple[2]))
  

if __name__ == "__main__":
  euler9()
