from inventory_manager import InventoryManager
from models import Book

def verify_search_feedback():
    manager = InventoryManager()
    
    # Setup
    # Add Book A
    book_a = Book("978-A", "Book A", "Author A", 1.0, 100)
    manager.add_book(book_a)
    
    # Reserve Book B (which doesn't exist in inventory)
    # Note: Our system allows reserving books that are not in inventory if we manually enqueue
    # In GUI, you can't reserve if not found, but we are testing the "Not Found" logic here.
    # So let's simulate a reservation for a non-existent book (maybe it was deleted?)
    print("\n--- Setup: Reserving non-existent Book B ---")
    manager.reservations.enqueue("User 2", 0, "978-B")
    
    # 1. Search for Book A (Should be found)
    print("\n--- Test 1: Search Existing Book (978-A) ---")
    # We simulate what the GUI does: call binary_search directly
    from searching_algorithms import binary_search
    index = binary_search(manager.ordered_inventory, "978-A")
    if index != -1:
        print(f"PASS: Book A found at index {index}.")
    else:
        print("FAIL: Book A not found.")
        
    # 2. Search for Book B (Should be NOT found, but have reservations)
    print("\n--- Test 2: Search Non-Existent Book with Reservations (978-B) ---")
    index_b = binary_search(manager.ordered_inventory, "978-B")
    if index_b == -1:
        print("PASS: Book B correctly not found in inventory.")
        res_count = manager.reservations.count_reservations("978-B")
        if res_count == 1:
            print(f"PASS: Correctly detected {res_count} reservation for Book B.")
        else:
            print(f"FAIL: Expected 1 reservation, found {res_count}.")
    else:
        print(f"FAIL: Book B found at index {index_b} (Should not exist).")

    # 3. Search for Book C (Should be NOT found, NO reservations)
    print("\n--- Test 3: Search Non-Existent Book with NO Reservations (978-C) ---")
    index_c = binary_search(manager.ordered_inventory, "978-C")
    if index_c == -1:
        print("PASS: Book C correctly not found.")
        res_count_c = manager.reservations.count_reservations("978-C")
        if res_count_c == 0:
            print("PASS: Correctly detected 0 reservations for Book C.")
        else:
            print(f"FAIL: Expected 0 reservations, found {res_count_c}.")

    # 4. Search for Book A (Found, Stock 0, with Reservations)
    print("\n--- Test 4: Search Found Book with 0 Stock and Reservations (978-A) ---")
    # Force stock to 0 and add reservation
    book_a.stock = 0
    manager.reservations.enqueue("User 1", 0, "978-A")
    
    index_a = binary_search(manager.ordered_inventory, "978-A")
    if index_a != -1:
        print(f"PASS: Book A found at index {index_a}.")
        found_book = manager.ordered_inventory[index_a]
        if found_book.stock == 0:
            print("PASS: Book A stock is 0.")
            res_count_a = manager.reservations.count_reservations("978-A")
            if res_count_a == 1:
                print(f"PASS: Correctly detected {res_count_a} reservation for Book A.")
            else:
                print(f"FAIL: Expected 1 reservation, found {res_count_a}.")
        else:
            print(f"FAIL: Book A stock is {found_book.stock}, expected 0.")
    else:
        print("FAIL: Book A not found.")

if __name__ == "__main__":
    verify_search_feedback()
