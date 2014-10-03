#!/usr/bin/python


from math import log, ceil
import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange
from unitTests import testAssert


def getDigit(num, n, base=10):
  """
  return nth least-significant digit of integer num (n=0 returns ones place)
  in specified base
  """
  return int(num / base**n) % base


def getNumDigits(num, base=10):
  """
  return the number of significant digits of integer num in specified base
  if num == 0, returns 0
  """
  if base == 2:
    return num.bit_length()
  else:
    # compute number of digits
    absNum = abs(num)
    nPutative = int(ceil(log(absNum+1, base)))
    # for large numbers, nPutative may err due to rounding error on log
    if absNum > 1000000000000000 and base**(nPutative-1) > absNum:
      nPutative -= 1
    return nPutative


def genDigits(num, base=10, leastFirst=True):
  """
  Generate all the significant digits of integer num in specified base.
  By default, return the least significant digits first
  """
  if num == 0:
    yield 0
  elif leastFirst:
    num, d = divmod(num, base)
    yield d
    while num > 0:
      num, d = divmod(num, base)
      yield d
  else:
    startPow = getNumDigits(num, base) - 1
    divTest = base**startPow
    d, num = divmod(num, divTest)
    if d > 0:
      yield d
    while divTest > 1:
      divTest /= base
      d, num = divmod(num, divTest)
      yield d


def isPalindrome(num, base=10):
  """
  return True if integer num is a palindrome in specified base, False otherwise
  """
  digits = list(genDigits(num, base))
  for n in range(len(digits) / 2):
    if digits[n] != digits[-1 - n]:
      return False
  return True


def genNDigitPalindrome(n, base=10):
  """
  Generate all n-digit palendromes in requested base, in sequential order
  """
  def _incrementPalinVec(palinVec, base):
    # Increment a list of digits that encodes a palindrome number
    n = 0
    palinVec[n] += 1
    while palinVec[n] == base:
      palinVec[n] = 0
      n += 1
      if n == len(palinVec):
        return False
      palinVec[n] += 1
    return True
  
  def _palinVecToEven(palinVec, base):
    # Convert list of digits to palindrome number with even number of digits
    num = palinVec[-1]
    mult = base
    for d in reversed(palinVec[:-1]):
      num += d * mult
      mult *= base
    for d in palinVec:
      num += d * mult
      mult *= base
    return num
  
  def _palinVecToOdd(palinVec, base):
    # Convert list of digits to palindrome number with odd number of digits
    num = palinVec[-1]
    mult = base
    for d in reversed(palinVec[:-1]):
      num += d * mult
      mult *= base
    for d in palinVec[1:]:
      num += d * mult
      mult *= base
    return num

  if n == 1:
    for n in range(base):
      yield n
  elif n % 2:
    # generate a palindrome with 2 * nHalf + 1 digits
    palinVec = [0] * (n / 2) + [1]
    yield _palinVecToOdd(palinVec, base)
    while _incrementPalinVec(palinVec, base):
      yield _palinVecToOdd(palinVec, base)
  else:
    # generate a palindrome with 2 * nHalf digits
    palinVec = [0] * (n / 2 - 1) + [1]
    yield _palinVecToEven(palinVec, base)
    while _incrementPalinVec(palinVec, base):
      yield _palinVecToEven(palinVec, base)


def genPalindromes(maxNumber=None, maxDigit=float('inf'), base=10):
  """
  Generate all palendromes in requested base, in sequential order
  """
  if maxNumber is None:
    n = 1
    while n <= maxDigit:
      for p in genNDigitPalindrome(n, base):
        yield p
      n = n + 1
  else:
    maxDigit = min(maxDigit, getNumDigits(maxNumber, base))
    n = 1
    while n <= maxDigit:
      for p in genNDigitPalindrome(n, base):
        if p > maxNumber:
          raise StopIteration()
        yield p
      n = n + 1


def digitSum(numbers, base=10):
  """
  Add an iterator or list of numbers represented as array of digits
  """
  if type(numbers) is list:
    s = numbers[0]
    for n in numbers[1:]:
      digitPlusEqual(s, n, base)
  else:
    s = next(numbers)
    for n in numbers:
      digitPlusEqual(s, n, base)
  return s


def digitPlusEqual(n1, n2, base=10):
  """
  n1 += n2 for numbers represented as array of digits
  """
  carry = 0
  while len(n2) > len(n1):
    n1.insert(0, 0)
  
  for d in range(1, 1 + len(n2)):
    n1[-d] += n2[-d] + carry
    if n1[-d] >= base:
      carry = n1[-d] / base
      n1[-d] = n1[-d] % base
    else:
      carry = 0
  
  for d in range(1 + len(n2), 1 + len(n1)):
    n1[-d] += carry
    if n1[-d] >= base:
      carry = n1[-d] / base
      n1[-d] = n1[-d] % base
    else:
      carry = 0
      break
  
  if carry > 0:
    n1.insert(0, carry)


def digitsToInt(digits, base=10):
  """
  Convert list of digits (in specified base) to an integer
  """
  # first get an iterator to digits
  if not hasattr(digits, 'next'):
    # digits is an iterator
    digits = iter(digits)
  # now loop through digits, updating num
  num = next(digits)
  for d in digits:
    num *= base
    num += d
  return num

  
def digitsToStr(digitNum, base=10):
  """
  Convert list of digits (in specified base) to a string suitable for printing
  """
  if base <= 10:
    return ''.join(chr(d + 48) for d in digitNum)
  elif base <= 36:
    def _char(d):
      if d < 10:
        return chr(d + 48)
      else:
        return chr(d + 55)
    return ''.join(_char(d) for d in digitNum)
  else:
    raise NotImplementedError("Can't covert digits to string for base > 36")


def intToStr(num, base=10):
  """
  Convert integer to a string suitable for printing, in specified base
  """
  if base==10:
    return str(num)
  else:
    return digitsToStr(genDigits(num, base=base, leastFirst=False), base=base)


def genUniqueDigits(base=10, exclude0=False,
                    leading0=False,
                    sortedDigits=False,
                    repeatDigits=True,
                    minNumDigits=1,
                    maxNumDigits=float('inf'),
                    maxDigit=None):
  """
  Generate a series of digits (represented as lists of integers) with requested
  properties. Options:
    base: interpret digits in this base, if maxDigit is unspecified, use all
          allowed digit values in 0, 1, 2, 3, ..., base-1
    exclude0: if True, don't generate digit lists with any zeros
    leading0: if True, allow digit lists with zero in most significant place
    sortedDigits: if True, generate digit lists sorted in reverse order
    repeatDigits: if False, don't generate lists with any repeated digits
    minNumDigits: don't generate any lists with fewer than this many digits
    maxNumDigits: don't generate any lists with more than this many digits
    maxDigit: if specified, don't generate lists that contain any digits
              greater than this value
  """
  if maxDigit is None:
    maxDigit = base - 1
  if exclude0:
    leading0 = False
  firstNum = int(exclude0)
  if not repeatDigits:
    maxNumDigits = min(maxNumDigits, maxDigit + 1 - firstNum)
  repeatOffset = 1 - int(repeatDigits)
  
  if minNumDigits <= 1:
    for d in range(firstNum, maxDigit + 1):
      yield [d]
    digits = [d]
  else:
    digits = [maxDigit] * (minNumDigits - 1)
  
  lastInd = len(digits) - 1
  while sortedDigits:
    # increment digits, keeping largest digits to lower indices
    j = lastInd ; i = j - 1
    while digits[j] >= digits[i] - repeatOffset:
      # current digit has reached its maximum
      if i <= 0:
        # current digit is second-most significant digit
        if digits[i] == maxDigit:
          # most significant digit is already at its max, add a digit or stop
          lastInd += 1
          if lastInd >= maxNumDigits:
            raise StopIteration()
          if repeatDigits:
            if leading0:
              digits = [0] * (1 + lastInd)
            else:
              digits = [1] + lastInd * [firstNum]
          else:
            digits = list(range(firstNum + lastInd, firstNum - 1, -1))
          j = None
        else:
          # increase most significant digit
          if repeatDigits:
            digits[j] = firstNum
          else:
            digits[j] = firstNum + lastInd - j
          j = 0
        break
      else:
        # change next more significant digit
        if repeatDigits:
          digits[j] = firstNum
        else:
          digits[j] = firstNum + lastInd - j
        j = i ; i -= 1
    if j is not None:
      # increment current digit
      digits[j] += 1
    # yield the correctly incremented digits
    yield digits[:]

  
  while repeatDigits:
    # increment digits, allowing digits to be disordered and repeated
    j = lastInd ; i = j - 1
    while digits[j] >= maxDigit:
      # current digit has reached its maximum
      if i <= 0:
        # current digit is second-most significant digit
        if digits[i] == maxDigit:
          # most significant digit is already at its max, add a digit or stop
          lastInd += 1
          if lastInd >= maxNumDigits:
            raise StopIteration()
          if leading0:
            digits = [firstNum] * (1 + lastInd)
          else:
            digits = [1] + lastInd * [firstNum]
          j = None
        else:
          # increase most significant digit
          digits[j] = firstNum
          j = 0
        break
      else:
        # change next more significant digit
        digits[j] = firstNum
        j = i ; i -= 1
    if j is not None:
      # increment current digit
      digits[j] += 1
    # yield the correctly incremented digits
    yield digits[:]

  
  okToYield = True
  while True:
    # increment digits, allowing digits to be disordered
    j = lastInd ; i = j - 1
    while digits[j] >= maxDigit:
      # current digit has reached its maximum
      if i <= 0:
        # current digit is second-most significant digit
        if digits[i] == maxDigit:
          # most significant digit is already at its max, add a digit or stop
          lastInd += 1
          if lastInd >= maxNumDigits:
            raise StopIteration()
          if exclude0:
            digits = list(range(1,lastInd+2))
          elif leading0:
            digits = list(range(lastInd+1))
          else:
            digits = [1] + [0] + list(range(2,lastInd+1))
          j = None
        else:
          # increase most significant digit
          digits[j] = firstNum + lastInd - j
          j = 0
        break
      else:
        # change next more significant digit
        digits[j] = firstNum + lastInd - j
        j = i ; i -= 1
    if j is not None:
      # increment current digit
      digits[j] += 1
      checkDigits = digits[0:j]
      while digits[j] in checkDigits:
        if digits[j] < maxDigit:
          digits[j] += 1
        else:
          digits[j:] = [maxDigit] * (lastInd + 1 - j)
          okToYield = False
          break
      if okToYield and j < lastInd:
        # form the rightmost digits
        allowDigits = sorted( list( set( n for n in range(firstNum, maxDigit+1)
                                       ).difference(digits[0:j+1])
                                  )
                            )
        digits[j+1:] = allowDigits[:lastInd - j]
    # increment digits, allowing digits to be disordered but NOT repeated
    if okToYield:
      yield digits[:]
    else:
      okToYield = True


def genDigitFuncSums(func, minNumDigits=2, base=10, display=False):
  """
  generate numbers n for whom:
    sum(func(d) for d in digits) == n,
  where digits is the list of digits (in specified base) that represent n
  """
  def _displayMatch(base, digits, sumVal):
    if base == 10:
      print('%s acting on %s sums to %d'% (func.__name__, str(digits), sumVal))
    else:
      print('%s acting on %s sums to %s (base %d)'
            % (func.__name__, str(digits), intToStr(sumVal, base=base), base))

  # there are two generators: this one is for when func(0) == 0
  def _genNoZeroDigitFuncSums(fVec, base, display):
    maxDigit = base - 1  
    for digits in genUniqueDigits(base=base, sortedDigits=True, exclude0=True,
                                  minNumDigits=minNumDigits):
      sumVal = sum(fVec[d] for d in digits)
      sumDigits = sorted((d for d in genDigits(sumVal, base=base) if d != 0),
                         reverse=True)
      if sumDigits == digits:
        if display:
          _displayMatch(base, digits, sumVal)
        yield sumVal
      if len(digits) > 1 and digits[-2] == maxDigit:
        # check if it's time to stop search
        digitsVal = digitsToInt(reversed(digits), base=base)
        if sumVal < digitsVal:
          # the number represented by the digits is so large, no sum will ever
          # match it
          raise StopIteration()
  
  # there are two generators: this one is for when func(0) != 0
  def _genWithZeroDigitFuncSums(fVec, base, display):  
    maxDigit = base - 1  
    for digits in genUniqueDigits(base=base, sortedDigits=True, leading0=False,
                                  minNumDigits=minNumDigits):
      sumVal = sum(fVec[d] for d in digits)
      sumDigits = sorted(genDigits(sumVal, base=base), reverse=True)
      if sumDigits == digits:
        if display:
          _displayMatch(base, digits, sumVal)
        yield sumVal
      if len(digits) > 1 and digits[-2] == maxDigit and digits[-1] > 0:
        # check if it's time to stop search
        digitsVal = digitsToInt(reversed(digits), base=base)
        if sumVal < digitsVal:
          # the number represented by the digits is so large, no sum will ever
          # match it
          raise StopIteration()
  
  # pre-compute the function of the digits
  fVec = [func(d) for d in range(base)]
  if fVec != sorted(fVec):
    # fVec must monotonically increase
    raise NotImplementedError(
      "Stopping criterion incompatible with non-monotonic functions")
  # depending on whether func(0) == 0, use correct generator
  if fVec[0] == 0:
    return _genNoZeroDigitFuncSums(fVec, base, display)
  else:
    return _genWithZeroDigitFuncSums(fVec, base, display)


def test_genDigits(largeBase):
  """
  Test genDigits, digitsToInt, getDigit, for 0, and for a very large number
  """
  # construct reversed digits, and corresponding integer
  digits = [d for d in range(1, largeBase)]
  p = 1 ; n = 0
  for d in digits:
    n += p * d
    p *= largeBase
  # test genDigits() normally (least significant first)
  gDigits = list(genDigits(n, base=largeBase))
  testAssert( gDigits == digits,
              "genDigits(base=%d) generated %s instead of %s"
              % (largeBase, str(gDigits), str(digits))
            )
  # test getDigit()
  for k, d in enumerate(digits):
    dG = getDigit(n, k, base=largeBase)
    testAssert( dG == d,
                "getDigit(%d, base=%d) returned %d instead of %d"
                % (n, largeBase, dG, d)
              )
  # test genDigits() with most significant digits first
  gDigits = list(genDigits(n, base=largeBase, leastFirst=False))
  digits.reverse()
  testAssert( gDigits == digits,
              "genDigits(base=%d) generated %s instead of %s"
              % (largeBase, str(gDigits), str(digits))
            )
  # test digitsToInt
  nDigits = digitsToInt(digits, base=largeBase)
  testAssert( nDigits == n,
              "digitsToInt(%s, base=%d) = %d instead of %d"
              % (str(digits), largeBase, nDigits, n)
            )
  
  # test genDigits() on 0
  digits = genDigits(0, base=largeBase)
  testAssert( genDigits(0, base=largeBase),
              "genDigits(0, base=%d) produced %s instead of [0]"
              % (largeBase, str(digits))
            )
  digits = genDigits(0, base=largeBase, leastFirst=False)
  testAssert( genDigits(0, base=largeBase),
              "genDigits(0, base=%d) produced %s instead of [0]"
              % (largeBase, str(digits))
            )
  # test getDigit() on 0
  dG = getDigit(0, 0, base=largeBase)
  testAssert( dG == 0,
              "getDigit(0, base=%d) returned %d instead of 0"
              % (largeBase, dG)
            )


def test_genUniqueDigits(base=10, maxBasePow=4):
  """
  Run fairly comprehensive test on genUniqueDigits(), digitsToInt(),
    digitsToStr(), and intToStr() in specified base
  Test involves incrementing digits from 0 to base**maxBasePow
  """
  maxNum = base**maxBasePow
  genDigitsAll = genUniqueDigits(base=base, exclude0=False, leading0=True,
                                 sortedDigits=False, repeatDigits=True,
                                 minNumDigits=1, maxNumDigits=float('inf'),
                                 maxDigit=None)
  genDigitsInt = genUniqueDigits(base=base, leading0=False)
  genDigitsSorted = genUniqueDigits(base=base, sortedDigits=True,
                                    leading0=False)
  genDigitsSortNoReps = genUniqueDigits(base=base, sortedDigits=True,
                                        leading0=False,repeatDigits=False)
  genThreePlus = genUniqueDigits(base=base, repeatDigits=False, leading0=True,
                                 minNumDigits=3, maxNumDigits=maxBasePow)
  
  genPal = genPalindromes(maxDigit=maxBasePow, base=base)
  
  for n in range(maxNum):
    # test genDigits() and digitsToInt()
    trueDigits = list(genDigits(n, base=base, leastFirst=False))
    nDigits = digitsToInt(trueDigits, base=base)
    testAssert( nDigits == n,
                "genDigits(%d, base=%d) = %s, and digitsToInt(%s) -> %d != %d"
                % (n, base, str(trueDigits), str(trueDigits), nDigits, n)
              )
    # test intToStr() and digitsToStr()
    nStr = intToStr(n, base=base)
    digitStr = digitsToStr(trueDigits, base=base)
    testAssert( nStr == digitStr,
                "intToStr(%d, base=%d) != digitsToStr(%s, base=%d)"
                % (n, base, str(trueDigits), base)
              )
    # test genUniqueDigits:
    #  -with no leading 0s (i.e. generate integer digits)
    digits = next(genDigitsInt)
    testAssert( trueDigits == digits,
                "genUniqueDigits(base=%d) generated %s instead of %s"
                % (base, str(digits), str(trueDigits))
              )
    #  -with leading 0s (i.e. generate all possible digit sequences in order)
    allDigits = next(genDigitsAll)
    if allDigits[0] == 0 and n > 0:
      testAssert( allDigits[1:] == digits[1:],
                  "allDigits(base=%d) generated %s instead of %s"
                  %  (base, str(allDigits), str([0] + digits[1:]))
                )
      for dummy in range(-1 + base**(len(allDigits)-1)):
        next(genDigitsAll)
      allDigits = next(genDigitsAll)
    testAssert( allDigits == digits,
                "allDigits(base=%d) generated %s instead of %s"
                % (base, str(allDigits), str(digits))
              )
    #  -with digits sorted into decreasing order
    isSorted = (digits == sorted(digits, reverse=True))
    noRepeats = (len(set(digits)) == len(digits))
    if isSorted:
      # digits are in sorted order, repeats allowed
      sDigits = next(genDigitsSorted)
      testAssert( sDigits == digits,
                  "sortedDigits(base=%d) generated %s instead of %s"
                  % (base, str(sDigits), str(digits))
                )
      if noRepeats:
        # digits are sorted, and no digit may repeat
        sNoRepDigits = next(genDigitsSortNoReps)
        testAssert( sNoRepDigits == digits,
                    "sortedNoRepeatDigits(base=%d) generated %s instead of %s"
                    % (base, str(sNoRepDigits), str(digits))
                  )
    #  -with minimum three digits and maximum maxBasePow digits, no repeats
    if getNumDigits(n, base=base) >= 3 and noRepeats:
      tpDigits = next(genThreePlus)
      if n > 0:
        while(tpDigits[0] == 0):
          tpDigits = next(genThreePlus)
      testAssert( tpDigits == digits,
                  "threePlusDigits(base=%d) generated %s instead of %s"
                  % (base, str(tpDigits), str(digits))
                )
    # test isPalindrome() and genPalendromes()
    if isPalindrome(n, base):
      pal = next(genPal)
      testAssert( pal == n,
                  "genPalendromes(base=%d) generated %s instead of %s"
                  % (base, intToStr(pal,base=base), nStr)
                )
  try:
    tpDigits = next(genThreePlus)
    raise AssertionError( "genUniqueDigits did not generate all threePlus,"
                          " still had not produced %s" % str(tpDigits) )
  except StopIteration:
    pass

  try:
    palStr = intToStr(next(genPal), base=base)
    raise AssertionError( "genPalendromes did not generate all palendromes,"
                          " still had not produced %s" % palStr )
  except StopIteration:
    pass
  
              
def test(genTests=[(2,6), (3,6), (4,6), (12,4)], largeBase=20):
  """
  Unit test for functions in digit_math.py
  genTests specifies list of bases and maxBasePows that will be passed to
    test_genDigits
  """
  sys.stdout.write('Testing digit_math.py... ')
  sys.stdout.flush()
  
  # test digitsToInt and genDigits for a very large number
  test_genDigits(largeBase)
  
  # test genUniqueDigits for each base/power combination
  for base, maxBasePow in genTests:
    test_genUniqueDigits(base=base, maxBasePow=maxBasePow)

  print('passed')


if __name__ == "__main__":
  test()
