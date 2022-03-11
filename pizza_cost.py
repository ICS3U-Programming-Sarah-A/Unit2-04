#!/usr/bin/env python3
# Created by: Sarah
# Created on: Mar 10, 2022
# This program asks the user for the diameter of the
# pizza. It then calculates and displays the total cost
# of the pizza with tax
import constants


def main():
    # get user input, diameter
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # calculate subtotal, tax, and total cost
    subtotal = constants.LABOUR_COST + constants.RENTAL_COST + \
        constants.INGRED_COST * diameter
    tax = constants.HST * subtotal
    total = subtotal + tax

    # display results to user, total cost
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()

