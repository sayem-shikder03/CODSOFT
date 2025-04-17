contacts = {}

# Add Contact
def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' added successfully.")

# View All Contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

# Search Contact
def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if query.lower() in name.lower() or query in info['phone']:
            print(f"\nFound Contact:\nName: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

# Update Contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.")
        return
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
    email = input(f"Enter new email (current: {contacts[name]['email']}): ")
    address = input(f"Enter new address (current: {contacts[name]['address']}): ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' updated successfully.")

# Delete Contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

# Main Menu
def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
