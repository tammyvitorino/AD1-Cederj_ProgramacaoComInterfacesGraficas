#!/usr/bin/env python
# coding: UTF-8
#
## @package Customer
#
#  A class describing a customer of the Video Store.
#
#  @author Paulo Roma
#  @since 11/07/2017

import sys, datetime
from StatusException import StatusException
from AbstractItem import AbstractItem
from DVD import DVD
from NewReleaseDVD import NewReleaseDVD
from Game import Game

##
#  A Customer is a client of a VideoStore who can rent
#  items. A client is identified by a unique name.
#  At any given time a Customer has a list of
#  items currently rented, and a balance representing
#  rental charges, late fees, or credits (where a negative
#  balance indicates a credit).  Balances are in cents.
#  Ordinary customers are not allowed to rent new
#  items if they have any items overdue.
#
class Customer:

    ##
    #  Constructs a Customer with the given name.  Initially
    #  there are no items rented and the balance is zero.
    #  @param name
    #    the new customer's name
    #
    def __init__(self, name):
        ## Items currently rented by this customer.
        self.__itemsOut = []
        ## Name of this customer.
        self.__name = name
        ## Balance currently owed by this customer.
        self.__balance = 0

    ##
    #  Rents an item and adds it to this customer's list of items.
    #  If the item can be rented, this method updates the item's
    #  status (including the due date) and then adds it to this customer's list of items.
    #  If the item cannot be rented to this customer, a StatusException is thrown.
    #  @param item
    #    the item to be rented
    #  @param today
    #    the date on which the item is being rented
    #  @throws StatusException
    #    if the item cannot be rented to this customer for any reason
    #
    def rentItem(self, item, today):
        if not self.canRent(today):
            raise StatusException("Customer already has overdue items")
        else:
            item.setRented(today)
            self.__balance += item.getRentalCost()
            self.__itemsOut.append(item)

    ##
    #  Returns an item that this customer currently has rented and updates
    #  the balance if a late fee or credit is due.  If the item can be
    #  successfully returned, this method updates the item's status and removes
    #  it from this customer's list of items.  If the customer does not have
    #  the item rented, a StatusException is thrown.
    #  @param barcode
    #    identifier for the item to be returned
    #  @param today
    #    the date on which the item is being returned
    #  @throws StatusException
    #    if this customer does not have the given item rented
    #
    today = datetime.datetime.now()
    def bringBackItem(self, barcode):
        for i in range(len(self.getItemsOut())):
            if barcode == self.getItemsOut()[i].getBarcode():
                self.__balance += self.getItemsOut()[i].setReturned(self.today)
                del self.__itemsOut[i]
            else:
                print("Customer doesn't have the Item.")

    ##
    #  Returns the balance for this customer.
    #  @return
    #    this customer's balance
    #
    def getBalance(self):
        return self.__balance

    def getItemsOut(self):
    	return self.__itemsOut
    ##
    #  Returns the name of this customer.
    #  @return
    #    this customer's name
    #
    def getName(self):
        return self.__name

    ##
    #  Makes a payment on this customer's balance.
    #  @param amount
    #    the amount to be paid, in cents
    #
    def makePayment(self, amount):
        self.__balance -= amount;

    ##
    #  Returns a string representation of this customer.  The format
    #  consists of multiple lines.  The first line is the patron's name.
    #  Subsequent lines are formed from the __str__() values of the
    #  items currently rented, separated by a newline.
    #  @return
    #    representation of this object as a multi-line string
    #
    def __str__(self):
        sb = self.__name + ":"
        for item in self.__itemsOut:
            sb += item
            sb += "\n"
        return sb

    ##
    #  Helper method determines whether this customer
    #  already has overdue items.
    #  @param today
    #    the current date
    #  @return
    #    true if the customer has no overdue items,
    #    false otherwise
    #
    def canRent(self,today):
        for item in self.__itemsOut:
            if item.getDueDate().isBefore(today):
                return False
        return True

def main():
    item = NewReleaseDVD("Matrix", "Science Fiction", 3)
    customer = Customer("John Doe")
    print (customer)
    if customer.canRent(datetime.datetime.now()):
        try:
            customer.rentItem(item, datetime.datetime.now())
        except:
            print("rentItem method not implemented yet. Sorry...")

#testes
    print(customer.getBalance())
    teste = (customer.getItemsOut())[0]
    print(teste)
    customer.bringBackItem(3)
    teste = (customer.getItemsOut())
    print(teste)
    print(customer.getBalance())

if __name__ == "__main__":
    sys.exit(main())
