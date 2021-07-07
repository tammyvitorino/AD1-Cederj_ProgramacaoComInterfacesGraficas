#!/usr/bin/env python
# coding: UTF-8
#
## @package AbstractItem
#
#  Partial implementation of the Item interface.
#
#  @author Paulo Roma
#  @since 11/07/2017

import Item, sys, datetime, math
from StatusException import StatusException

##
#  Partial implementation of the Item interface.
#
class AbstractItem(Item.Item):
    ##
    #  Constructs a new Item with the given title, genre, and barcode.
    #  This constructor may only be invoked by subclasses.
    #  @param title the title of the item
    #  @param genre the genre of the item
    #  @param barcode a unique integer identifier for the item
    #
    def __init__(self, title, genre, barcode, z = 300):
        ##  Title of this item.
        self.__title = title
        ##  Genre of this item.
        self.__genre = genre
        ##  Unique Barcode for this item.
        self.__barcode = barcode
        ##  Rental status of this item.
        self.__rented = False
        ##  Due date for this item.
        self.__dueDate = None
        ## The Rental cost for this item
        self.__rentalCost = z

    ##
    #  Rents this item if it is not already rented and sets the
    #  due date.
    #  @param today
    #    the date on which this item is being rented
    #  @throws Exception
    #    if the item cannot be rented
    #
    def setRented(self, today, x = 0):
        rented = self.__rented
        if rented == True:
            print ("Sorry! Item is already rented.")
        else:
            self.__rented = True
            self.__dueDate = today + datetime.timedelta(days=x)
        return None

    ##
    #  Returns this item, if it is currently rented.
    #  @param today
    #    the date on which the item is being returned
    #  @throws StatusException
    #    if the item is not currently rented
    #
    def setReturned(self, today):
        rented = self.__rented
        if rented == False:
            print("Sorry! Item isn't rented.")
            return None
        else:
            lateFee = self.calculateLateFee(today)
            self.__rented = False
            self.__dueDate = None
            return lateFee

    ##
    #  Returns the cost to rent this item.
    #  @return
    #    cost to rent the item
    #
    def getRentalCost(self):
         return self.__rentalCost

    ##
    # Calculate the bonuses and fees when they exists
    # @param today
    #    the due Date
    # @return
    #   the credits or debits by delivery date
    firstDay = 0
    otherDays = 0
    bonus = 0
    feeDays = 1
    def calculateLateFee(self, today):
        if self.__dueDate == None:
            return "Item isn't rented yet"
        else:
            lateFee = 0
            lateDays = math.ceil((((today - self.__dueDate).days)) / self.feeDays)
            if lateDays < 0:
                lateFee = self.bonus
            elif lateDays > 0:
                lateFee = ((lateDays - 1)* self.otherDays) + self.firstDay
            return lateFee


            ## Returns whether this item is rented.
    def isRented(self):
        return self.__rented

    ## Returns this item due date.
    def getDueDate(self):
        return str(self.__dueDate)[0:10]

    def getDateDue(self):
        return self.__dueDate

    ## Returns this item title.
    def getTitle(self):
        return self.__title

    ## Returns this item genre.
    def getGenre(self):
        return self.__genre

    ## Returns this item barcode.
    def getBarcode(self):
        return self.__barcode

    ##
    #  Returns a representation of the state of this object as a
    #  multiline string.  The format is:
    #  <pre>
    #    type
    #    title
    #    (genre)
    #    status
    #  </pre>
    #  The status is either
    #  <pre>
    #    Rented: yyyy-mm-dd
    #  </pre>
    #  or
    #  <pre>
    #    Available
    #  </pre>
    #  where "yyyy-mm-dd" is the current due date.
    #
    #  @return a string representation of this object
    #
    def __str__(self):
        s = type(self).__name__ + "\n"
        s += self.getTitle() + "\n"
        s += " (" + self.getGenre() + ")\n"
        if self.isRented():
            s += "Rented: " + self.getDueDate()
        else:
            s += "Available"
        return s

    ##
    #  Determines whether this item is the same as another
    #  one based on its barcode.
    #  @param obj
    #     the object to compare to this item
    #  @return
    #     true if the given object is an AbstractItem
    #     with the same barcode as this one
    #
    def __eq__(self, obj):
        if not isinstance(obj, AbstractItem):
            return false
        return self.getBarcode() == obj.getBarcode()

            ##
            # The total cost of the rent
            #
            ##


def main():
    item1 = AbstractItem("A Movie Name", "Action", 1)
    item2 = AbstractItem("Another Movie Name", "Action", 2)
    #item1.setReturned()
    print(item1 == item2)
    print(item1)
    print(item2)
    item1.setReturned(datetime.datetime.today())
    item1.setRented(datetime.datetime.today())
    print("Late Fee: ", item1.calculateLateFee(datetime.datetime.today()))
    print("Rental Cost: ", item1.getRentalCost())


if __name__ == "__main__":
    sys.exit(main())