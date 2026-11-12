# Smart Inventory System

## Project Overview
The Smart Inventory System is a Python-based application developed using Object-Oriented Programming (OOP) concepts. It manages books, magazines, and digital media through a menu-driven interface.

## Features
- Add books, magazines, and digital media.
- Display all inventory items.
- Search items using their unique ID.
- Borrow and return inventory items.
- Calculate borrowing fees.
- Generate audit reports.
- Track item availability.

## Technologies Used
- Python 3
- Object-Oriented Programming
- ABC (Abstract Base Class)
- Python Modules

## OOP Concepts Implemented
1. **Abstraction:** `LibraryItem` is an abstract base class.
2. **Encapsulation:** Private attributes protect item information.
3. **Inheritance:** Book, Magazine, and DigitalMedia inherit from LibraryItem.
4. **Polymorphism:** Each item type implements its own fee calculation.
5. **Property Decorators:** Getters and setters control attribute access.
6. **Dunder Methods:** `__str__`, `__repr__`, `__len__`, and `__eq__` are implemented.

## Project Structure
```text
Smart_Inventory_System/
│
├── models.py
├── inventory.py
└── README.md
```

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python inventory.py
```

## Borrowing Fee Rates

| Item Type | Fee per Day |
|---|---:|
| Book | ₹5 |
| Magazine | ₹3 |
| Digital Media | ₹2 |

## Limitations
- Inventory and audit records are stored in memory.
- Data is not retained after the application exits.
- Borrowing days are entered manually when returning an item.

## Conclusion
The Smart Inventory System demonstrates practical Python OOP concepts through an interactive inventory management application.
