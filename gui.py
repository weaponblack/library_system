import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from inventory_manager import InventoryManager

class UserManagementFrame(ttk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.create_widgets()

    def create_widgets(self):
        # Title
        ttk.Label(self, text="User Management", font=("Helvetica", 16)).pack(pady=10)

        # Input Frame
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=5)

        ttk.Label(input_frame, text="User ID:").grid(row=0, column=0, padx=5)
        self.user_id_entry = ttk.Entry(input_frame)
        self.user_id_entry.grid(row=0, column=1, padx=5)

        ttk.Label(input_frame, text="Name:").grid(row=0, column=2, padx=5)
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=0, column=3, padx=5)

        # Buttons Frame
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Add User", command=self.add_user).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Update User", command=self.update_user).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete User", command=self.delete_user).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear Fields", command=self.clear_fields).pack(side=tk.LEFT, padx=5)

        # Search Frame
        search_frame = ttk.Frame(self)
        search_frame.pack(pady=5)
        ttk.Label(search_frame, text="Search by ID:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_user).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Show All", command=self.list_users).pack(side=tk.LEFT, padx=5)

        # Listbox to display users
        self.user_listbox = tk.Listbox(self, width=50, height=15)
        self.user_listbox.pack(pady=10)
        self.user_listbox.bind('<<ListboxSelect>>', self.on_select)

    def add_user(self):
        user_id = self.user_id_entry.get()
        name = self.name_entry.get()
        if user_id and name:
            if self.manager.add_user(user_id, name):
                messagebox.showinfo("Success", "User added successfully.")
                self.list_users()
                self.clear_fields()
            else:
                messagebox.showerror("Error", "User ID already exists.")
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def update_user(self):
        user_id = self.user_id_entry.get()
        name = self.name_entry.get()
        if user_id and name:
            if self.manager.update_user(user_id, name):
                messagebox.showinfo("Success", "User updated successfully.")
                self.list_users()
                self.clear_fields()
            else:
                messagebox.showerror("Error", "User not found.")
        else:
            messagebox.showwarning("Warning", "Please enter User ID and new Name.")

    def delete_user(self):
        user_id = self.user_id_entry.get()
        if user_id:
            if messagebox.askyesno("Confirm", f"Delete user {user_id}?"):
                if self.manager.delete_user(user_id):
                    messagebox.showinfo("Success", "User deleted.")
                    self.list_users()
                    self.clear_fields()
                else:
                    messagebox.showerror("Error", "User not found.")
        else:
            messagebox.showwarning("Warning", "Please enter User ID.")

    def search_user(self):
        user_id = self.search_entry.get()
        if user_id:
            user = self.manager.find_user(user_id)
            self.user_listbox.delete(0, tk.END)
            if user:
                self.user_listbox.insert(tk.END, str(user))
            else:
                messagebox.showinfo("Result", "User not found.")
        else:
            messagebox.showwarning("Warning", "Enter ID to search.")

    def list_users(self):
        self.user_listbox.delete(0, tk.END)
        for user in self.manager.list_users():
            self.user_listbox.insert(tk.END, str(user))

    def on_select(self, event):
        try:
            selection = self.user_listbox.curselection()
            if selection:
                data = self.user_listbox.get(selection[0])
                # Parse simple string representation: User(ID='1', Name='Bob')
                # This is a bit brittle, but sufficient for this demo.
                # A better way is to store objects or a mapping.
                # For now, let's just extract ID roughly or just rely on manual entry for updates.
                # Actually, let's try to parse it to fill the fields.
                import re
                match = re.search(r"ID='(.*?)', Name='(.*?)'", data)
                if match:
                    self.user_id_entry.delete(0, tk.END)
                    self.user_id_entry.insert(0, match.group(1))
                    self.name_entry.delete(0, tk.END)
                    self.name_entry.insert(0, match.group(2))
        except Exception:
            pass

    def clear_fields(self):
        self.user_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)


class BookManagementFrame(ttk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.create_widgets()

    def create_widgets(self):
        # Title
        ttk.Label(self, text="Book Management", font=("Helvetica", 16)).pack(pady=10)

        # Input Frame
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=5)

        ttk.Label(input_frame, text="ISBN:").grid(row=0, column=0, padx=5)
        self.isbn_entry = ttk.Entry(input_frame)
        self.isbn_entry.grid(row=0, column=1, padx=5)

        ttk.Label(input_frame, text="Title:").grid(row=0, column=2, padx=5)
        self.title_entry = ttk.Entry(input_frame)
        self.title_entry.grid(row=0, column=3, padx=5)

        ttk.Label(input_frame, text="Author:").grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = ttk.Entry(input_frame)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Weight (kg):").grid(row=1, column=2, padx=5, pady=5)
        self.weight_entry = ttk.Entry(input_frame)
        self.weight_entry.grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Value (COP):").grid(row=2, column=0, padx=5, pady=5)
        self.value_entry = ttk.Entry(input_frame)
        self.value_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons Frame
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Add Book", command=self.add_book).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Update Book", command=self.update_book).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete Book", command=self.delete_book).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear Fields", command=self.clear_fields).pack(side=tk.LEFT, padx=5)

        # Search Frame
        search_frame = ttk.Frame(self)
        search_frame.pack(pady=5)
        ttk.Label(search_frame, text="Search ISBN:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Linear Search", command=lambda: self.search_book("linear")).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Binary Search", command=lambda: self.search_book("binary")).pack(side=tk.LEFT, padx=5)

        # List Buttons
        list_btn_frame = ttk.Frame(self)
        list_btn_frame.pack(pady=5)
        ttk.Button(list_btn_frame, text="List General Inventory", command=self.list_general).pack(side=tk.LEFT, padx=5)
        ttk.Button(list_btn_frame, text="List Ordered Inventory", command=self.list_ordered).pack(side=tk.LEFT, padx=5)

        # Treeview for Books
        columns = ("ISBN", "Title", "Author", "Weight", "Value", "Stock")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)
        self.tree.bind('<<TreeviewSelect>>', self.on_select)
        
        # Initial population
        self.list_ordered()

    def add_book(self):
        try:
            isbn = self.isbn_entry.get()
            title = self.title_entry.get()
            author = self.author_entry.get()
            weight = float(self.weight_entry.get())
            value = float(self.value_entry.get())
            
            from models import Book
            new_book = Book(isbn, title, author, weight, value)
            
            # Use manager's add_book to handle stock logic
            added_book = self.manager.add_book(new_book)
            
            messagebox.showinfo("Success", f"Book processed. Current Stock: {added_book.stock}")
            self.list_ordered()
            self.clear_fields()
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Weight or Value.")

    def update_book(self):
        # For simplicity, we'll update in place if found. 
        # Note: Changing ISBN would require re-sorting, so let's disallow ISBN change or handle it carefully.
        # Here we will just update other fields.
        isbn = self.isbn_entry.get()
        book = self.manager.find_book_by_isbn(isbn)
        if book:
            try:
                book.title = self.title_entry.get()
                book.author = self.author_entry.get()
                book.weight_kg = float(self.weight_entry.get())
                book.value_cop = float(self.value_entry.get())
                messagebox.showinfo("Success", "Book updated.")
                self.list_ordered()
                self.clear_fields()
            except ValueError:
                messagebox.showerror("Error", "Invalid input.")
        else:
            messagebox.showerror("Error", "Book not found.")

    def delete_book(self):
        isbn = self.isbn_entry.get()
        # Deleting from both lists is tricky without a dedicated method in manager, 
        # but I'll implement it here for the GUI requirement.
        # Ideally, move this logic to InventoryManager.
        book = self.manager.find_book_by_isbn(isbn)
        if book:
            if messagebox.askyesno("Confirm", f"Delete book {isbn}?"):
                if book in self.manager.general_inventory:
                    self.manager.general_inventory.remove(book)
                if book in self.manager.ordered_inventory:
                    self.manager.ordered_inventory.remove(book)
                messagebox.showinfo("Success", "Book deleted.")
                self.list_ordered()
                self.clear_fields()
        else:
            messagebox.showerror("Error", "Book not found.")

    def search_book(self, method):
        isbn = self.search_entry.get()
        if not isbn:
            messagebox.showwarning("Warning", "Enter ISBN to search.")
            return

        import searching_algorithms
        if method == "linear":
            # Linear search on general inventory
            # We need to adapt linear_search to return index or object. 
            # The existing linear_search returns index.
            # Let's assume general_inventory is the target.
            # But general_inventory contains objects, linear_search might expect list of objects and a key?
            # Let's check searching_algorithms.py signature.
            # Assuming it takes (list, target_isbn).
            # Wait, I need to check searching_algorithms.py content to be sure.
            # I'll assume standard implementation for now or check it quickly.
            # Actually, I'll just use the manager's find method for binary, and implement linear here or call manager.
            # The requirement says "demonstration".
            
            # Let's use the manager's list.
            found = False
            for book in self.manager.general_inventory:
                if book.isbn == isbn:
                    self.tree.delete(*self.tree.get_children())
                    self.tree.insert("", tk.END, values=(book.isbn, book.title, book.author, book.weight_kg, book.value_cop, book.stock))
                    found = True
                    break
            if not found:
                 messagebox.showinfo("Result", "Book not found (Linear Search).")
        
        elif method == "binary":
            # Use binary_search directly to get index
            import searching_algorithms
            # Ensure ordered inventory is sorted (it should be, but binary search requires it)
            # self.manager.ordered_inventory is sorted by insertion logic
            
            index = searching_algorithms.binary_search(self.manager.ordered_inventory, isbn)
            
            self.tree.delete(*self.tree.get_children())
            if index != -1:
                book = self.manager.ordered_inventory[index]
                self.tree.insert("", tk.END, values=(book.isbn, book.title, book.author, book.weight_kg, book.value_cop, book.stock))
                
                msg = f"Book found at position {index}."
                if book.stock == 0:
                    res_count = self.manager.reservations.count_reservations(isbn)
                    msg += f"\n\nWARNING: Book is out of stock."
                    if res_count > 0:
                        msg += f"\nThere are {res_count} active reservation(s) for this ISBN."
                    else:
                        msg += "\nNo active reservations."
                
                messagebox.showinfo("Result", msg)
            else:
                # Check for active reservations
                res_count = self.manager.reservations.count_reservations(isbn)
                msg = f"Book not found in inventory."
                if res_count > 0:
                    msg += f"\n\nHowever, there are {res_count} active reservation(s) for this ISBN."
                else:
                    msg += "\nNo active reservations for this ISBN."
                
                messagebox.showinfo("Result", msg)

    def list_general(self):
        self.tree.delete(*self.tree.get_children())
        for book in self.manager.general_inventory:
            self.tree.insert("", tk.END, values=(book.isbn, book.title, book.author, book.weight_kg, book.value_cop, book.stock))

    def list_ordered(self):
        self.tree.delete(*self.tree.get_children())
        for book in self.manager.ordered_inventory:
            self.tree.insert("", tk.END, values=(book.isbn, book.title, book.author, book.weight_kg, book.value_cop, book.stock))

    def on_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            if values:
                self.isbn_entry.delete(0, tk.END)
                self.isbn_entry.insert(0, values[0])
                self.title_entry.delete(0, tk.END)
                self.title_entry.insert(0, values[1])
                self.author_entry.delete(0, tk.END)
                self.author_entry.insert(0, values[2])
                self.weight_entry.delete(0, tk.END)
                self.weight_entry.insert(0, values[3])
                self.value_entry.delete(0, tk.END)
                self.value_entry.insert(0, values[4])

    def clear_fields(self):
        self.isbn_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)


class ShelfManagementFrame(ttk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.current_shelf_books = []
        self.create_widgets()

    def create_widgets(self):
        # Title
        ttk.Label(self, text="Shelf Management & Algorithms", font=("Helvetica", 16)).pack(pady=10)

        # Top Frame: Book Selection
        top_frame = ttk.LabelFrame(self, text="Build a Shelf (Select Books)")
        top_frame.pack(pady=5, fill=tk.BOTH, expand=True, padx=10)

        # Inventory List (Left)
        inv_frame = ttk.Frame(top_frame)
        inv_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        ttk.Label(inv_frame, text="Available Inventory").pack()
        
        self.inv_listbox = tk.Listbox(inv_frame, selectmode=tk.MULTIPLE)
        self.inv_listbox.pack(fill=tk.BOTH, expand=True)
        
        # Buttons (Center)
        btn_frame = ttk.Frame(top_frame)
        btn_frame.pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Add >>", command=self.add_to_shelf).pack(pady=5)
        ttk.Button(btn_frame, text="<< Remove", command=self.remove_from_shelf).pack(pady=5)

        # Shelf List (Right)
        shelf_frame = ttk.Frame(top_frame)
        shelf_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        ttk.Label(shelf_frame, text="Books on Shelf").pack()
        
        self.shelf_listbox = tk.Listbox(shelf_frame, selectmode=tk.MULTIPLE)
        self.shelf_listbox.pack(fill=tk.BOTH, expand=True)

        # Refresh Button
        ttk.Button(self, text="Refresh Inventory List", command=self.refresh_inventory).pack(pady=5)

        # Algorithm Controls
        algo_frame = ttk.LabelFrame(self, text="Run Algorithms")
        algo_frame.pack(pady=10, fill=tk.X, padx=10)

        ttk.Button(algo_frame, text="Brute Force (Heavy Shelf > 8kg)", command=self.run_brute_force).pack(side=tk.LEFT, padx=20, pady=10)
        ttk.Button(algo_frame, text="Backtracking (Optimal Value <= 8kg)", command=self.run_backtracking).pack(side=tk.LEFT, padx=20, pady=10)

        # Results Area
        res_frame = ttk.LabelFrame(self, text="Results")
        res_frame.pack(pady=5, fill=tk.BOTH, expand=True, padx=10)
        self.result_text = tk.Text(res_frame, height=10)
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def refresh_inventory(self):
        self.inv_listbox.delete(0, tk.END)
        for book in self.manager.general_inventory:
            self.inv_listbox.insert(tk.END, f"{book.isbn} - {book.title} ({book.weight_kg}kg, ${book.value_cop})")

    def add_to_shelf(self):
        selections = self.inv_listbox.curselection()
        for i in selections:
            book_str = self.inv_listbox.get(i)
            # Find book object (simple parsing or index matching if list didn't change)
            # Safer to parse ISBN
            isbn = book_str.split(' - ')[0]
            book = self.manager.find_book_by_isbn(isbn) # This uses ordered inventory, but ISBN should match
            if book and book not in self.current_shelf_books:
                self.current_shelf_books.append(book)
                self.shelf_listbox.insert(tk.END, book_str)

    def remove_from_shelf(self):
        selections = self.shelf_listbox.curselection()
        # Remove in reverse order to maintain indices
        for i in reversed(selections):
            self.shelf_listbox.delete(i)
            del self.current_shelf_books[i]

    def run_brute_force(self):
        if len(self.current_shelf_books) < 4:
            messagebox.showwarning("Warning", "Need at least 4 books for this brute force demo.")
            return
        
        from problem_solving import brute_force_heavy_shelf
        results = brute_force_heavy_shelf(self.current_shelf_books)
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Brute Force Results (Combinations > 8kg):\nFound {len(results)} combinations.\n\n")
        for i, combo in enumerate(results, 1):
            total_weight = sum(b.weight_kg for b in combo)
            self.result_text.insert(tk.END, f"Combo {i} (Total Weight: {total_weight:.2f}kg):\n")
            for b in combo:
                self.result_text.insert(tk.END, f"  - {b.title} ({b.weight_kg}kg)\n")
            self.result_text.insert(tk.END, "\n")

    def run_backtracking(self):
        from problem_solving import backtracking_optimal_shelf
        # Capture stdout to show steps
        import io
        import sys
        
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        
        best_value, best_combo = backtracking_optimal_shelf(self.current_shelf_books)
        
        sys.stdout = old_stdout
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Backtracking Results (Max Value <= 8kg):\n")
        self.result_text.insert(tk.END, f"Best Value: ${best_value}\n")
        self.result_text.insert(tk.END, "Best Combination:\n")
        for b in best_combo:
            self.result_text.insert(tk.END, f"  - {b.title} (${b.value_cop}, {b.weight_kg}kg)\n")
            
        self.result_text.insert(tk.END, "\n--- Execution Log ---\n")
        self.result_text.insert(tk.END, mystdout.getvalue())


class LoanManagementFrame(ttk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.create_widgets()

    def create_widgets(self):
        # Title
        ttk.Label(self, text="Loans Management (Stack)", font=("Helvetica", 16)).pack(pady=10)

        # Action Frame
        action_frame = ttk.LabelFrame(self, text="Borrow / Return")
        action_frame.pack(pady=5, fill=tk.X, padx=10)

        ttk.Label(action_frame, text="ISBN:").pack(side=tk.LEFT, padx=5)
        self.isbn_entry = ttk.Entry(action_frame)
        self.isbn_entry.pack(side=tk.LEFT, padx=5)

        ttk.Button(action_frame, text="Check Stock", command=self.check_stock).pack(side=tk.LEFT, padx=5)
        self.borrow_btn = ttk.Button(action_frame, text="Borrow Book", command=self.borrow_book, state=tk.DISABLED)
        self.borrow_btn.pack(side=tk.LEFT, padx=5)
        ttk.Button(action_frame, text="Return Book", command=self.return_book).pack(side=tk.LEFT, padx=5)

    def check_stock(self):
        isbn = self.isbn_entry.get()
        book = self.manager.find_book_by_isbn(isbn)
        if book:
            if book.stock > 0:
                self.borrow_btn.config(state=tk.NORMAL)
                messagebox.showinfo("Stock Available", f"Stock: {book.stock}. You can borrow.")
            else:
                self.borrow_btn.config(state=tk.DISABLED)
                messagebox.showwarning("Out of Stock", "Stock is 0. Cannot borrow.")
        else:
            self.borrow_btn.config(state=tk.DISABLED)
            messagebox.showerror("Error", "Book not found.")

        # History Frame
        hist_frame = ttk.LabelFrame(self, text="Loan History (Stack)")
        hist_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)

        self.history_list = tk.Listbox(hist_frame)
        self.history_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Stack Controls
        stack_ctrl_frame = ttk.Frame(self)
        stack_ctrl_frame.pack(pady=5)
        ttk.Button(stack_ctrl_frame, text="Refresh History", command=self.refresh_history).pack(side=tk.LEFT, padx=5)
        ttk.Button(stack_ctrl_frame, text="Save Stack", command=self.save_stack).pack(side=tk.LEFT, padx=5)
        ttk.Button(stack_ctrl_frame, text="Load Stack", command=self.load_stack).pack(side=tk.LEFT, padx=5)

    def borrow_book(self):
        isbn = self.isbn_entry.get()
        success, result = self.manager.borrow_book(isbn)
        
        if success:
            messagebox.showinfo("Success", f"Borrowed {result.title}. New Stock: {result.stock}")
            self.refresh_history()
        else:
            messagebox.showwarning("Failed", result)

    def return_book(self):
        isbn = self.isbn_entry.get()
        # We should check if this user actually borrowed it, but for this simplified system 
        # we just process the return of the ISBN.
        
        # Capture stdout for process_return output
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        
        self.manager.process_return(isbn)
        
        sys.stdout = old_stdout
        output = mystdout.getvalue()
        
        messagebox.showinfo("Return Processed", output)
        self.refresh_history() # History stack doesn't change on return in this model, but good to refresh UI

    def refresh_history(self):
        self.history_list.delete(0, tk.END)
        # Stack doesn't have iteration method exposed directly in data_structures.py, 
        # but we can access .items for display purposes.
        # Ideally we should add an iterator or get_all method.
        # I'll access .items directly since I'm the developer.
        for item in reversed(self.manager.user_history.items):
            self.history_list.insert(tk.END, f"ISBN: {item['isbn']} - Date: {item['loan_date']}")

    def save_stack(self):
        filepath = "data/loans.json"
        self.manager.user_history.save_to_file(filepath)
        messagebox.showinfo("Saved", f"Stack saved to {filepath}")

    def load_stack(self):
        filepath = "data/loans.json"
        self.manager.user_history.load_from_file(filepath)
        self.refresh_history()
        messagebox.showinfo("Loaded", f"Stack loaded from {filepath}")


class ReservationManagementFrame(ttk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.create_widgets()

    def create_widgets(self):
        # Title
        ttk.Label(self, text="Reservations (Queue)", font=("Helvetica", 16)).pack(pady=10)

        # Action Frame
        action_frame = ttk.LabelFrame(self, text="Create Reservation")
        action_frame.pack(pady=5, fill=tk.X, padx=10)

        ttk.Label(action_frame, text="User ID:").pack(side=tk.LEFT, padx=5)
        self.user_id_entry = ttk.Entry(action_frame)
        self.user_id_entry.pack(side=tk.LEFT, padx=5)

        ttk.Label(action_frame, text="Book ISBN:").pack(side=tk.LEFT, padx=5)
        self.isbn_entry = ttk.Entry(action_frame)
        self.isbn_entry.pack(side=tk.LEFT, padx=5)

        ttk.Button(action_frame, text="Reserve", command=self.reserve_book).pack(side=tk.LEFT, padx=5)

        # Queue Frame
        q_frame = ttk.LabelFrame(self, text="Reservation Queue (FIFO)")
        q_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)

        self.queue_list = tk.Listbox(q_frame)
        self.queue_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Queue Controls
        q_ctrl_frame = ttk.Frame(self)
        q_ctrl_frame.pack(pady=5)
        ttk.Button(q_ctrl_frame, text="Refresh Queue", command=self.refresh_queue).pack(side=tk.LEFT, padx=5)
        ttk.Button(q_ctrl_frame, text="Save Queue", command=self.save_queue).pack(side=tk.LEFT, padx=5)
        ttk.Button(q_ctrl_frame, text="Load Queue", command=self.load_queue).pack(side=tk.LEFT, padx=5)

    def reserve_book(self):
        user_id = self.user_id_entry.get()
        isbn = self.isbn_entry.get()
        
        if not user_id or not isbn:
            messagebox.showwarning("Warning", "Enter User ID and ISBN.")
            return

        book = self.manager.find_book_by_isbn(isbn)
        if not book:
            messagebox.showerror("Error", "Book not found.")
            return

        # Check if user exists
        if not self.manager.find_user(user_id):
            messagebox.showerror("Error", "User ID not found.")
            return

        if self.manager.reservations.enqueue(user_id, book.stock,isbn):
            messagebox.showinfo("Success", "Reservation added to queue.")
            self.refresh_queue()
        else:
            messagebox.showwarning("Failed", "Cannot reserve: Book is currently in stock.")

    def refresh_queue(self):
        self.queue_list.delete(0, tk.END)
        for item in self.manager.reservations.items:
            self.queue_list.insert(tk.END, f"User: {item['user_id']} - Date: {item['request_date']}")

    def save_queue(self):
        filepath = "data/reservations.json"
        self.manager.reservations.save_to_file(filepath)
        messagebox.showinfo("Saved", f"Queue saved to {filepath}")

    def load_queue(self):
        filepath = "data/reservations.json"
        self.manager.reservations.load_from_file(filepath)
        self.refresh_queue()
        messagebox.showinfo("Loaded", f"Queue loaded from {filepath}")


class ReportsFrame(ttk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.create_widgets()

    def create_widgets(self):
        # Title
        ttk.Label(self, text="Reports", font=("Helvetica", 16)).pack(pady=10)

        # Value Report
        val_frame = ttk.LabelFrame(self, text="Value Report (Merge Sort)")
        val_frame.pack(pady=10, fill=tk.X, padx=10)

        ttk.Label(val_frame, text="Generate a report of books sorted by value.").pack(pady=5)
        ttk.Button(val_frame, text="Generate Report", command=self.generate_report).pack(pady=10)

    def generate_report(self):
        filepath = "reports/value_report.csv"
        self.manager.generate_value_report(filepath)
        messagebox.showinfo("Success", f"Report generated at {filepath}")


class AlgorithmsDemoFrame(ttk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.create_widgets()

    def create_widgets(self):
        # Title
        ttk.Label(self, text="Algorithms Demo (Recursion)", font=("Helvetica", 16)).pack(pady=10)

        # Input Frame
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=5)

        ttk.Label(input_frame, text="Author Name:").pack(side=tk.LEFT, padx=5)
        self.author_entry = ttk.Entry(input_frame)
        self.author_entry.pack(side=tk.LEFT, padx=5)

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Total Value (Stack Recursion)", command=self.run_total_value).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Avg Weight (Tail Recursion)", command=self.run_avg_weight).pack(side=tk.LEFT, padx=5)

        # Results
        res_frame = ttk.LabelFrame(self, text="Results")
        res_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)
        self.result_text = tk.Text(res_frame, height=10)
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def run_total_value(self):
        author = self.author_entry.get()
        if not author:
            messagebox.showwarning("Warning", "Enter Author Name.")
            return

        from problem_solving import recursive_total_value_by_author
        # Use general inventory for this
        total_value = recursive_total_value_by_author(self.manager.general_inventory, author)
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Recursive Total Value for '{author}': ${total_value:.2f}\n")

    def run_avg_weight(self):
        author = self.author_entry.get()
        if not author:
            messagebox.showwarning("Warning", "Enter Author Name.")
            return

        from problem_solving import tail_recursive_average_weight_by_author
        avg_weight = tail_recursive_average_weight_by_author(self.manager.general_inventory, author)
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Tail Recursive Average Weight for '{author}': {avg_weight:.2f}kg\n")


class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("900x700")
        
        self.manager = InventoryManager()
        
        # Load initial inventory
        import os
        data_path = os.path.join('data', 'books.csv')
        self.manager.load_inventory(data_path)
        
        # Create Notebook (Tabs)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Add Modules
        self.add_modules()
        
    def add_modules(self):
        # User Management
        self.user_frame = UserManagementFrame(self.notebook, self.manager)
        self.notebook.add(self.user_frame, text="User Management")
        
        # Book Management
        self.book_frame = BookManagementFrame(self.notebook, self.manager)
        self.notebook.add(self.book_frame, text="Book Management")
        
        # Shelf Management
        self.shelf_frame = ShelfManagementFrame(self.notebook, self.manager)
        self.notebook.add(self.shelf_frame, text="Shelf Management")
        
        # Loans
        self.loan_frame = LoanManagementFrame(self.notebook, self.manager)
        self.notebook.add(self.loan_frame, text="Loans")
        
        # Reservations
        self.reservation_frame = ReservationManagementFrame(self.notebook, self.manager)
        self.notebook.add(self.reservation_frame, text="Reservations")
        
        # Reports
        self.reports_frame = ReportsFrame(self.notebook, self.manager)
        self.notebook.add(self.reports_frame, text="Reports")
        
        # Algorithms Demo
        self.algo_frame = AlgorithmsDemoFrame(self.notebook, self.manager)
        self.notebook.add(self.algo_frame, text="Algorithms Demo")


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
