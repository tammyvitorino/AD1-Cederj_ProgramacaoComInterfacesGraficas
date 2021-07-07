#!/usr/bin/env python
# coding: UTF-8
#
## @package Premier Member Customer
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
class PremierMember(Customer.Customer):

    ##
    #  Constructs a Customer with the given name.  Initially
    #  there are no items rented and the balance is zero.
    #  @param name
    #    the new customer's name
    #
    def __init__(self, name):
        super().__init__(name)

    def rentItem(self, item, today):
        super().rentItem(item,today)

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
    item = DVD("Matrix", "Science Fiction", 3)
    customer = PremierMember("John Doe")
    print (customer)
    if customer.canRent(datetime.datetime.now()):
        try:
            customer.rentItem(item, "")
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
