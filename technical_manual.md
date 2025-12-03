# Technical Manual: Library Management System

## 1. General System Description

### Purpose and Scope
The Library Management System is a comprehensive software solution designed to manage the core operations of a library. It facilitates the management of books, users, loans, and reservations through a user-friendly Graphical User Interface (GUI). The system is built to ensure efficient tracking of inventory, streamlined borrowing processes, and robust handling of high-demand items through a reservation queue.

### Main Features
-   **Inventory Management**: Add, update, delete, and search for books. Maintains both a general (unsorted) and an ordered (sorted by ISBN) inventory.
-   **User Management**: Register, update, and delete library users.
-   **Stock Control**: Real-time tracking of book availability. Automatically increments stock for duplicate additions and decrements for loans.
-   **Loan System**: Allows users to borrow books with stock validation. Tracks loan history using a Stack data structure.
-   **Reservation System**: Enables users to reserve out-of-stock books. Manages a waitlist using a Queue data structure.
-   **Reporting**: Generates value-based reports using advanced sorting algorithms.
-   **Algorithmic Demonstrations**: Includes modules for shelf optimization (Brute Force, Backtracking) and statistical analysis (Recursion).

---

## 2. Architecture Overview

The system follows a modular architecture, separating the frontend presentation layer from the backend logic and data management.

### Frontend (GUI)
-   **Framework**: Python `tkinter`
-   **Structure**: The GUI is organized into a main `LibraryApp` class containing a `ttk.Notebook` for tabbed navigation. Each functional module (User, Book, Shelf, Loans, Reservations, Reports) is encapsulated in its own Frame class (e.g., `UserManagementFrame`, `BookManagementFrame`).
-   **Responsibility**: Handles user input, displays data (using Treeviews and Listboxes), and invokes backend methods.

### Backend (Logic & Data)
-   **Controller**: `InventoryManager` class acts as the central facade, coordinating interactions between data models, data structures, and algorithms.
-   **Entities**: `Book` and `User` classes define the core data objects.
-   **Data Persistence**:
    -   **Inventory**: Loaded from CSV/JSON files.
    -   **State**: Loan history and Reservation queues are persisted to JSON files (`loans.json`, `reservations.json`).

### Technologies Used
-   **Language**: Python 3.x
-   **GUI Library**: Tkinter (Standard Python GUI)
-   **Data Formats**: CSV, JSON

---

## 3. Data Structures Used

The system employs specific data structures chosen for their efficiency in particular operations.

| Data Structure | Usage | Justification |
| :--- | :--- | :--- |
| **List (Dynamic Array)** | `general_inventory`, `users` | Provides flexible storage for collections where order of insertion matters or random access is needed. |
| **Sorted List** | `ordered_inventory` | Maintained sorted by ISBN to enable efficient Binary Search ($O(\log n)$). |
| **Stack (LIFO)** | `user_history` | Used for tracking loan history. The Last-In-First-Out nature is ideal for "undo" operations or viewing the most recent transactions first. |
| **Queue (FIFO)** | `reservations` | Used for the reservation waitlist. The First-In-First-Out nature ensures fairness: the first person to reserve is the first to receive the book. |
| **Dictionary** | Internal Lookups | Used implicitly in `Book.to_dict()` and JSON serialization for key-value mapping. |

---

## 4. Description of Entities

### Book
Represents a physical book in the library.
-   **Attributes**:
    -   `isbn` (str): Unique identifier (Key).
    -   `title` (str): Name of the book.
    -   `author` (str): Writer of the book.
    -   `weight_kg` (float): Physical weight (used for shelf algorithms).
    -   `value_cop` (float): Monetary value (used for reports).
    -   `stock` (int): Quantity available. Defaults to 1, increments on duplicate addition.

### User
Represents a registered library member.
-   **Attributes**:
    -   `user_id` (str): Unique identifier.
    -   `name` (str): Full name.

---

## 5. System Logic & Algorithms

### Stock Management Logic
The system implements "Real Stock Management" to handle physical inventory counts.

1.  **Adding Books**:
    -   **Check**: Does a book with this ISBN already exist?
    -   **If Yes**: Increment `stock` by 1. Do not create a new object.
    -   **If No**: Create new `Book` object with `stock = 1`. Add to `general_inventory` and `ordered_inventory`.

2.  **Borrowing Books**:
    -   **Check**: Is `stock > 0`?
    -   **If Yes**: Decrement `stock` by 1. Record loan in `user_history`.
    -   **If No**: Deny transaction. Prompt user to reserve.

3.  **Returning Books**:
    -   **Check**: Is `reservations` queue empty?
    -   **If Empty**: Increment `stock` by 1.
    -   **If Not Empty**: Dequeue the next user. The book is logically assigned to them (stock remains 0 or effectively transfers).

### Implemented Algorithms

| Algorithm | Type | Usage | Complexity |
| :--- | :--- | :--- | :--- |
| **Insertion Sort** | Sorting | Inserts new books into `ordered_inventory` while maintaining ISBN order. | $O(n)$ (Best case), $O(n^2)$ (Worst) |
| **Merge Sort** | Sorting | Sorts `general_inventory` by Value (COP) for generating reports. Stable and efficient for large datasets. | $O(n \log n)$ |
| **Binary Search** | Searching | Finds books by ISBN in `ordered_inventory`. | $O(\log n)$ |
| **Linear Search** | Searching | Finds books by Title/Author in `general_inventory`. | $O(n)$ |
| **Brute Force** | Optimization | Finds all shelf combinations > 8kg. | $O(2^n)$ |
| **Backtracking** | Optimization | Finds shelf combination with max value <= 8kg (Knapsack-style). | $O(2^n)$ |
| **Recursion** | Traversal | Calculates total value of books by a specific author. | $O(n)$ |

---

## 6. Execution Results & Scenarios

### Scenario A: Adding Duplicate Books
**Input**: Adding "The Great Gatsby" (ISBN: 123) when it already exists with Stock: 1.
**System Behavior**:
1.  Detects ISBN 123 in `ordered_inventory`.
2.  Updates `stock` to 2.
3.  Returns success message: "Stock updated for The Great Gatsby: 2".

### Scenario B: Borrowing with Stock
**Input**: User borrows "1984" (Stock: 5).
**System Behavior**:
1.  Validates `stock > 0`.
2.  Decrements `stock` to 4.
3.  Pushes transaction to `user_history` Stack.
4.  UI updates to show Stock: 4.

### Scenario C: Borrowing without Stock
**Input**: User attempts to borrow "Dune" (Stock: 0).
**System Behavior**:
1.  Validates `stock > 0` -> False.
2.  Blocks transaction.
3.  Displays error: "Book is out of stock."
4.  Enables "Reserve" option.

### Scenario D: Reservation Fulfillment
**Input**: "Dune" (Stock: 0) is returned. Queue has [User A, User B].
**System Behavior**:
1.  Book returned.
2.  Checks Queue -> Not Empty.
3.  Dequeues User A.
4.  Assigns book to User A.
5.  Stock remains 0 (or transitions to 1 then immediately 0 depending on implementation nuance, effectively 0 available for general borrowing).
6.  Log: "Reserved book assigned to User ID: User A".

---

## 7. Justification of Design Decisions

### Data Structure Choices
-   **Why Stack for Loans?**: A stack perfectly models a "history" view where the most recent actions are most relevant. It also supports a simple "undo" or "return last" workflow if needed.
-   **Why Queue for Reservations?**: Fairness is critical in waitlists. A FIFO Queue is the only structure that guarantees the first person to ask is the first served.
-   **Why Two Inventory Lists?**:
    -   `general_inventory` preserves insertion order and allows for flexible sorting (like by Value) without disrupting the main index.
    -   `ordered_inventory` is strictly for ISBN lookups, optimizing the most frequent system operation (finding a book) via Binary Search.

### Algorithmic Approach
-   **Insertion Sort vs. Quick Sort**: Since books are added one by one, the list is already sorted. Insertion Sort is extremely efficient ($O(n)$) for adding a single element to an already sorted list, whereas Quick Sort would be overkill ($O(n \log n)$).
-   **Merge Sort for Reports**: Reporting is a batch operation. Merge Sort provides consistent $O(n \log n)$ performance regardless of data state, ensuring reliability for large reports.

### Architecture
-   **Separation of Concerns**: Logic is isolated in `InventoryManager`. The GUI only handles presentation. This allows the backend to be tested independently (as seen in `test_stock_system.py`) or swapped for a web interface (Flask/Django) in the future without rewriting core logic.
