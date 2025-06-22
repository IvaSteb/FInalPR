from contact_book import Contact, ContactBook, menu

my_contact_book = ContactBook()

def main_loop():
    while True: 
        menu() 
        choice = int(input("Your choice: "))

        if choice == 1:
            name = input("Name: ")
            phone = input("Number: ")
            new_contact = Contact(name, phone) 
            my_contact_book.add_contact(new_contact) 

        elif choice == 2:
            name_to_delete = input("Enter name to delete: ")
            my_contact_book.delete_contact(name_to_delete)

        elif choice == 3:
            my_contact_book.list_contacts()

        elif choice == 4:
            print("Goodbye!")
            break 
        
        else:
            print("Wrong choice!\nTry again!")

if __name__ == "__main__":
    main_loop()