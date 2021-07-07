#!/usr/bin/env python
# coding: UTF-8
#
## @package SimpleDate
#
#  Packages dates in the format yyyy-mm-dd.
#
#  @author Paulo Roma
#  @since 11/07/2017

import datetime, calendar, sys

##
 # Date consisting of a year, month, and day.
 #
class SimpleDate:
	## Number of millisecons in one day.
	#
	MILLIS_IN_24_HOURS = 1000 * 60 * 60 * 24

	##
	# Constructs a SimpleDate with the given year, month, and day.
	# @param year four-digit year
	# @param month 1-based month number
	# @param day 1-based day of month
	#
	def __init__(self, year, month, day):
		date = str(day) + '/' + str(month) + '/' + str(year)
		## Holds the date in this SimpleDate object.
		self.__date = datetime.datetime.strptime(date,'%d/%m/%Y').date()
  
	##
	# Returns a SimpleDate that is a given number of days
	# after an existing date.
	# @param existing the given SimpleDate
	# @param additionalDays the number of days to be added to the existing date
	#
	def SimpleDateFromDays(self, existing, additionalDays):
		date = datetime.datetime.strptime(str(existing),'%Y-%m-%d').date()
		date += datetime.timedelta(days=additionalDays)
		l = str(date).split("-")
		return SimpleDate(l[0], l[1], l[2])

	##
	# Determines whether this date is strictly earlier than the
	# given date.
	# @param other
	# @return true if this date is strictly before the given date.
	#   false otherwise
	#
	def isBefore(self, other):
		return self.daysUntil(other) > 0
  
	##
	# Returns the number of days from this date until the given date.
	# Returns a negative number if this date after the given date.
	# @param other the future date
	# @return number of days until the given date (negative if it is in the past)
	#
	def daysUntil(self, other):
		dt = other.__date - self.__date
		return dt.days
 
	## Prints this simpleDate in the format year-month-day. 
	#
	def __str__(self):
		tp = self.__date.timetuple()
		return "%4d-%02d-%02d" % ( tp.tm_year, tp.tm_mon, tp.tm_mday )


def main():
	date = SimpleDate(2017, 7, 12)
	date2 = date.SimpleDateFromDays(date,22)
	print (date)
	print (date2)
	print (date.daysUntil(date2))
	print (date.isBefore(date2))

	from datetime import datetime
	now = datetime.now()
	print (now.year, now.month, now.day)


if __name__=="__main__":
     sys.exit(main())
