#!/usr/bin/python


from math import log, ceil


def getDigit(num, n, base=10):
  # return nth-digit of num
  return int(num / base**(n-1)) % base


def getNumDigits(num, base=10):
  # return the number of significant digits of num
  return int(ceil(log(num+1, base)))


def genDigits(num, base=10, leastFirst=True):
  # return a generator to get all the significant digits of num
  # by default, return the least significant digits first
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
  # return true if num is a palindrome, false otherwise
  digits = list(genDigits(num, base))
  for n in range(len(digits) / 2):
    if digits[n] != digits[-1 - n]:
      return False
  return True


def genNDigitPalindrome(n, base=10):
  # return generator for all n-digit palindromes
  
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

  if n % 2:
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
  # add an iterator or list of numbers represented as array of digits
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
  # n1 += n2 for numbers represented as array of digits
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
  # convert array of digits to an integer
  
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
  # convert array digits to a string suitable for printing
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


def genUniqueDigitNums(base=10, exclude0=False,
                       sortedDigits=False,
                       singleDigits=True,
                       repeatDigits=True,
                       maxNumDigits=float('inf'),
                       maxDigit=None):
  if maxDigit is None:
    maxDigit = base - 1
  
  firstNum = int(exclude0)
  if singleDigits:
    for d in range(firstNum, maxDigit + 1):
      yield [d]
  
  if not repeatDigits:
    maxNumDigits = min(maxNumDigits, maxDigit + 1 - firstNum)
  
  repeatOffset = 1 - int(repeatDigits)
  digits = [firstNum + repeatOffset, firstNum]
  lastInd = 1
  
  while sortedDigits:
    # increment digits, keeping largest digits to lower indices
    yield digits[:]
      
    j = lastInd ; i = j - 1
    while digits[j] == digits[i] - repeatOffset:
      # current digit has reached its maximum
      if i == 0:
        # current digit is second-most significant digit
        if digits[i] == maxDigit:
          # most significant digit is already at its max, add a digit or stop
          lastInd += 1
          if lastInd >= maxNumDigits:
            raise StopIteration()
          if repeatDigits:
            digits = lastInd * [1] + [firstNum]
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
  
  while repeatDigits:
    # increment digits, allowing digits to be disordered and repeated
    yield digits[:]
    
    j = lastInd ; i = j - 1
    while digits[j] == maxDigit:
      # current digit has reached its maximum
      if i == 0:
        # current digit is second-most significant digit
        if digits[i] == maxDigit:
          # most significant digit is already at its max, add a digit or stop
          lastInd += 1
          if lastInd >= maxNumDigits:
            raise StopIteration()
          digits = lastInd * [1] + [firstNum]
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
  
  okToYield = True
  while True:
    # increment digits, allowing digits to be disordered but NOT repeated
    if okToYield:
      yield digits[:]
    else:
      okToYield = True
      
    # increment digits, allowing digits to be disordered
    j = lastInd ; i = j - 1
    while digits[j] == maxDigit:
      # current digit has reached its maximum
      if i == 0:
        # current digit is second-most significant digit
        if digits[i] == maxDigit:
          # most significant digit is already at its max, add a digit or stop
          lastInd += 1
          if lastInd >= maxNumDigits:
            raise StopIteration()
          if exclude0:
            digits = list(range(1,lastInd+2))
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


def genDigitFuncSums(func, base=10, display=False):
  # there are two generators: this one is for when func(0) == 0
  def _genNoZeroDigitFuncSums(fVec, base, display):  
    for digit in range(1, base):
      sumVal = fVec[digit]
      sumDigits = list(genDigits(sumVal, base))
      if len(sumDigits) > 1:
        sumDigits = sorted((d for d in sumDigits if d != 0), reverse=True)
        if sumDigits == [digit]:
          if display:
            print('%s sums to %d' % (str([digit]), sumVal))
          yield sumVal
    
    digits = [1, 1]
    maxDigit = base - 1
    lastInd = 1
    while True:
      # compute sum of the func of the digits
      sumVal = sum(fVec[d] for d in digits)
      # sort them, and throw out any zeros
      sumDigits = sorted((d for d in genDigits(sumVal, base) if d != 0),
                         reverse=True)
      if sumDigits == digits:
        # the sum of the function of the digits matches the digits
        if display:
          print('%s sums to %d' % (str(digits), sumVal))
        yield sumVal
      if digits[-2] == maxDigit:
        # check if it's time to stop looking
        digitsVal = digitsToInt(reversed(digits), base=base)
        if sumVal < digitsVal:
          # the number represented by the digits is so large no sum will ever
          # match it
          raise StopIteration()
      
      # increment digits, keeping largest digits to lower indices and never
      # using the digit 0
      j = lastInd
      i = j - 1
      while digits[i] == digits[j]:
        if i == 0:
          if digits[i] == maxDigit:
            lastInd += 1
            digits = lastInd * [1] + [0]
            j = lastInd
          else:
            digits[j] = 1
            j = 0
          break
        else:
          digits[j] = 1
          j = i
          i -= 1
      digits[j] += 1
  # there are two generators: this one is for when func(0) != 0
  def _genWithZeroDigitFuncSums(fVec, base, display):  
    digits = [1, 0]
    maxDigit = base - 1
    lastInd = 1
    while True:
      # compute sum of the func of the digits
      sumVal = sum(fVec[d] for d in digits)
      if sorted(genDigits(sumVal, base), reverse=True) == digits:
        # the sum of the function of the digits matches the digits
        if display:
          print('%s sums to %d' % (str(digits), sumVal))
        yield sumVal
      if digits[-2] == maxDigit and digits[-1] > 0:
        # check if it's time to stop looking
        digitsVal = digitsToInt(reversed(digits), base=base)
        if sumVal < digitsVal:
          # the number represented by the digits is so large no sum will ever
          # match it
          raise StopIteration()
      
      # increment digits, keeping largest digits to lower indices
      j = lastInd
      i = j - 1
      while digits[i] == digits[j]:
        if i == 0:
          if digits[i] == maxDigit:
            lastInd += 1
            digits = [1] + lastInd * [0]
            j = None
          else:
            digits[j] = 0
            j = 0
          break
        else:
          digits[j] = 0
          j = i
          i -= 1
      if j is not None:
        digits[j] += 1
  
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


if __name__ == "__main__":
  def _testPalindrome(num, base=10):
    import sys
    digits = reversed([d for d in genDigits(num, base)])
    sys.stdout.write('digits of %d are:' % num)
    for d in digits:
      sys.stdout.write(' %d' % d)
    sys.stdout.write(' --> ')
    if isPalindrome(num, base):
      print('%d is a palindrome' % num)
    else:
      print('%d is not a palindrome' % num)

  import random
  random.seed()
  numDigits = random.randint(4, 7)
  pVec = [p for p in genNDigitPalindrome(numDigits)]
  randomP = random.choice(pVec)
  randomNum = random.randint(10**(numDigits-1), 10**numDigits - 1)
  _testPalindrome(randomNum)
  _testPalindrome(randomP)
