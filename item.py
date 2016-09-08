# Upper-Polo To Do List App

import datetime

# An Item object for each user entry to their todo list.

class Item:
	def __init__(self, title, complete = False):
		self.title = title
		self.date = datetime.datetime.now()
		self.complete = complete