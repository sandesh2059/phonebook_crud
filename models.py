import json
import os

DATA_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_contacts(contacts):
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f, indent=2)

def add_contact(name, phone):
    contacts = load_contacts()
    if name in contacts:
        return False, 'Contact already exists!'
    
    contacts[name] = phone
    save_contacts(contacts)
    return True, 'Contact added successfully!'

def get_all_contacts():
    return load_contacts()

def get_contact(name):
    contacts = load_contacts()
    return contacts.get(name)

def update_contact(name, new_phone):
    contacts = load_contacts()
    if name not in contacts:
        return False, 'Contact not found!'
    
    contacts[name] = new_phone
    save_contacts(contacts)
    return True, 'Contact updated successfully!'

def delete_contact(name):
    contacts = load_contacts()
    if name not in contacts:
        return False, 'Contact not found!'
    
    del contacts[name]
    save_contacts(contacts)
    return True, 'Contact deleted successfully!'