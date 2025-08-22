import os
import pickle

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class ContactBook:
    def __init__(self, filename="contacts.dat"):
        self.head = None
        self.filename = filename
        self.load()

    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        if not self.head or name.lower() < self.head.name.lower():
            new_contact.next = self.head
            self.head = new_contact
        else:
            current = self.head
            while current.next and current.next.name.lower() < name.lower():
                current = current.next
            new_contact.next = current.next
            current.next = new_contact
        self.save()

    def search_contact(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                return current
            current = current.next
        return None

    def update_contact(self, name, new_phone):
        contact = self.search_contact(name)
        if contact:
            contact.phone = new_phone
            self.save()
            return True
        return False

    def delete_contact(self, name):
        if not self.head:
            return False
        if self.head.name.lower() == name.lower():
            self.head = self.head.next
            self.save()
            return True
        current = self.head
        while current.next:
            if current.next.name.lower() == name.lower():
                current.next = current.next.next
                self.save()
                return True
            current = current.next
        return False

    def display_contacts(self):
        contacts = []
        current = self.head
        while current:
            contacts.append((current.name, current.phone))
            current = current.next
        return contacts

    def save(self):
        contacts = []
        current = self.head
        while current:
            contacts.append((current.name, current.phone))
            current = current.next
        with open(self.filename, "wb") as f:
            pickle.dump(contacts, f)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                contacts = pickle.load(f)
                for name, phone in sorted(contacts, key=lambda x: x[0].lower(), reverse=True):
                    self.add_contact(name, phone)

book = ContactBook()
book.add_contact("Alice", "12345")
book.add_contact("Bob", "67890")
book.add_contact("Charlie", "54321")
print(book.display_contacts())
print(book.search_contact("Bob").phone)
book.update_contact("Bob", "11111")
print(book.display_contacts())
book.delete_contact("Alice")
print(book.display_contacts())
