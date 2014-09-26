#!/usr/bin/python


def euler29(aMax=100, bMax=100):  
  distinctPowers = set(a**b for a in range(2, aMax + 1)
                            for b in range(2, bMax + 1))
  
  print('For a in [2,%d] and b in [2,%d] there are %d distinct power of a^b'
        % (aMax, bMax, len(distinctPowers)))


if __name__ == "__main__":
  euler29()
