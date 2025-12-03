"""
problem_solving.py

This module implements the Shelf Module algorithms (Brute Force, Backtracking)
and Recursion tasks.
"""

def brute_force_heavy_shelf(books):
    """
    Finds all combinations of 4 books whose total weight exceeds 8.0 kg.
    Uses a brute-force approach (nested loops).

    Args:
        books (list): A list of Book objects.

    Returns:
        list: A list of tuples, where each tuple contains 4 Book objects.
    """
    n = len(books)
    results = []
    
    # We need to pick 4 distinct books.
    # Using 4 nested loops to generate combinations.
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    combo = [books[i], books[j], books[k], books[l]]
                    total_weight = sum(b.weight_kg for b in combo)
                    
                    if total_weight > 8.0:
                        results.append(combo)
                        
    return results

def backtracking_optimal_shelf(books, max_weight=8.0):
    """
    Finds the combination of books that maximizes total value without exceeding max_weight.
    Prints exploration steps to the console.

    Args:
        books (list): A list of Book objects.
        max_weight (float): The maximum allowed weight.

    Returns:
        tuple: (best_value, best_combination_of_books)
    """
    best_value = 0.0
    best_combination = []

    def backtrack(index, current_books, current_weight, current_value):
        nonlocal best_value, best_combination

        # Base case: we've considered all books
        if index == len(books):
            if current_value > best_value:
                best_value = current_value
                best_combination = list(current_books)
            return

        book = books[index]

        # Option 1: Include the book (if weight allows)
        if current_weight + book.weight_kg <= max_weight:
            print(f"DECIDE: Include ISBN {book.isbn} (Weight: {book.weight_kg}, Value: {book.value_cop})")
            current_books.append(book)
            backtrack(index + 1, current_books, current_weight + book.weight_kg, current_value + book.value_cop)
            current_books.pop() # Backtrack
            print(f"BACKTRACK: Remove ISBN {book.isbn}")
        else:
             print(f"SKIP: ISBN {book.isbn} (Weight: {book.weight_kg} exceeds limit with current {current_weight})")

        # Option 2: Exclude the book
        # print(f"DECIDE: Exclude ISBN {book.isbn}") # Optional: can be too verbose
        backtrack(index + 1, current_books, current_weight, current_value)

    print("\n--- Starting Backtracking Exploration ---")
    backtrack(0, [], 0.0, 0.0)
    print("--- End Backtracking Exploration ---\n")
    
    return best_value, best_combination

# --- Recursion Functions ---

def recursive_total_value_by_author(books, author):
    """
    Calculates the total value of books by a specific author using stack recursion.

    Args:
        books (list): List of Book objects.
        author (str): Author name to filter by.

    Returns:
        float: Total value of books by the author.
    """
    if not books:
        return 0.0
    
    head, *tail = books
    value = head.value_cop if head.author.lower() == author.lower() else 0.0
    
    return value + recursive_total_value_by_author(tail, author)

def tail_recursive_average_weight_by_author(books, author, current_sum=0.0, count=0):
    """
    Calculates the average weight of books by a specific author using tail recursion style.
    Note: Python does not optimize tail recursion, but the structure is implemented as requested.

    Args:
        books (list): List of Book objects.
        author (str): Author name to filter by.
        current_sum (float): Accumulator for total weight.
        count (int): Accumulator for number of books found.

    Returns:
        float: Average weight.
    """
    if not books:
        return current_sum / count if count > 0 else 0.0
    
    head, *tail = books
    
    if head.author.lower() == author.lower():
        return tail_recursive_average_weight_by_author(tail, author, current_sum + head.weight_kg, count + 1)
    else:
        return tail_recursive_average_weight_by_author(tail, author, current_sum, count)
