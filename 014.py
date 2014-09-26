#!/usr/bin/python


#_collatzMap = {1 : 1}


def getCollatzChainLen(n, _collatzMap):
  #global _collatzMap
  
  chain = []
  while n not in _collatzMap:
    chain.append(n)
    if n % 2:
      # n is odd
      n = 3 * n + 1
    else:
      # n is even
      n /= 2
  
  chainLen = _collatzMap[n]
  for n in reversed(chain):
    chainLen += 1
    _collatzMap[n] = chainLen
  
  return chainLen


def genCollatzChains(nMax=1000000):
  _collatzMap = {1 : 1}
  for n in range(2, nMax):
    yield (getCollatzChainLen(n, _collatzMap), n)


def euler14(nMax=1000000):
  chain = max(genCollatzChains(nMax), key = lambda x: x[0])
  print('Longest Collatz sequence under %d: starts with %d, has length %d'
        % (nMax, chain[1], chain[0]))


if __name__ == "__main__":
  euler14()
