"""
searching_algorithms.py

This module implements searching algorithms required for the system.
"""

def linear_search(inventory, query, search_by="title"):
    """
    Performs a linear search on the inventory.

    Args:
        inventory (list): A list of Book objects.
        query (str): The search term (title or author).
        search_by (str): The attribute to search by ("title" or "author").

    Returns:
        list: A list of matching Book objects.
    """
    results = []
    query = query.lower()
    
    for book in inventory:
        if search_by == "title":
            if query in book.title.lower():
                results.append(book)
        elif search_by == "author":
            if query in book.author.lower():
                results.append(book)
                
    return results

def binary_search(inventory, target_isbn):
    """
    Performs a binary search on the sorted inventory to find a book by ISBN.
    
    Args:
        inventory (list): A list of Book objects, sorted by ISBN.
        target_isbn (str): The ISBN to search for.

    Returns:
        int: The index of the book if found, otherwise -1.
    """
    low = 0
    high = len(inventory) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_isbn = inventory[mid].isbn

        if mid_isbn == target_isbn:
            return mid
        elif mid_isbn < target_isbn:
            low = mid + 1
        else:
            high = mid - 1

    return -1
