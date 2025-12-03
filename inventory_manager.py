"""
inventory_manager.py

This module contains the InventoryManager class, which acts as the central controller
for the Library Management System. It coordinates data loading, sorting, searching,
and interactions with the shelf module.
"""

import csv
import json
import os
from models import Book, User
from data_structures import Stack, Queue
from sorting_algorithms import insertion_sort, merge_sort
from searching_algorithms import linear_search, binary_search

class InventoryManager:
    """
    Manages the library inventory, user history, and reservations.
    """
    def __init__(self):
        self.general_inventory = []  # Unsorted list (loading order)
        self.ordered_inventory = []  # Sorted by ISBN
        self.user_history = Stack()
        self.reservations = Queue()
        self.users = [] # List to store User objects
        
        # Ensure data directories exist
        os.makedirs('data', exist_ok=True)
        os.makedirs('reports', exist_ok=True)

    # --- User Management ---
    def add_user(self, user_id: str, name: str):
        """Adds a new user to the system."""
        if self.find_user(user_id):
            print(f"User with ID {user_id} already exists.")
            return False
        new_user = User(user_id, name)
        self.users.append(new_user)
        print(f"User added: {new_user}")
        return True

    def find_user(self, user_id: str):
        """Finds a user by ID."""
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def update_user(self, user_id: str, new_name: str):
        """Updates a user's name."""
        user = self.find_user(user_id)
        if user:
            user.name = new_name
            print(f"User updated: {user}")
            return True
        print(f"User with ID {user_id} not found.")
        return False

    def delete_user(self, user_id: str):
        """Deletes a user by ID."""
        user = self.find_user(user_id)
        if user:
            self.users.remove(user)
            print(f"User deleted: {user_id}")
            return True
        print(f"User with ID {user_id} not found.")
        return False

    def list_users(self):
        """Returns the list of all users."""
        return self.users

    # --- Inventory Management ---
    def load_inventory(self, filepath: str):
        """
        Loads books from a CSV or JSON file into inventories.
        """
        if not os.path.exists(filepath):
            print(f"Error: File {filepath} not found.")
            return

        ext = os.path.splitext(filepath)[1].lower()
        count = 0

        try:
            if ext == '.csv':
                with open(filepath, mode='r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        book = Book(
                            isbn=row['isbn'],
                            title=row['title'],
                            author=row['author'],
                            weight_kg=float(row['weight_kg']),
                            value_cop=float(row['value_cop'])
                        )
                        self.add_book(book)
                        count += 1
            elif ext == '.json':
                with open(filepath, mode='r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data:
                        book = Book(
                            isbn=item['isbn'],
                            title=item['title'],
                            author=item['author'],
                            weight_kg=float(item['weight_kg']),
                            value_cop=float(item['value_cop'])
                        )
                        self.add_book(book)
                        count += 1
            else:
                print("Unsupported file format.")
                return

            print(f"Processed {count} records from {filepath}")

        except Exception as e:
            print(f"Error loading inventory: {e}")

    def add_book(self, new_book: Book):
        """
        Adds a book to the inventory. If it exists, increments stock.
        """
        existing_book = self.find_book_by_isbn(new_book.isbn)
        if existing_book:
            existing_book.stock += 1
            print(f"Stock updated for {existing_book.title}: {existing_book.stock}")
            return existing_book
        else:
            # New book, stock is already 1 from constructor
            self.general_inventory.append(new_book)
            self.add_book_to_ordered(new_book)
            print(f"New book added: {new_book.title}")
            return new_book

    def add_book_to_ordered(self, book: Book):
        """
        Adds a book to the ordered inventory and maintains sort order using Insertion Sort.
        """
        self.ordered_inventory.append(book)
        insertion_sort(self.ordered_inventory)

    def find_book_by_isbn(self, isbn: str):
        """
        Finds a book in the ordered inventory using Binary Search.
        """
        index = binary_search(self.ordered_inventory, isbn)
        if index != -1:
            return self.ordered_inventory[index]
        return None

    def borrow_book(self, isbn: str):
        """
        Attempts to borrow a book. Decrements stock if available.
        """
        book = self.find_book_by_isbn(isbn)
        if not book:
            return False, "Book not found."
        
        if book.stock < 1:
            return False, "Book is out of stock."
            
        book.stock -= 1
        self.user_history.push(isbn)
        print(f"Book borrowed: {book.title}. New Stock: {book.stock}")
        return True, book

    def process_return(self, isbn: str):
        """
        Processes a book return. Checks for reservations.
        """
        index = binary_search(self.ordered_inventory, isbn)
        if index != -1:
            book = self.ordered_inventory[index]
            print(f"Book returned: {book.title}")
            
            # Check reservations
            if not self.reservations.is_empty():
                # In a real app we'd check if the reservation is for THIS book.
                # But the requirement says: "If so, assign the book to the first user in line."
                reservation = self.reservations.dequeue()
                print(f"Reserved book assigned to User ID: {reservation['user_id']}")
                # Stock doesn't increase because it goes to the reserver
            else:
                book.stock += 1
                print(f"Stock updated: {book.stock}")
        else:
            print("Book not found in inventory.")

    def generate_value_report(self, filepath: str):
        """
        Generates a report of books sorted by value using Merge Sort.
        """
        sorted_books = merge_sort(self.general_inventory)
        
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['ISBN', 'Title', 'Author', 'Weight(kg)', 'Value(COP)'])
                for book in sorted_books:
                    writer.writerow([book.isbn, book.title, book.author, book.weight_kg, book.value_cop])
            print(f"Report generated at {filepath}")
        except IOError as e:
            print(f"Error generating report: {e}")
