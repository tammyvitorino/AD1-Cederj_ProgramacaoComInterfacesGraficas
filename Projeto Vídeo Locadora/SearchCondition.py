#!/usr/bin/env python
# coding: UTF-8
#
## @package SearchCondition
#
#  A search predicate for items.
#
#  @author Paulo Roma
#  @since 11/07/2017

##
# Abstraction of a search predicate for items. Subtypes
# can customize the nature of the search (e.g., exact title, 
# title keywords, genre, etc.).
#
class SearchCondition:
	##
	# Determine whether the given item matches this 
	# search condition's criteria for inclusion.
	# @param item the item to be checked
	# @return true if the item matches this condition's
	#   criteria, false otherwise
	#
	def matches(self, item):
		pass
