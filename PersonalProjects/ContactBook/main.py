import csv


def load_contacts(filename):
    contacts = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            contacts = list(reader)
    except FileNotFoundError:
        pass
    return contacts


def save_contacts(filename, contacts):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)


def display_contacts(contacts):
    print("Contact Book:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact[0]}, Phone: {contact[1]}")
    print("\n")


def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    contacts.append([name, phone])
    print("Contact added!\n")


def remove_contact(contacts):
    display_contacts(contacts)
    contact_no = int(input("Enter the contact number to remove: "))
    if 1 <= contact_no <= len(contacts):
        contacts.pop(contact_no - 1)
        print("Contact removed!\n")
    else:
        print("Invalid contact number!\n")


def main():
    filename = 'contacts.csv'
    contacts = load_contacts(filename)

    while True:
        display_contacts(contacts)
        print("Options:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            remove_contact(contacts)
        elif choice == '3':
            break
        else:
            print("Invalid choice!\n")

    save_contacts(filename, contacts)


if __name__ == "__main__":
    main()