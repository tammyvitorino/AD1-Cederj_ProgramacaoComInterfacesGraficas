#!/usr/bin/env python
# coding: UTF-8
#
## @package Item
#
#  A class modeling an item of the Video Store.
#
#  @author Paulo Roma
#  @since 11/07/2017

from StatusException import StatusException

## This is an abstract class. All methods here must be implemented elsewhere.
#
#  An item represents a movie or game that can be rented
#  from a video store. Each item has a title, a genre,
#  and a unique integer identifier called a barcode.
#  An item can be rented or available, and if rented
#  it has a due date.
#
class Item(object):
	##
	#  Rents this item if it is not already rented and sets the
	#  due date.
	#  @param today 
	#    the date on which this item is being rented
	#  @throws StatusException
	#    if the item cannot be rented
	#
	def setRented(self, today):
		raise StatusException("setRented: Must be implemented")

	##
	#  Returns this item, if it is currently rented.
	#  @param today 
	#    the date on which the item is being returned
	#  @throws StatusException
	#    if the item is not currently rented
	#
	def setReturned(self,today): 
		raise StatusException("setReturned: Must be implemented")
  
	##
	#  Returns the cost to rent this item.
	#  @return
	#    cost to rent the item
	#
	def getRentalCost(self):
		pass

	##
	#  Calculates the late fee (or bonus) that would be charged (or
	#  applied) for returning the item on the given date.
	#  @param today 
	#    the date on which the item is being returned
	#  @return
	#    the late fee or bonus for returning the item on the given date,
	#    or zero if the item is not currently rented
	#
	def calculateLateFee(self,today):
		pass

	##
	#  Returns a String representing the genre of this item
	#  @return 
	#    genre of this item
	#
	def getGenre(self):
		return "Not implemented yet"

	##
	#  Determines whether this item is currently rented.
	#  @return 
	#    true if this item is rented, false otherwise
	#
	def isRented(self):
		pass

	##
	#  Returns the due date for this item if it is currently rented,
	#  or null if the item is not rented.
	#  @return 
	#    due date for this item
	#
	def getDueDate(self):
		pass

	##
	#  Returns the title of this item.
	#  @return 
	#    title of this item
	#
	def getTitle(self):
		pass

	##
	#  Returns the integer barcode for this item.
	#  @return 
	#    barcode of this item
	#
	def getBarcode(self):
		pass
