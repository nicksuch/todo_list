# Upper-Polo To Do List App

# An Item object for each user entry to their todo list.

class ItemList:
    def __init__(self):
        self.userlist = []

    def add_item(self, item):
        # TODO: Check inputs

        self.userlist.append(item)
        

    def remove_item(self, item):
        # TODO: Check inputs
        
        self.userlist.remove(item)    

