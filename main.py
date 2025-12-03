"""
main.py

This is the main entry point for the Library Management System.
It demonstrates all required functionalities including data loading,
sorting, searching, data structures (stack/queue), and problem-solving algorithms.
"""

import os
from inventory_manager import InventoryManager
from models import Book
from searching_algorithms import linear_search
from problem_solving import (
    brute_force_heavy_shelf, 
    backtracking_optimal_shelf, 
    recursive_total_value_by_author,
    tail_recursive_average_weight_by_author
)

def main():
    print("=== Library Management System Demo ===\n")
    
    # Initialize Manager
    manager = InventoryManager()
    
    # 1. Load Data
    print("--- 1. Loading Data ---")
    data_path = os.path.join('data', 'books.csv')
    manager.load_inventory(data_path)
    print(f"General Inventory Size: {len(manager.general_inventory)}")
    print(f"Ordered Inventory Size: {len(manager.ordered_inventory)}")
    print("")

    # 2. Sorting (Insertion Sort Demo)
    print("--- 2. Sorting (Insertion Sort) ---")
    print("Adding a new book with ISBN '978-0000000001' (should be first)...")
    new_book = Book("978-0000000001", "New Book", "New Author", 0.5, 50000)
    manager.add_book_to_ordered(new_book)
    print("First 3 books in Ordered Inventory:")
    for b in manager.ordered_inventory[:3]:
        print(f"  {b.isbn} - {b.title}")
    print("")

    # 3. Searching
    print("--- 3. Searching ---")
    # Linear Search
    print("Linear Search for 'Design':")
    results = linear_search(manager.general_inventory, "Design", "title")
    for b in results:
        print(f"  Found: {b.title} by {b.author}")
    
    # Binary Search
    print("\nBinary Search for ISBN '978-0262033848' (Intro to Algorithms):")
    book = manager.find_book_by_isbn("978-0262033848")
    if book:
        print(f"  Found: {book.title}")
    else:
        print("  Not found.")
    print("")

    # 4. Data Structures (Stack & Queue)
    print("--- 4. Data Structures ---")
    # Stack (Loan History)
    print("Simulating Loans (Stack)...")
    manager.user_history.push("978-0132350884")
    manager.user_history.push("978-0201616224")
    print(f"  Stack Top: {manager.user_history.peek()}")
    stack_path = os.path.join('data', 'history.json')
    manager.user_history.save_to_file(stack_path)
    
    # Queue (Reservations)
    print("\nSimulating Reservations (Queue)...")
    # Force stock to 0 for a book to allow reservation
    if book:
        book.stock = 0
        print(f"  Set stock of '{book.title}' to 0.")
        success = manager.reservations.enqueue("user_123", book.stock)
        if success:
            print("  Enqueued reservation for user_123.")
        
        queue_path = os.path.join('data', 'reservations.json')
        manager.reservations.save_to_file(queue_path)
        
        # Simulate Return to trigger Queue check
        print("\nSimulating Return of reserved book...")
        manager.process_return(book.isbn)
    print("")

    # 5. Reports (Merge Sort)
    print("--- 5. Reports (Merge Sort) ---")
    report_path = os.path.join('reports', 'inventory_by_value.csv')
    manager.generate_value_report(report_path)
    print("")

    # 6. Problem Solving (Shelf Module)
    print("--- 6. Shelf Module Algorithms ---")
    
    # Brute Force
    print("A. Brute Force (Combinations of 4 books > 8kg):")
    # We need enough heavy books. Our sample data has weights: 1.2, 0.8, 0.5, 2.5, 4.5, 3.0, 1.0, 1.5
    # 4.5+3.0+2.5+1.5 = 11.5 > 8.0. Should find matches.
    combos = brute_force_heavy_shelf(manager.general_inventory)
    for i, combo in enumerate(combos[:3]): # Print first 3
        w = sum(b.weight_kg for b in combo)
        titles = [b.title for b in combo]
        print(f"  Combo {i+1}: Weight={w:.1f}kg, Books={titles}")
    if not combos:
        print("  No combinations found.")

    # Backtracking
    print("\nB. Backtracking (Optimal Value, Max Weight 8kg):")
    # Using a subset for clearer output if list is huge, but 9 books is fine.
    val, best_books = backtracking_optimal_shelf(manager.general_inventory, 8.0)
    print(f"  Optimal Value: ${val}")
    print("  Books in Optimal Set:")
    for b in best_books:
        print(f"    - {b.title} (${b.value_cop}, {b.weight_kg}kg)")
    print("")

    # 7. Recursion
    print("--- 7. Recursion ---")
    target_author = "Robert C. Martin"
    print(f"Calculating total value for author '{target_author}' (Stack Recursion)...")
    total_val = recursive_total_value_by_author(manager.general_inventory, target_author)
    print(f"  Total Value: ${total_val}")

    print(f"\nCalculating average weight for author '{target_author}' (Tail Recursion)...")
    avg_weight = tail_recursive_average_weight_by_author(manager.general_inventory, target_author)
    print(f"  Average Weight: {avg_weight:.2f}kg")

    print("\n=== Demo Completed ===")

if __name__ == "__main__":
    main()
