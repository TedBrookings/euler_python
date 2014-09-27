#!/usr/bin/python


import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange
from math import sqrt


def isPythagorean(a, b, c):
  # return True if a^2 + b^2 == c^2, False otherwise
  return a*a + b*b == c*c


def genPythagorean(maxC=float('inf'), maxB=None, primitive=False):
  # generate all Pythagorean triples, such that c <= maxC, b <= maxB
  #   if primitive=True, then only generates triples with no common factors
  if maxB is None:
    maxB = maxC
  computeDerived = not primitive
  
  m, n = 2, 1
  # add primitive seed for (3,4,5)
  seeds = [(2,1)]
  while seeds:
    tup = seeds.pop(0)
    if len(tup) == 2:
      # this m,n tuple describes a primitive pythagorean triple
      m,n = tup
      # calculate pythagorean triple
      mSqrd, nSqrd = m*m, n*n
      c = mSqrd + nSqrd
      if c > maxC:
        continue
      b = 2*m*n
      if c > maxB:
        continue
      a = mSqrd-nSqrd
      if a > b:
        a, b = b, a
      # yield primitive pythagorean triple
      yield a,b,c
      # add three new primitive seeds
      seeds.append((2*m - n, m))
      seeds.append((2*m + n, m))
      seeds.append((m + 2*n, n))
      if computeDerived:
        # add a derived seed
        seeds.append((a,b,c, 2))
    else:
      # this a,b,c,k tuple describes a primitive pythagorean triple and
      # a multiplying factor
      a,b,c,k = tup
      # check to be sure the tuple isn't too big
      c_new = c * k
      if c_new > maxC:
        continue
      b_new = b * k
      if b_new > maxB:
        continue
      # yield derived pythagorean triple
      yield a*k, b_new, c_new
      # add next derived seed
      seeds.append((a,b,c, k+1))


def genPythagoreanSlow(maxC=float('inf'), maxB=None, primitive=False):
  # generates all Pythagorean triples. Slow, for testing purposes.
  from math import sqrt
  c = 2
  while c <= maxC:
    for a in range(1, int(c/sqrt(2.0)) + 1):
      b = int(round(sqrt(c*c - a*a)))
      
      if isPythagorean(a, b, c):
        yield a,b,c
    c += 1


def genPythagoreanWithPerimeter(perimeter, primitive=False):
  # generate all Pythagorean triples, such that c <= maxC, b <= maxB
  #   if primitive=True, then only generates triples with no common factors
  computeDerived = not primitive
  
  maxN = int(round(sqrt(perimeter / 4)))
  perimStop = perimeter / 2
  
  m, n = 2, 1
  # add primitive seed for (3,4,5)
  seeds = [(2,1)]
  while seeds:
    tup = seeds.pop(0)
    # this m,n tuple describes a primitive pythagorean triple
    m,n = tup
    mSqrd, nSqrd = m*m, n*n
    a, b, c = mSqrd-nSqrd, 2*m*n, mSqrd + nSqrd
    if a > b:
      a, b = b, a
    p = a + b + c
    
    if p >= perimeter:
      if p == perimeter:
        # found a match, yield it
        yield a, b, c
      # this tree is too big, will never have matching descendents
      continue
    
    if computeDerived:
      # Not a match, but maybe a multiplicative factor will match
      f, r = divmod(perimeter, p)
      if r == 0:
        # f * (a,b,c) is a match
        yield (f * a, f * b, f * c)
      
    # add three new primitive seeds
    if m <= maxN:
      seeds.append((2*m - n, m))
      seeds.append((2*m + n, m))
    seeds.append((m + 2*n, n))

  
def testAssert(booleanVal, message):
  # print Assertion message with line info on fail
  if not booleanVal:
    import os, sys
    from traceback import extract_stack
    callingTracebackStack = extract_stack()[1]
    callingFile = os.path.relpath(callingTracebackStack[0])
    callingLine = callingTracebackStack[1]
    print(' In %s line %d:' % (callingFile, callingLine))
    sys.tracebacklimit=0
    raise AssertionError(message)


def testPythagorean(maxC=1000):
  ### Test if genPythagorean, genPythagoreanSlow, and isPythagorean work by
  ###   comparing their results
  sys.stdout.write('Testing pythagorean.py...')
  # generate a list of Pythagorean triples with c < maxC, sorted by maximum
  # value of C
  generatedTrips = sorted(genPythagorean(maxC=maxC), key=lambda t:t[2]-1.0/t[1])
  for trip in generatedTrips:
    # assert each generated triple is valid
    testAssert( isPythagorean(*trip),
                'genPythagorean generated ' + str(trip) +
                ' which is not a pythagorean triplet'
              )
  testAssert( len(set(generatedTrips)) == len(generatedTrips),
              'genPythagorean generated duplicate triplets'
            )
  
  # now do it the slow way, to test if they're the same
  slowTrips = sorted(genPythagoreanSlow(maxC=maxC), key=lambda t:t[2]-1.0/t[1])
  testAssert( len(set(slowTrips)) == len(slowTrips),
              'genPythagoreanSlow generated duplicate triplets'
            )

  try:
    assert slowTrips == generatedTrips
  except AssertionError:
    for trip in slowTrips:
      # assert each generated triple is valid
      testAssert( isPythagorean(*trip),
                  'genPythagoreanSlow generated ' + str(trip) +
                  ' which is not a pythagorean triplet'
                )
      # assert each triple was generated already by the fast way
      #  (i.e. fast was was comprehensive)
      testAssert( trip in generatedTrips,
                  'genPythagorean failed to generate ' + str(trip) +
                  ' which is a pythagorean triplet'
                )
    for trip in generatedTrips:
      # assert each generated triple is valid
      testAssert( trip in slowTrips,
                  'genPythagoreanSlow failed to generate ' + str(trip) +
                  ' which is a pythagorean triplet'
                )
    raise

  # test fix perimeter generation
  for p in range(12, maxC):
    fixedTrips = sorted(genPythagoreanWithPerimeter(p),
                        key=lambda t:t[2]-1.0/t[1])
    testAssert( len(set(fixedTrips)) == len(fixedTrips),
               'genPythagoreanWithPerimeter generated duplicate triplets'
            )
    genTrips = sorted((t for t in generatedTrips if sum(t) == p),
                      key=lambda t:t[2]-1.0/t[1])
    try:
      assert fixedTrips == genTrips
    except AssertionError:
      for trip in fixedTrips:
        # assert each generated triple is valid
        testAssert( isPythagorean(*trip),
                    'genPythagoreanWithPerimeter generated ' + str(trip) +
                    ' which is not a pythagorean triplet'
                  )
      for trip in genTrips:
        # assert fixed-perimeter triple was comprehensive
        testAssert( trip in fixedTrips,
                    'genPythagoreanWithPerimeter failed to generate '
                    + str(trip) + ' with perimeter %d' % p
                  )
      raise
    
  print(' passed')


if __name__ == "__main__":
  args = tuple(eval(a) for a in sys.argv[1:])
  testPythagorean(*args)
