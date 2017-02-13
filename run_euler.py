#!/usr/bin/python


import os
import time
import euler
import pkgutil


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


def runAllEuler(exeColor='boldYellow', scriptColor='white'):
  for importer, moduleName, ispackage in pkgutil.iter_modules(euler.__path__):
    if not moduleName.startswith('euler'):
      continue
    print(_colors[exeColor] + 'executing %s' % moduleName + _colors[scriptColor])
    funcName = 'euler' + str( int( moduleName[-3:]))
    module = importer.find_module(moduleName).load_module(moduleName)
    func = getattr( module, funcName )
    startTime = time.time()
    func()
    endTime = time.time()
    print( 'Completed in %.1f seconds' % (endTime - startTime) )
    print(_colors['endColor'])


if __name__ == "__main__":
  runAllEuler()
