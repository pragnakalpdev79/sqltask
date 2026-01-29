import sys
import os

from dbcon import get_db_connection
from logerror import log_db_error

from upsert import upsert_product
from addsupplier import add_supplier
from purchaserecord import record_purchase
from report import generate_reports
from clean import cleanup_data
from validate import get_valid_input
from placeorder import place_order
from data import create_tables

#=================================================================================
# [2] USSER MENU FUNCTION
def user_menu():
    """
    Docstring for user_menu:-
    - The main program starts by calling this function
    - it has no aguments
    - it will print the menu for users
    - take their choice as a string
    - and then execute specific functions accordingly
    - the input validation functions are called first 
        get_valid_input function takes an input and validates it too,
        without breaking the program
        and then that value is passed 
        to actual function.
    
    Args : No arguments
    Returns : NO return statement in this function
    """
    while True:
        os.system('clear')
        print("\n" + "="*40)
        print("|  INVENTORY MANAGEMENT SYSTEM         |")
        print("="*40)
        print("1. Add/Update Product")
        print("2. Add Supplier")
        print("3. Record Inventory Purchase ")
        print("4. Place Customer Order  = Sell")
        print("5. Daily Order Summary")
        print("6. Supplier Purchase Summary")
        print("7. Cleanup Old Order Data")
        print("8. Exit")
        
        choice = input("\nSelect an option (1-8): ")
        
        if choice == '1':
            name = get_valid_input(">Product Name: ")
            price = get_valid_input(">Price: ", float)
            #stock = get_valid_input("Initial Stock (if new): ", int)
            upsert_product(name, price)
            
        elif choice == '2':
            name = get_valid_input(">Supplier Name: ")
            checkifmail = input(">Do you want to Enter Email for this supplier? \n\nSelect an option (y/n):  ").strip().lower()
            if checkifmail == "y":
                email = get_valid_input(">>Email: ")
            else: 
                email = None
            add_supplier(name, email)
            
        elif choice == '3':
            sup = get_valid_input(">Supplier Name: ")
            prod = get_valid_input(">Product Name: ")
            qty = get_valid_input(">Quantity: ", int)
            record_purchase(sup, prod, qty)
            
        elif choice == '4':
            prod = get_valid_input("Product Name: ")
            qty = get_valid_input("Quantity to Sell: ", int)
            place_order(prod, qty)
            
        elif choice == '5':
            generate_reports("daily")
            
        elif choice == '6':
            generate_reports("supplier")
            
        elif choice == '7':
            cleanup_data()
            
        elif choice == '8':
            print("Exiting system.")
            sys.exit(0)
        else:
            print("Invalid choice, try again.")
        
        input("\nPress Enter to continue...")

"""
MAIN PROGRAM STARTS BELOW :- 
"""
if __name__ == '__main__':
    create_tables()
    user_menu()