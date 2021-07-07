#!/usr/bin/env python
# coding: UTF-8
#
## @package VideoStore
#
#  A video store that rents DVDs, and Games.
#
#  @author Paulo Roma
#  @since 11/07/2017

import sys
from Customer import Customer
from AbstractItem import AbstractItem

##
#
#  VideoStore consists of a list of items and a list of customers
#  who can rent items.
#
class VideoStore:
  
	##
	#  Constructs a VideoStore that initially has no items and no customers.
	#
	def __init__(self):
		## The items in this store.
		self.__items     = []
		## The list of customers of this store.
		self.__customers = []
  
	##
	#  Adds an item to this store's list of items, provided
	#  that there is not already an item with the same barcode.
	#  @param item 
	#    the item to be added
	#
	def addItem(self, item):
		if not item in self.__items:
			self.__items.append(item)
  
	##
	#  Adds a customer to this store's list of customers.
	#  @param customer the customer to be added
	#
	def addCustomer(self, customer):
		self.__customers.append(customer)
  
	##
	#  Returns the customer with the given name
	#  @param name 
	#    the name of the customer to search for
	#  @return 
	#    the customer 
	#
	def findUser(self, name):
		for p in self.__customers:
			if name == p.getName():
				return p
		return None
  
	##
	#  Search the store's collection of for items satisfying the
	#  given SearchCondition.
	#  @param condition 
	#    the SearchCondition
	#  @return 
	#    list of items satisfying the condition
	#
	def search(self, condition):
		results = []
		for item in self.__items:
			if condition.matches(item):
				results.append(item)
		return results   

	## 
	#  Returns the set of users and items in this store.
	#
	#  @return a string with all users and items.
	#
	def __str__(self):
		st = ""
		for item in self.__items:
			st += "%s: Genre = %s\n" % (item, item.getGenre())

		st += "\n"

		for cust in self.__customers:
			st += str(cust) + "\n"

		return st

def main():
	store = VideoStore()
	i1 = AbstractItem("Matrix", "Science Fiction", 3)
	i2 = AbstractItem("Ladyhawke", "Fantasy", 2)
	c1 = Customer("João")
	c2 = Customer("Maria")
	c3 = Customer("Pedro")
	store.addCustomer(c1)
	store.addCustomer(c2)
	store.addCustomer(c3)
	store.addItem(i1)
	store.addItem(i2)
	print (store.findUser("João"))
	print (store)

if __name__=="__main__":
     sys.exit(main())
