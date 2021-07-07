#!/usr/bin/env python
# coding: UTF-8
#
## @package Club Member Customer
#
#  A class describing a customer of the Video Store.
#
#  @author Tamara Vitorino
#  @since 26/08/2017

import Customer, sys, datetime
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
class ClubMember(Customer.Customer):

    ##
    #  Constructs a Customer with the given name.  Initially
    #  there are no items rented and the balance is zero.
    #  @param name
    #    the new customer's name
    #
    def __init__(self, name):
        super().__init__(name)

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
    def bringBackItem(self, barcode):
        Customer.Customer.today = today = datetime.datetime.now() + datetime.timedelta(days=-1)
        super().bringBackItem(barcode)

    ##
    #  Helper method determines whether this customer
    #  already has overdue items.
    #  @param today
    #    the current date
    #  @return
    #    always true
    #
    def canRent(self,today):
        return True


def main():
    item = NewReleaseDVD("Matrix", "Science Fiction", 3)
    customer = ClubMember("John Doe")
    print (customer)
    if customer.canRent(datetime.datetime.now()):
        try:
            customer.rentItem(item, datetime.datetime.now() + datetime.timedelta(days=-4))
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
