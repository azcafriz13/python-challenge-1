# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = {}

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu which are keys). 
    #
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
        # Note that menu_items is now a dict with the 4 Menu Categories as Keys
    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected.
            # 
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            
            # 2. Ask customer to input menu item number
            #  v NEW CODE HERE v 
            menu_item = input("What is the item that you want to purchase? ")
            
            # 3. Check if the customer typed a number
            #    Convert the menu selection to an integer
            #                  v NEW CODE HERE v 
            if menu_item.isdigit():
                number = int(menu_item)    
                
                # 4. Check if the menu selection is in the menu items
                # See 2.3-08 Nested Dictionaries Solution    
                # Check if the user's input is a valid option
                #  v NEW CODE HERE v 
                if int(menu_item) in menu_items.keys():
                    # Store the item name as a variable
                    menu_selection_name = menu_items[int(menu_item)]
                    print(f"{menu_selection_name} is The Menu Selection Name for {menu_item}")

                    # Ask the customer for the quantity of the menu item
                    qty_menu_item = input(f"Type How Many of {menu_selection_name} Do You Want: ")

                    # Check if the quantity is a number, default to 1 if not
                    if qty_menu_item.isdigit():
                        number = int(qty_menu_item)
                    else: 
                        number = 1
                    print(f"You have Entered Qty '{number}' ")

                    
                    #  Loop for new dictionary: Could not figure out how to do this
                    # Add the item name, price, and quantity to the order list
                    for key in menu.keys():
                        print(f"{i}: {key}")
                        # Store the menu category associated with its menu item number
                        menu_items[i] = key
                        # Add 1 to the menu item number
                        i += 1
                
                    print(menu_items.keys())
                    # Initialize a order item counter
                    order_item_counter = 0
                    # Append the order list with a dictionary that includes the item name,
                    # price and qty ordered
                    # Do not know how to do this
                    order_item = menu_items[key][number]
                    print(f"{order_item}")
                    new_variable += variable
                    #my_dictionary['foo'] = new_variable
                        
                    print("\nUsing for key in order_list.keys():")
                    for key in order_list.keys():
                        print(key)
                            # Add 1 to the order_item_counter
                        order_item_counter += 1
            
                # Tell the customer they didn't select a menu option (?item?cf)
                else:
                    print(f"{menu_item} is not a menu item number.")
                    break

                # Tell the customer they didn't select a menu option (?item?cf)
            else:
                print(f"{menu_item} is not a menu item number.")
                break

                # Student Note: ^ End New Code ^ 
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        # New Code Here VVVV
        # 5. Check the customer's input
        match keep_ordering.lower():
            # Customer chose yes
            case 'y':
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break
            # Customer chose no
            case 'n':
                # Complete the order
                place_order = False
                # Since the customer decided to stop ordering, thank them for their order
                print("Thank you for your order.")
                # Exit the keep ordering question loop
                break
            # Customer typed an invalid input
            case _:
                # Tell the customer to try again
                print("I didn't understand your response. Please try again.")

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order.\n")
                # Exit the keep ordering question loop
                place_order = false

                # Tell the customer to try again

#End New Code
# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
# New Code Here -------------------------------------------------
# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
