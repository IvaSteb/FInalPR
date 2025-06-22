def menu():
        print("Hello! You in ContactBook! Choose the option: ")
        print("1. Record new contact")
        print("2. Delete contact")
        print("3. List of contacts")
        print("4. Quit")



class Contact:    
    def __init__(self, name, phone_number): 
        self.name = name
        self.phone_number = phone_number
    
    def __str__(self):
        return f"Name: {self.name}; Number: {self.phone_number}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added")
        
    def delete_contact(self, name_to_delete):
        initial_count = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name_to_delete.lower()]

        if len(self.contacts) < initial_count:
            print(f"Contacts with name '{name_to_delete}' deleted.")
        else:
            print(f"Contacts with name '{name_to_delete}' dont found.")
        
    def list_contacts(self):
        if not self.contacts: 
            print("List of contacts empty!")
            return

        print("\n--- Yours Contacts ---")
        for i, contact in enumerate(self.contacts):
            print(f"{i + 1}. {contact}") 
        print("---------------------\n")
    


