# Library Management System

A modular Python project implementing a Library Management System with custom data structures, sorting/searching algorithms, and problem-solving modules.

## Project Structure

- `models.py`: Core `Book` and `User` classes.
- `data_structures.py`: Custom `Stack` (LIFO) and `Queue` (FIFO) implementations with file persistence.
- `sorting_algorithms.py`: `insertion_sort` and `merge_sort`.
- `searching_algorithms.py`: `linear_search` and `binary_search`.
- `problem_solving.py`: Brute force, backtracking, and recursion algorithms.
- `inventory_manager.py`: Central controller class.
- `main.py`: Demonstration script.
- `data/`: Contains input data (`books.csv`) and saved structures.
- `reports/`: Contains generated reports.

## How to Run

1.  Ensure you have Python 3.10+ installed.
2.  Navigate to the project root directory.
3.  Run the main script:

```bash
python main.py
```

## Expected Outputs

- **Console**: The script will print the status of data loading, results of sorting/searching, simulation of loans/reservations, and the output of the shelf algorithms (including backtracking steps).
- **Files**:
    - `data/history.json`: Saved stack of user loan history.
    - `data/reservations.json`: Saved queue of book reservations.
    - `reports/inventory_by_value.csv`: Inventory sorted by value (COP).

## Algorithm Analysis

### Sorting
- **Insertion Sort**: Used for maintaining the ordered inventory.
    - Time Complexity: O(n^2) worst case, O(n) best case (nearly sorted).
    - Space Complexity: O(1) (in-place).
    - Trade-off: Efficient for small or nearly sorted datasets, but inefficient for large unsorted lists.
- **Merge Sort**: Used for generating value reports.
    - Time Complexity: O(n log n) always.
    - Space Complexity: O(n) (requires auxiliary space).
    - Trade-off: Stable and consistent performance, but uses more memory.

### Searching
- **Linear Search**:
    - Time Complexity: O(n).
    - Trade-off: Simple, works on unsorted data, but slow for large datasets.
- **Binary Search**:
    - Time Complexity: O(log n).
    - Trade-off: Extremely fast, but requires the data to be sorted first.

### Problem Solving
- **Brute Force (Heavy Shelf)**:
    - Time Complexity: O(n^4) (4 nested loops).
    - Trade-off: Guarantees finding all combinations, but computationally expensive and unscalable.
- **Backtracking (Optimal Shelf)**:
    - Time Complexity: O(2^n) worst case (subset sum variation).
    - Trade-off: Can find the optimal solution and prune invalid paths, but still exponential in worst case.
