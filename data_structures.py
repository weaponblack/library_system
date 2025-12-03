"""
data_structures.py

This module implements custom Stack and Queue data structures required for the system.
Both structures support saving to and loading from files.
"""

import json
import os
from datetime import datetime

class Stack:
    """
    LIFO Stack implementation for storing user loan history.
    """
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, isbn: str, loan_date: str = None):
        """
        Push a loan record onto the stack.

        Args:
            isbn (str): The ISBN of the borrowed book.
            loan_date (str, optional): The date of the loan in ISO 8601 format. 
                                       Defaults to current timestamp if not provided.
        """
        if loan_date is None:
            loan_date = datetime.now().isoformat()
        
        record = {"isbn": isbn, "loan_date": loan_date}
        self.items.append(record)

    def pop(self):
        """
        Remove and return the most recent loan record.

        Returns:
            dict: The last added loan record, or None if stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """
        Return the most recent loan record without removing it.

        Returns:
            dict: The last added loan record, or None if stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def save_to_file(self, filepath: str):
        """
        Save the stack contents to a JSON file.

        Args:
            filepath (str): Relative path to the output file.
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.items, f, indent=4)
            print(f"Stack saved to {filepath}")
        except IOError as e:
            print(f"Error saving stack: {e}")

    def load_from_file(self, filepath: str):
        """
        Load stack contents from a JSON file.

        Args:
            filepath (str): Relative path to the input file.
        """
        if not os.path.exists(filepath):
            print(f"File {filepath} not found. Starting with empty stack.")
            return

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.items = json.load(f)
            print(f"Stack loaded from {filepath}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading stack: {e}")


class Queue:
    """
    FIFO Queue implementation for storing book reservations.
    """
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, user_id: str, book_stock: int):
        """
        Add a reservation to the queue. 
        Only allowed if book stock is 0.

        Args:
            user_id (str): The ID of the user making the reservation.
            book_stock (int): The current stock of the book.
        
        Returns:
            bool: True if enqueued successfully, False otherwise.
        """
        if book_stock > 0:
            print("Cannot reserve: Book is currently in stock.")
            return False
        
        record = {
            "user_id": user_id,
            "request_date": datetime.now().isoformat()
        }
        self.items.append(record)
        return True

    def dequeue(self):
        """
        Remove and return the oldest reservation.

        Returns:
            dict: The oldest reservation record, or None if queue is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        """
        Return the oldest reservation without removing it.

        Returns:
            dict: The oldest reservation record, or None if queue is empty.
        """
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def save_to_file(self, filepath: str):
        """
        Save the queue contents to a JSON file.

        Args:
            filepath (str): Relative path to the output file.
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.items, f, indent=4)
            print(f"Queue saved to {filepath}")
        except IOError as e:
            print(f"Error saving queue: {e}")

    def load_from_file(self, filepath: str):
        """
        Load queue contents from a JSON file.

        Args:
            filepath (str): Relative path to the input file.
        """
        if not os.path.exists(filepath):
            print(f"File {filepath} not found. Starting with empty queue.")
            return

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.items = json.load(f)
            print(f"Queue loaded from {filepath}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading queue: {e}")
