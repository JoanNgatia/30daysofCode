# Given a Book class and a Solution class, write a MyBook class that does
# the following:

# Inherits from Book
# Has a parameterized constructor taking these  parameters:
# string Title
# string Author
# int Price
# Implements the Book class' abstract display() method so it prints these lines
# Title, a space, and then the current instance's Title.
# Author , a space, and then the current instance's Author.
# Price , a space, and then the current instance's Price

from abc import ABCMeta, abstractmethod


class Book:
    __metaclass__ = ABCMeta

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print "Title: %s" % (self.title)
        print "Author: %s" % (self.author)
        print "Price: %s" % (self.price)
