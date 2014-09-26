#!/usr/bin/python


def getCycleLength(n, d, base=10):
  numerators = []
  while n not in numerators:
    numerators.append(n)
    n = base * (n % d)
    if n == 0:
      return 0
  return len(numerators) - numerators.index(n)


def euler26(maxDenominator=1000, numerator=1, base=10):
  maxCycle=max(((d, getCycleLength(numerator, d))
               for d in range(1, maxDenominator)), key=lambda x: x[1])
  print('For d in [1,%d), the max cycle length of %d/d is: %d / %d = %d'
        % (maxDenominator, numerator, numerator, maxCycle[0], maxCycle[1]))


if __name__ == "__main__":
  euler26()
