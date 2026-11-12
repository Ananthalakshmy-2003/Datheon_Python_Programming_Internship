
from abc import ABC, abstractmethod


# Step 1: Abstract Base Class
class LibraryItem(ABC):

    def __init__(self, item_id, title, price):
        self.__item_id = item_id
        self.__title = title
        self.__price = price
        self.__is_borrowed = False
        self.__borrow_date = None

    # Encapsulation: Item ID
    @property
    def item_id(self):
        return self.__item_id

    # Encapsulation: Title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Title cannot be empty!")
        self.__title = value

    # Encapsulation: Price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero!")
        self.__price = value

    # Borrowing status
    @property
    def is_borrowed(self):
        return self.__is_borrowed

    @property
    def borrow_date(self):
        return self.__borrow_date

    def checkout(self, borrow_date):
        if self.__is_borrowed:
            raise ValueError("Item is already borrowed!")

        self.__is_borrowed = True
        self.__borrow_date = borrow_date

    def return_item(self):
        if not self.__is_borrowed:
            raise ValueError("Item is not currently borrowed!")

        self.__is_borrowed = False
        self.__borrow_date = None

    # Abstract methods
    @abstractmethod
    def calculate_fee(self, days):
        pass

    @abstractmethod
    def display_metadata(self):
        pass

    # Dunder methods
    def __str__(self):
        return f"{self.__title} (ID: {self.__item_id})"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.__item_id!r}, title={self.__title!r})"

    def __len__(self):
        return len(self.__title)

    def __eq__(self, other):
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self.__item_id == other.__item_id


# Step 2: Book Class
class Book(LibraryItem):

    def __init__(self, item_id, title, price, author):
        super().__init__(item_id, title, price)
        self.author = author

    def calculate_fee(self, days):
        return days * 5

    def display_metadata(self):
        return f"Book | Title: {self.title} | Author: {self.author} | Price: ₹{self.price}"


# Step 3: Magazine Class
class Magazine(LibraryItem):

    def __init__(self, item_id, title, price, issue_number):
        super().__init__(item_id, title, price)
        self.issue_number = issue_number

    def calculate_fee(self, days):
        return days * 3

    def display_metadata(self):
        return f"Magazine | Title: {self.title} | Issue: {self.issue_number} | Price: ₹{self.price}"


# Step 4: Digital Media Class
class DigitalMedia(LibraryItem):

    def __init__(self, item_id, title, price, file_format):
        super().__init__(item_id, title, price)
        self.file_format = file_format

    def calculate_fee(self, days):
        return days * 2

    def display_metadata(self):
        return f"Digital Media | Title: {self.title} | Format: {self.file_format} | Price: ₹{self.price}"
