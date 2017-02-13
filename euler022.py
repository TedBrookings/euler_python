#!/usr/bin/python


def getNames(nameFile):
  with open(nameFile, 'r') as fIn:
    names = [name[1:-1] for name in fIn.read().split(',')]
  names.sort()
  return names
  

def genNameScores(names):
  offset = ord('A') - 1
  n = 1
  for name in names:
    yield n * sum(ord(let) - offset for let in name)
  

def euler22(nameFile='data/euler022.txt'):
  names = getNames(nameFile)
  nameScoresSum = sum(genNameScores(names))
  print('The sum of the name scores is %d' % nameScoresSum)


if __name__ == "__main__":
  euler22()
