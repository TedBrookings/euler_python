#!/usr/bin/python


import sys
if sys.version_info[0] == 2:
  # get rid of 2.x range that produced list instead of iterator
  range = xrange


def genTriangleLines(triangleFile):
  with open(triangleFile, 'r') as fIn:
    for line in fIn:
      yield [int(n) for n in line[:-1].split()]


def findTrianglePath(triangleFile, pathTypeStr='max'):
  pathType = eval(pathTypeStr)
  triangleLines = genTriangleLines(triangleFile)
  cost = next(triangleLines)
  for triangleLine in triangleLines:
    triangleLine[0] += cost[0]
    triangleLine[-1] += cost[-1]
    for n in range(1, len(cost)):
      triangleLine[n] += pathType(cost[n-1], cost[n])
    cost = triangleLine
  
  print('%simum path sum is %d' % (pathTypeStr.title(), pathType(cost)))
  

def euler18(triangleFile='data/euler018.txt', pathTypeStr='max'):
  findTrianglePath(triangleFile, pathTypeStr)
  
  
if __name__ == "__main__":
  args = tuple(eval(a) for a in sys.argv[1:])
  euler18(*args)
