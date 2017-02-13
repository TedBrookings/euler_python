#!/usr/bin/python


from permutation import genPermutation
from number_words import getRankName


def euler24(numPermute=10, permutationIndex=1000000):
  # generate a permutation and store in tuple
  # add 1 to permutationIndex because want the millionth, and index starts at
  # 0
  p = tuple(genPermutation(permutationIndex + 1, numElements=numPermute))
  print('The %s lexographical permutation is %s' %
        (getRankName(permutationIndex), str(p)))


if __name__ == "__main__":
  euler24()
