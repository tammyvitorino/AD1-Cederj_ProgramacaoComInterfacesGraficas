#!/usr/bin/env python
# coding: UTF-8
#
## @package DVD
#
#  @author Tamara Vitorino
#  @since 23/08/2017

import AbstractItem, sys, datetime

class Game(AbstractItem.AbstractItem):
    ##
    #  Constructs a new Item with the given title, genre, and barcode.
    #  This constructor may only be invoked by subclasses.
    #  @param title the title of the item
    #  @param genre the genre of the item
    #  @param barcode a unique integer identifier for the item
    #
    def __init__(self, title, barcode):
        genre = "Game"
        z = 500
        super().__init__(title, genre, barcode, z)

    ##
    #  Rents this item if it is not already rented and sets the
    #  due date.
    #  @param today
    #    the date on which this item is being rented
    #    the loanDuration
    #  @throws Exception
    #    if the item cannot be rented
    #
    def setRented(self, today, x = 7):
        return super().setRented(today, x)

    ##
    # Return the bonuses and free when they aplly
    #
    def calculateLateFee(self, today):
        AbstractItem.AbstractItem.firstDay, AbstractItem.AbstractItem.otherDays  = 500, 500
        AbstractItem.AbstractItem.feeDays = 7
        return AbstractItem.AbstractItem.calculateLateFee(self, today)


# Tests
def main():
    item1 = Game("A Random Game", 1)
    print(item1)
    item1.setRented(datetime.datetime.today())
    print(item1)
    print("Late Fee: ", item1.calculateLateFee(datetime.datetime.today()))
    print("Rental Cost: ", item1.getRentalCost())

if __name__ == "__main__":
    sys.exit(main())
