#!/usr/bin/python


import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def euler31Slow(totalValue=200, coins=[1, 2, 5, 10, 20, 50, 100, 200]):
  # Keep list with set of ways to make each value. Each way is a tuple
  #  with an integer number of coins for each coin value
  # This method is slow but the logic is easy: the set ensures that no way
  #  is repeated
  
  # The only way to make 0 is with no coins
  waysToMake = [{tuple(0 for c in coins)}]
  
  # Loop over sum value of coins, starting at 1 and going up to totalValue
  for value in range(1, totalValue + 1):
    # Update waysToMake with the number of ways to make value:
    #   1. Loop over all the coins less than value:
    #       for n, c in enumerate(coins) if c <= value
    #   2. Loop over all the ways of making value - c:
    #       for way in waysToMake[value - c]
    #   3. add nth coin to way:
    #       way[0:n] + (way[n]+1,) + way[n+1:]
    #   4. store in a set, and append this to waysToMake
    waysToMake.append(set( way[0:n] + (way[n]+1,) + way[n+1:]
                         for n, c in enumerate(coins) if c <= value
                         for way in waysToMake[value - c]
                        )
                     )
  # Get number of ways to make the requested total value:
  numWaysToMakeTotal = len(waysToMake[totalValue])
  print('There are %d ways to make %d with coins of worth %s'
        % (numWaysToMakeTotal, totalValue, str(coins)))


def getNumWays(totalValue, coins):
  if len(coins) == 1:
    return totalValue % coins[0] == 0
  elif len(coins) == 2 and coins[0] == 1:
    return totalValue / coins[-1] + 1
  else:
    numDiv = totalValue / coins[-1] + 1
    return sum(getNumWays(totalValue - n * coins[-1], coins[:-1])
               for n in range(numDiv))


def euler31(totalValue=200, coins=[1, 2, 5, 10, 20, 50, 100, 200]):
  coins.sort()
  numWaysToMakeTotal = getNumWays(totalValue, coins)
  print('There are %d ways to make %d with coins of worth %s'
        % (numWaysToMakeTotal, totalValue, str(coins)))
    

def testAlgorithms(maxVal=100, numCoinsRange=[2, 9]):
  # Not necessary, but useful in case I want to improve the main euler31 algo.
  import random
  from random import randint
  random.seed()
  
  numCoins = randint(numCoinsRange[0], numCoinsRange[1])
  coins = []
  for n in range(numCoins):
    nRemain = numCoins - n
    maxC = maxVal / (n + 1)
    minC = numCoins - n
    if n > 0:
      maxC = min(maxC, min(coins) - 1)
    try:
      c = randint(minC, maxC)
    except:
      print(coins)
      print(minC, maxC)
      raise
    coins.append(c)
  maxCoin = maxVal / 2
  
  coins.sort()
  
  totalValue = randint(sum(coins[0:2]), maxVal)
  euler31Slow(totalValue, coins)
  euler31(totalValue, coins)


if __name__ == "__main__":
  euler31()
