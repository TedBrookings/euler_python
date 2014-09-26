#!/usr/bin/python


import scipy


def getGrid(fileName):
  grid = []
  with open(fileName, 'r') as fIn:
    for line in fIn:
      grid.append([int(n) for n in line.split()])
  return scipy.array(grid)
  

def genNegSlopeDiagonal(grid, numElements):
  numRows, numCols = grid.shape
  nEM1 = numElements - 1
  for row in range(numRows - nEM1):
    for col in range(numCols - nEM1):
      diag = grid[range(row, row + numElements),
                  range(col, col + numElements)]
      yield diag

def genPosSlopeDiagonal(grid, numElements):
  numRows, numCols = grid.shape
  nEM1 = numElements - 1
  for row in range(nEM1, numRows):
    for col in range(numCols - nEM1):
      diag = grid[range(row, row - numElements, -1),
                  range(col, col + numElements)]
      yield diag

def genHoriz(grid, numElements):
  numRows, numCols = grid.shape
  nEM1 = numElements - 1
  for row in range(numRows):
    for col in range(0, numCols - nEM1):
      horiz = grid[row, range(col, col + numElements)]
      yield horiz

def genVert(grid, numElements):
  numRows, numCols = grid.shape
  nEM1 = numElements - 1
  for row in range(numRows - nEM1):
    for col in range(numCols):
      vert = grid[range(row, row + numElements), col]
      yield vert

def genLine(grid, numElements):
  for seg in genNegSlopeDiagonal(grid, numElements):
    yield (scipy.prod(seg), seg, 'negative slope')
  for seg in genPosSlopeDiagonal(grid, numElements):
    yield (scipy.prod(seg), seg, 'positive slope')
  for seg in genHoriz(grid, numElements):
    yield (scipy.prod(seg), seg, 'horizontal')
  for seg in genVert(grid, numElements):
    yield (scipy.prod(seg), seg, 'vertical')
    

def euler11(gridFile='data/euler011.txt', numElements=4):
  grid = getGrid(gridFile)
  maxSeg = max(genLine(grid, numElements), key=lambda x: x[0])
  
  print('Greatest product is %d, From %s line with elements: %s'
        % (maxSeg[0], maxSeg[2], str(maxSeg[1])))
  

if __name__ == "__main__":
  euler11()
