# Library Management System

A comprehensive Library Management System featuring a modern GUI, custom data structures, and algorithmic demonstrations.

## Features

-   **User Management**: Register, update, and delete library users.
-   **Book Management**: Full CRUD operations for books, including stock tracking.
-   **Shelf Management**: Build custom shelves and run optimization algorithms (Brute Force, Backtracking).
-   **Loans**: Borrow and return books using a **Stack** data structure to track history.
-   **Reservations**: Reserve out-of-stock books using a **Queue** data structure to ensure fair waiting lists.
-   **Reports**: Generate value-based inventory reports using **Merge Sort**.
-   **Algorithms Demo**: Visualize recursion algorithms for statistical analysis.

## Project Structure

-   `gui.py`: **Main Entry Point**. The Graphical User Interface application.
-   `main.py`: CLI demonstration script (legacy/demo mode).
-   `inventory_manager.py`: Core backend logic and controller.
-   `models.py`: Data models (`Book`, `User`).
-   `data_structures.py`: Custom `Stack` and `Queue` implementations.
-   `sorting_algorithms.py`: `insertion_sort` and `merge_sort`.
-   `searching_algorithms.py`: `linear_search` and `binary_search`.
-   `problem_solving.py`: Optimization and recursion algorithms.
-   `data/`: Stores CSV/JSON data files.
-   `reports/`: Stores generated reports.

## How to Run

### 1. Graphical Interface (Recommended)
Run the full GUI application:

```bash
python gui.py
```

### 2. CLI Demo
Run the console-based algorithm demonstration:

```bash
python main.py
```

## Algorithm Analysis

### Sorting
-   **Insertion Sort**: Used in real-time to keep the `ordered_inventory` sorted by ISBN.
-   **Merge Sort**: Used to generate the "Inventory by Value" report efficiently ($O(n \log n)$).

### Searching
-   **Binary Search**: Used for fast ISBN lookups in the ordered inventory ($O(\log n)$).
-   **Linear Search**: Used for searching by Title or Author ($O(n)$).

### Data Structures
-   **Stack (LIFO)**: Manages User Loan History.
-   **Queue (FIFO)**: Manages Book Reservations.

### Problem Solving
-   **Brute Force**: Finds all combinations of books on a shelf heavier than a limit.
-   **Backtracking**: Finds the optimal set of books (max value) that fits within a weight limit (Knapsack problem).
-   **Recursion**: Calculates total value and average weight of books by a specific author.
