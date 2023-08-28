class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    def view_contacts(self):
        print("Contact List:")
        for name, contact in self.contacts.items():
            print(f"{name} - {contact.phone_number}")

    def search_contact(self, search_term):
        search_results = []
        for name, contact in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in contact.phone_number:
                search_results.append(contact)
        return search_results

    def update_contact(self, contact_name, new_contact):
        if contact_name in self.contacts:
            self.contacts[contact_name] = new_contact
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, contact_name):
        if contact_name in self.contacts:
            del self.contacts[contact_name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")


def main():
    cms = ContactManagementSystem()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            cms.add_contact(new_contact)
            print("Contact added successfully!")

        elif choice == "2":
            cms.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            search_results = cms.search_contact(search_term)
            if search_results:
                print("Search results:")
                for contact in search_results:
                    print(f"{contact.name} - {contact.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            contact_name = input("Enter the name of the contact to update: ")
            if contact_name in cms.contacts:
                updated_name = input("Enter new name: ")
                updated_phone = input("Enter new phone number: ")
                updated_email = input("Enter new email: ")
                updated_address = input("Enter new address: ")
                updated_contact = Contact(updated_name, updated_phone, updated_email, updated_address)
                cms.update_contact(contact_name, updated_contact)
            else:
                print("Contact not found.")

        elif choice == "5":
            contact_name = input("Enter the name of the contact to delete: ")
            cms.delete_contact(contact_name)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
