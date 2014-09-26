#!/usr/bin/python


import os
import time


_colors = {
  'endColor'   : '\033[0m',

  'black'      : '\033[0;30m',
  'red'        : '\033[0;31m',
  'green'      : '\033[0;32m',
  'yellow'     : '\033[0;33m',
  'blue'       : '\033[0;34m',
  'purple'     : '\033[0;35m',
  'cyan'       : '\033[0;36m',
  'lightGray'  : '\033[0;37m',

  'darkGray'   : '\033[1;30m',
  'boldRed'    : '\033[1;31m',
  'boldGreen'  : '\033[1;32m',
  'boldYellow' : '\033[1;33m',
  'boldBlue'   : '\033[1;34m',
  'boldPurple' : '\033[1;35m',
  'boldCyan'   : '\033[1;36m',
  'white'      : '\033[1;37m'
}


def isEulerFile(f):
  splitF = f.split('.')
  if len(splitF) == 2 and splitF[-1] == 'py':
    try:
      eulerNum = int(splitF[0])
      return True
    except ValueError as e:
      pass
  return False


def runAllEuler(eulerDir, exeColor='boldYellow', scriptColor='white'):
  dirList = os.listdir(eulerDir)
  dirList.sort()
  timeCmd = '/usr/bin/time -f "\tElapsedTime: %U"'
  for f in dirList:
    if isEulerFile(f):
      # execute the script
      print(_colors[exeColor] + 'executing %s' % f + _colors[scriptColor])
      os.system(timeCmd + ' ' + os.path.join(eulerDir, f))
      print(_colors['endColor'])
      




if __name__ == "__main__":
  eulerDir = os.path.dirname(os.path.realpath(__file__))
  runAllEuler(eulerDir)
