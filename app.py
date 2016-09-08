# Upper-Polo To Do List App
from item import Item
from item_list import ItemList

def main():
    my_list = ItemList()
    print(ItemList) # TODO: Remove this print
    while True:
        # Display menu
        show_menu()
        
        # Get user input
        user_in = int(input())
        
        # Add item
        if user_in == 1:
            print("Add Item")
            my_item_title = input("Please enter To-Do item\n")
            my_item = Item(my_item_title)
            my_list.add_item(my_item)
            print("\n=> Added: " + my_item_title)
        
        # Remove item
        elif user_in == 2:
            print("  \nRemove Which Item?")
            show_list_items(my_list.userlist)
            item_to_remove = my_list.userlist[int(input()) - 1]
            my_list.remove_item(item_to_remove)
            print("\n=X= Removed: " + item_to_remove)

        # Show items in item_list
        elif user_in == 3:
            print("  \nYour List")
            show_list_items(my_list.userlist)

        # Mark item complete
        elif user_in == 4:
            print("  \nComplete?")
            show_list_items(my_list.userlist)
            my_list.userlist[int(input()) - 1].complete = True
            show_list_items(my_list.userlist)

        # Sort by date
        elif user_in == 5:
            print("  \nSort by Date added (Reverse Chron)")
            my_list.userlist.sort(key = lambda x: x.date, reverse = True)
            show_list_items(my_list.userlist)

        # Sort by complete
        elif user_in == 6:
            print("  \nSort by Complete")
            my_list.userlist.sort(key = lambda x: x.complete, reverse = True)
            show_list_items(my_list.userlist)

        # Exit program
        elif user_in == 0:
            exit(0)

        else:
            print("invalid menu option")

# Views

def show_list_items(my_list):
    index = 1
    for my_item in my_list:
        item_date = ''
        for attribute in ['year', 'month', 'day', 'hour', 'minute']:
            item_date = item_date + str(getattr(my_item.date,attribute)) + "-"
        print("  " + str(index) + ": " + my_item.title + ", " + item_date + ", " + str(my_item.complete))
        index += 1

def show_menu():
    MENU_ITEMS = (  "",
                    "1. Add Item",
                    "2. Remove Item",
                    "3. List Items",
                    "4. Mark Complete",
                    "5. Sort By Date",
                    "6. Sort By Completed",
                    "0. Exit" )
    for menu_item in MENU_ITEMS:
        print(menu_item)

main()