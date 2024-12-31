class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

# Example usage
if __name__ == "__main__":
    my_contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Display Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: Raju")
            phone = input("Enter phone number: 6684591262")
            email = input("Enter email:raju123@gmail.com ")
            my_contact_book.add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter name to find: divya")
            contact = my_contact_book.find_contact(name)
            if contact:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
            else:
                print("Contact not found.")

        elif choice == '3':
            my_contact_book.display_contacts()

        elif choice == '4':
            name = input("Enter name to delete: ram")
            my_contact_book.delete_contact(name)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")