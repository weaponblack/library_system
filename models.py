"""
models.py

This module defines the core data models for the Library Management System.
"""

class Book:
    """
    Represents a book in the library inventory.
    """
    def __init__(self, isbn: str, title: str, author: str, weight_kg: float, value_cop: float):
        """
        Initialize a new Book instance.

        Args:
            isbn (str): The International Standard Book Number.
            title (str): The title of the book.
            author (str): The author of the book.
            weight_kg (float): The weight of the book in kilograms.
            value_cop (float): The value of the book in Colombian Pesos (COP).
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.weight_kg = weight_kg
        self.value_cop = value_cop
        self.stock = 1  # Default stock is 1 for simplicity based on requirements implying individual book tracking

    def __repr__(self):
        return f"Book(ISBN='{self.isbn}', Title='{self.title}', Author='{self.author}', Weight={self.weight_kg}kg, Value=${self.value_cop})"

    def to_dict(self):
        """Returns a dictionary representation of the book."""
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "weight_kg": self.weight_kg,
            "value_cop": self.value_cop
        }

class User:
    """
    Represents a library user.
    """
    def __init__(self, user_id: str, name: str):
        """
        Initialize a new User instance.

        Args:
            user_id (str): Unique identifier for the user.
            name (str): Full name of the user.
        """
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return f"User(ID='{self.user_id}', Name='{self.name}')"
