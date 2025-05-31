import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = input("Enter store name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("Contact added successfully.\n")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n Contact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} | {contact['phone']}")
    print()

def search_contact():
    term = input("Enter name or phone to search: ").lower()
    contacts = load_contacts()
    results = [c for c in contacts if term in c['name'].lower() or term in c['phone']]
    
    if results:
        print("\n Search Results:")
        for c in results:
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}\n")
    else:
        print("No matching contact found.\n")

def update_contact():
    term = input("Enter name or phone of contact to update: ").lower()
    contacts = load_contacts()
    for c in contacts:
        if term in c['name'].lower() or term in c['phone']:
            print(f"Updating contact: {c['name']} ({c['phone']})")
            c['name'] = input("New name (leave blank to keep current): ") or c['name']
            c['phone'] = input("New phone (leave blank to keep current): ") or c['phone']
            c['email'] = input("New email (leave blank to keep current): ") or c['email']
            c['address'] = input("New address (leave blank to keep current): ") or c['address']
            save_contacts(contacts)
            print("Contact updated.\n")
            return
    print("Contact not found.\n")

def delete_contact():
    term = input("Enter name or phone of contact to delete: ").lower()
    contacts = load_contacts()
    new_contacts = [c for c in contacts if term not in c['name'].lower() and term not in c['phone']]
    
    if len(new_contacts) != len(contacts):
        save_contacts(new_contacts)
        print("Contact deleted successfully.\n")
    else:
        print("Contact not found.\n")

def main_menu():
    while True:
        print("=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main_menu()
