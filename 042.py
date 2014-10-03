#!/usr/bin/python


from bisect import bisect_left


def genWords(fileName):
  with open(fileName, 'r') as fIn:
    while True:
      letter = fIn.read(1)
      while letter != '"':
        # should never happen, but just in case
        if not letter:
          break
        letter = fIn.read(1)
      word = fIn.read(1)
      letter = fIn.read(1)
      while letter != '"':
        word += letter
        letter = fIn.read(1)
      yield word
      # get comma
      letter = fIn.read(1)
      if not letter:
        # end of file
        break
    

_triangleNums = [1]
def isTriangleWord(word, triangleNums=_triangleNums):
  """
  return True if len(word) is a triangleNum (L == n * (n+1) / 2 for some n),
    False otherwise
  """
  wordLen = len(word)
  if wordLen > triangleNums[-1]:
    n = len(triangleNums) + 1
    t = (n * (n + 1)) / 2
    triangleNums.append(t)
    while wordLen > t:
      n += 1 
      t = (n * (n + 1)) / 2
      triangleNums.append(t)
    return wordLen == t
  
  return triangleNums[bisect_left(triangleNums, wordLen)] == wordLen


def euler42(fileName = 'data/euler042.txt'):
  numTriangleWords = sum(1 for word in genWords(fileName)
                         if isTriangleWord(word))
  print('%d words from %s are triangle words' % (numTriangleWords, fileName))
  return numTriangleWords


if __name__ == "__main__":
  euler42()
