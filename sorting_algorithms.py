"""
sorting_algorithms.py

This module implements sorting algorithms required for the system.
"""

def insertion_sort(inventory):
    """
    Sorts the inventory list in-place by ISBN using Insertion Sort.
    This is used to maintain the Ordered Inventory.

    Args:
        inventory (list): A list of Book objects.
    """
    for i in range(1, len(inventory)):
        key_book = inventory[i]
        j = i - 1
        # Compare ISBNs (strings)
        while j >= 0 and key_book.isbn < inventory[j].isbn:
            inventory[j + 1] = inventory[j]
            j -= 1
        inventory[j + 1] = key_book

def merge_sort(inventory):
    """
    Sorts the inventory list by Value (COP) using Merge Sort.
    Returns a new sorted list, leaving the original list unchanged.

    Args:
        inventory (list): A list of Book objects.

    Returns:
        list: A new list of Book objects sorted by value_cop.
    """
    if len(inventory) <= 1:
        return inventory

    mid = len(inventory) // 2
    left_half = inventory[:mid]
    right_half = inventory[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return _merge(left_sorted, right_sorted)

def _merge(left, right):
    """
    Helper function to merge two sorted lists by book value.

    Args:
        left (list): Left sorted list.
        right (list): Right sorted list.

    Returns:
        list: Merged sorted list.
    """
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].value_cop <= right[j].value_cop:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list
