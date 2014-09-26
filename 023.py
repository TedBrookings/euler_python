#!/usr/bin/python


from primes import getDivisors


def genAbundantNums(aMax):
  # generate all the abundant numbers <= aMax
  for a in range(12, aMax + 1):
    if sum(getDivisors(a, proper=True)) > a:
      yield a


def isSumOf(n, testSet, numElements=2):
  # return true if n is a sum of numElements from testSet
  if numElements == 2:
    return any( (n - checkElement in testSet) for checkElement in testSet)
  else:
    numCheck = numElements - 1
    return any( isSumOf(n - checkElement, testSet, numCheck)
                for checkElement in testSet )


def genNonSums(maxNumCheck, testSet, numElements=2):
  # generate numbers that aren't sums of two abundant numbers
  minCheckSum = min(testSet) * numElements
  for n in range(1, minCheckSum):
    yield n
  for n in range(minCheckSum, maxNumCheck + 1):
    if not isSumOf(n, testSet, numElements):
      yield n


def euler23(maxNumCheck=28123, numSum=2):
  # get all the abundant numbers that could be relevant for finding natural
  # numbers that can't be expressed as sum of numSum abundant numbers
  abundantNums = set(genAbundantNums(maxNumCheck - 12))
  
  # get the sum of all the numbers that aren't the sum of numSum abundantNums
  sumOfNonSums = sum(genNonSums(maxNumCheck, abundantNums, numSum))
  
  print('Sum of all numbers not expressable as sum of %d abundant numbers is %d'
        % (numSum, sumOfNonSums))


if __name__ == "__main__":
  euler23()
