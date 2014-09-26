#!/usr/bin/python


import random
random.seed()


def genFactorial(nStop):
  # generate n! up for n < nStop
  f = 1
  yield f
  yield f
  for n in range(2, nStop):
    f *= n
    yield f


def getPermutationIndex(permutation, naturalOrder=None):
  # return the index to permuation's lexographic order
  # can pass in a vector giving the natural order of elements, or
  #   by default they are assumed to be in sort order
  if naturalOrder is None:
    permOrder = list(permutation[:])
    permOrder.sort()
  else:
    permOrder = naturalOrder[:]
  
  # count down: (numElements-1)!, (numElements-2), ..., 1!
  _factorial = reversed(list(genFactorial(len(permutation))))
  
  index = 0
  for pElem in permutation[:-1]:
    n_permOrder = permOrder.index(pElem)
    permOrder.remove(pElem)
    index += n_permOrder * next(_factorial)
    
  return index


def genPermutation(index, numElements=None, elements=None):
  # return the index^th lexographical permuation of elements
  if numElements is None:
    if elements is None:
      raise ValueError('Must specify numElements or elements')
    numElements = len(elements)
    permOrder = list(elements[:])
  elif elements is None:
    permOrder = list(range(numElements))
  else:
    if len(elements) != numElements:
      raise ValuError('len(elements) != numElements')
  
  # count down: (numElements-1)!, (numElements-2), ..., 1!
  _factorial = reversed(list(genFactorial(numElements)))
  
  try:
    for n in range(numElements):
      digIndex, index = divmod(index, next(_factorial))
      yield permOrder.pop(digIndex)
  except IndexError:
    raise ValueError('Index greater than number of %d-element permutations'
                     % numElements)


def genRandomPermutation(numElements=None, elements=None):
  # Choose a random permutation by choosing lexographical index randomly
  if numElements is None:
    if elements is None:
      raise ValueError('Must specify numElements or elements')
    numElements = len(elements)
    permOrder = list(elements[:])
  elif elements is None:
    permOrder = list(range(numElements))
  else:
    if len(elements) != numElements:
      raise ValuError('len(elements) != numElements')
  
  # count down: numElements!, (numElements-1)!, (numElements-2), ..., 1!
  _factorial = reversed(list(genFactorial(numElements + 1)))
  
  # choose a random index
  index = random.randint(0, next(_factorial) - 1)
  
  # generate the permutation from the index
  for n in range(numElements):
    digIndex, index = divmod(index, next(_factorial))
    yield permOrder.pop(digIndex)


def genRandomPermutationSlow(numElements=None, elements=None):
  # Choose a random permutation by sequentially choosing members of elements
  # Mainly here to have a method of randomly-generating permutations without
  # using lexographical index, thus testing lexographical index-based methods
  if numElements is None:
    if elements is None:
      raise ValueError('Must specify numElements or elements')
    numElements = len(elements)
    elementsRemaining = list(elements[:])
  elif elements is None:
    elementsRemaining = list(range(numElements))
  else:
    if len(elements) != numElements:
      raise ValuError('len(elements) != numElements')

  for n in range(numElements - 1):
    ind = random.randint(0, len(elementsRemaining) - 1)
    yield elementsRemaining.pop(ind)
  yield elementsRemaining.pop(0)


def testPermute(numPermute=9, permuationNum=4):
  p = tuple(genRandomPermutationSlow(numPermute))
  print('Randomly generated permutation p = %s' % str(p))
  index = getPermutationIndex(p)
  print('p has lexographical index %d' % index)
  pRegen = tuple(genPermutation(index, numPermute))
  print('Permutation generated from this index: %s' % str(pRegen))


if __name__ == "__main__":
  testPermute()
