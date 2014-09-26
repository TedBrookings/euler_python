#!/usr/bin/python


def intToWord(n, useAnd=True):
  # Convert integer to string with word name
  if n == 0:
    return 'zero'
  
  ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine']
  teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen']
  tens = ['aught', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
          'seventy', 'eighty', 'ninety']
  blocks = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
            'quintillion', 'sextillion', 'septillion', 'octillion',
            'nonillion', 'decillion']
  blockNum = 0
  word = ''
  needsNextAnd = True
  while n > 0:
    (n, block) = divmod(n, 1000)
    if not block:
      blockNum += 1
      continue
    h, t, o = (int(d) for d in '%03d' % block)
    
    if h >= 1:
      blockWord = ones[h] + ' hundred'
      if t > 0 or o > 0:
        if useAnd:
          blockWord += ' and '
        else:
          blockWord += ' '
    else:
      blockWord = ''
    if t > 1:
      blockWord += tens[t]
      if o > 0:
        blockWord += '-' + ones[o]
    elif t == 1:
      blockWord += teens[o]
    elif o > 0:
      blockWord += ones[o]
    
    if blockNum > 0:
      blockWord += ' ' + blocks[blockNum]
    blockNum += 1
    if word:
      if useAnd and needsNextAnd:
        word = blockWord + ' and ' + word
      else:
        word = blockWord + ' ' + word
    else:
      word = blockWord
    needsNextAnd = (h == 0)
  return word


def getRankName(n):
  # return string with ordinal number (e.g. getRankName(21) = '21st')
  block = n % 100
  t, o = (int(d) for d in '%02d' % block)
  if t != 1:
    if o == 1:
      suffix = 'st'
    elif o == 2:
      suffix = 'nd'
    elif o == 3:
      suffix = 'rd'
    else:
      suffix = 'th'
  else:
    suffix = 'th'
  return str(n) + suffix
  
