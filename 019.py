#!/usr/bin/python

from datetime import datetime


def incDate(year, month):
  if month == 12:
    year += 1
    month = 1
  else:
    month += 1
  return year, month


def euler19(startDate='1901-01-01', endDate='2000-12-01'):
  startYear, startMonth, startDay = (int(n) for n in startDate.split('-'))
  endYear, endMonth, endDay = (int(n) for n in endDate.split('-'))
  if startDay != 1:
    year, month = incDate(startYear, startMonth)
  else:
    year, month = startYear, startMonth
  
  numSundays = 0
  while year < endYear or (year == endYear and month <= endMonth):
    d = datetime(year, month, 1)
    numSundays += (d.weekday() == 6)
    year, month = incDate(year, month)
  print('Number of Sundays on first of month between %s and %s is %d'
        % (startDate, endDate, numSundays))

if __name__ == "__main__":
  euler19()
