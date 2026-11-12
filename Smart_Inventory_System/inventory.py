
from models import Book, Magazine, DigitalMedia
from datetime import date


# Step 1: Inventory Manager Class
class InventoryManager:

    def __init__(self):
        self.__items = {}
        self.__audit_log = []

    # Add item to inventory
    def add_item(self, item):

        if item.item_id in self.__items:
            print("Item ID already exists!")
            return

        self.__items[item.item_id] = item
        self.__audit_log.append(
            f"{date.today()} - Added: {item.title}"
        )

        print("Item added successfully!")

    # Display all items
    def display_items(self):

        if not self.__items:
            print("Inventory is empty!")
            return

        print("\n========== INVENTORY ==========")

        for item in self.__items.values():

            status = "Borrowed" if item.is_borrowed else "Available"

            print(item.display_metadata())
            print("Status:", status)
            print("-" * 40)

    # Search item
    def search_item(self, item_id):

        item = self.__items.get(item_id)

        if item:
            print("\nItem Found:")
            print(item.display_metadata())
            return item

        print("Item not found!")
        return None

    # Borrow item
    def checkout_item(self, item_id):

        item = self.__items.get(item_id)

        if item is None:
            print("Item not found!")
            return

        try:
            item.checkout(date.today())

            self.__audit_log.append(
                f"{date.today()} - Borrowed: {item.title}"
            )

            print("Item borrowed successfully!")

        except ValueError as error:
            print(error)

    # Return item
    def return_item(self, item_id, days):

        item = self.__items.get(item_id)

        if item is None:
            print("Item not found!")
            return

        if not isinstance(days, int) or days < 0:
            print("Days must be a non-negative integer!")
            return

        try:
            fee = item.calculate_fee(days)

            item.return_item()

            self.__audit_log.append(
                f"{date.today()} - Returned: {item.title} | Fee: ₹{fee}"
            )

            print("Item returned successfully!")
            print("Borrowing fee: ₹", fee)

        except ValueError as error:
            print(error)

    # Generate audit report
    def generate_report(self):

        print("\n========== AUDIT REPORT ==========")

        if not self.__audit_log:
            print("No activities recorded.")
            return

        for record in self.__audit_log:
            print(record)

        print("\nTotal inventory items:", len(self.__items))


# Step 2: Main program
def main():

    inventory = InventoryManager()

    while True:

        print("\n===== SMART INVENTORY SYSTEM =====")
        print("1. Add Book")
        print("2. Add Magazine")
        print("3. Add Digital Media")
        print("4. Display Inventory")
        print("5. Search Item")
        print("6. Borrow Item")
        print("7. Return Item")
        print("8. Generate Audit Report")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        try:

            if choice == "1":

                item_id = input("Enter Book ID: ").strip()
                title = input("Enter Book Title: ").strip()
                price = float(input("Enter Book Price: "))
                author = input("Enter Author Name: ").strip()

                item = Book(item_id, title, price, author)
                inventory.add_item(item)

            elif choice == "2":

                item_id = input("Enter Magazine ID: ").strip()
                title = input("Enter Magazine Title: ").strip()
                price = float(input("Enter Magazine Price: "))
                issue = input("Enter Issue Number: ").strip()

                item = Magazine(item_id, title, price, issue)
                inventory.add_item(item)

            elif choice == "3":

                item_id = input("Enter Media ID: ").strip()
                title = input("Enter Media Title: ").strip()
                price = float(input("Enter Media Price: "))
                file_format = input("Enter File Format: ").strip()

                item = DigitalMedia(
                    item_id, title, price, file_format
                )

                inventory.add_item(item)

            elif choice == "4":

                inventory.display_items()

            elif choice == "5":

                item_id = input("Enter Item ID: ").strip()
                inventory.search_item(item_id)

            elif choice == "6":

                item_id = input("Enter Item ID to borrow: ").strip()
                inventory.checkout_item(item_id)

            elif choice == "7":

                item_id = input("Enter Item ID to return: ").strip()
                days = int(input("Enter number of borrowed days: "))

                inventory.return_item(item_id, days)

            elif choice == "8":

                inventory.generate_report()

            elif choice == "9":

                print("Thank you for using Smart Inventory System!")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError as error:
            print("Invalid input:", error)

        except (EOFError, KeyboardInterrupt):
            print("\nProgram terminated.")
            break


if __name__ == "__main__":
    main()
