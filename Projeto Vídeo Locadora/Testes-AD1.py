#!/usr/bin/env python
# coding: UTF-8
#
## @package AbstractItem
#
# Tests for AD1 CEDERJ 2017.2 PIG
#
#  @author Tamara Vitorino
#  @since 28/07/2017

import Item, sys, datetime, AbstractItem

# # Tests for the Class AbstractItem:
# from AbstractItem import AbstractItem
# print("Tests for the Class AbstractItem: \n")
# item1 = AbstractItem("To Kill A Mockingbird", "Drama", 1) #adding a new Item
# print(item1, "\n") # print the added item
# item1.setRented(datetime.datetime.today()) # rent the Item
# print(item1, "\n") #show the rented data
# print("Rental Cost: ", item1.getRentalCost(), "\n") #Shows the Item rental Cost
# item1.setRented(datetime.datetime.today()) # tries to rent the Item already rented
# print()
# item1.setReturned(datetime.datetime.today()) # return the Item
# print(item1, "\n")#the item is now available again

# Tests for the Class DVD:
from DVD import DVD
print("Tests for the Class DVD: \n")
# Adding a new Item and priting it
item2 = DVD("Back To The Future", "Science Fiction", 2)
print(item2, "\n") # print the added item

#Tries to return the Item when it's not rented
item2.setReturned(datetime.datetime.today()) # Tries to return the Item when it's not rented
print()

#Rent the Item, show the Item status and the rental cost
item2.setRented(datetime.datetime.today())
print(item2, "\n") #show the rented data
print("Rental Cost: ", item2.getRentalCost(), "\n")

#Tries to rent the Item already rented
item2.setRented(datetime.datetime.today())
print()

#Show the lateFees in different situations
print("LateFee:", item2.calculateLateFee(datetime.datetime.today()))
print("LateFee:", item2.calculateLateFee(datetime.datetime.today() + datetime.timedelta(days=7)),"\n")

#Return the Item
item2.setReturned(datetime.datetime.today())

#Shows the Item available again now
print(item2, "\n")
#
#
# # Tests for the Class NewReleaseDVD:
# from NewReleaseDVD import NewReleaseDVD
# print("Tests for the Class NewReleaseDVD: \n")
# item3 = NewReleaseDVD("Dunkirk", "Thriller", 3) #adding a new Item
# print(item3, "\n") # print the added item
# item3.setRented(datetime.datetime.today()) # rent the Item
# print(item3, "\n") #show the rented data
# print("Rental Cost: ", item3.getRentalCost(), "\n") #Shows the Item rental Cost
# item3.setRented(datetime.datetime.today()) # tries to rent the Item already rented
# print()
# item3.setReturned(datetime.datetime.today()) # return the Item
# print(item3, "\n")#the item is now available again
#
# # Tests for the Class Game:
# from Game import Game
# print("Tests for the Class Game: \n")
# item4 = Game("Resident Evil", 4) #adding a new Item
# print(item4, "\n") # print the added item
# item4.setRented(datetime.datetime.today()) # rent the Item
# print(item4, "\n") #show the rented data
# print("Rental Cost: ", item4.getRentalCost(), "\n") #Shows the Item rental Cost
# item4.setRented(datetime.datetime.today()) # tries to rent the Item already rented
# print()
# item4.setReturned(datetime.datetime.today()) # return the Item
# print(item4, "\n") #the item is now available again
#