class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.next = None
        self.available = True

class Inventory:
    def __init__(self):
        self.head = None

    def add_book(self, title, author):
        new_book = Book(title, author)
        new_book.next = self.head
        self.head = new_book

    def search(self, keyword):
        results = []
        current = self.head
        while current:
            if keyword.lower() in current.title.lower() or keyword.lower() in current.author.lower():
                results.append((current.title, current.author, current.available))
            current = current.next
        return results

    def find_book(self, title):
        current = self.head
        while current:
            if current.title.lower() == title.lower():
                return current
            current = current.next
        return None

class UndoStack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        return self.stack.pop() if self.stack else None

class Library:
    def __init__(self):
        self.inventory = Inventory()
        self.undo_stack = UndoStack()

    def borrow_book(self, title):
        book = self.inventory.find_book(title)
        if book and book.available:
            book.available = False
            self.undo_stack.push(("borrow", book))
            return True
        return False

    def return_book(self, title):
        book = self.inventory.find_book(title)
        if book and not book.available:
            book.available = True
            self.undo_stack.push(("return", book))
            return True
        return False

    def undo(self):
        action = self.undo_stack.pop()
        if action:
            act, book = action
            if act == "borrow":
                book.available = True
            elif act == "return":
                book.available = False
            return True
        return False

library = Library()
library.inventory.add_book("Python Programming", "John Doe")
library.inventory.add_book("Data Structures", "Jane Smith")
library.inventory.add_book("Algorithms", "Robert Martin")

print(library.borrow_book("Python Programming"))
print(library.return_book("Python Programming"))
print(library.undo())
print(library.inventory.search("Jane"))
