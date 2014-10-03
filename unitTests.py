#!/usr/bin/python


def testAssert(booleanVal, message):
  """
  print Assertion message with line info on fail
  """
  if not booleanVal:
    import os, sys
    from traceback import extract_stack
    callingTracebackStack = extract_stack()[-2]
    callingFile = os.path.relpath(callingTracebackStack[0])
    callingLine = callingTracebackStack[1]
    print(' In %s line %d:' % (callingFile, callingLine))
    sys.tracebacklimit=0
    raise AssertionError(message)


def testEuler():
  import pythagorean
  pythagorean.test()
  import digit_math
  digit_math.test()
  import fibonacci
  fibonacci.test()
  

if __name__ == "__main__":
  testEuler()
