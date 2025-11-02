"""
Data Layer - Handles all data operations
Team Member 1: Data Management
"""
import json
import os

DATA_FILE = 'contacts.json'

def load_contacts():
    """
    Load all contacts from JSON file
    Returns: Dictionary of contacts
  """
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_contacts(contacts):
    """
    Save contacts to JSON file
    Args: contacts - Dictionary of contacts to save
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f, indent=2)
        def add_contact(name, phone):
    """
    Add a new contact
    Returns: (success, message)
    """
    contacts = load_contacts()
    if name in contacts:
        return False, 'Contact already exists!'
    
    contacts[name] = phone
    save_contacts(contacts)
    return True, 'Contact added successfully!'
def get_all_contacts():
    """
    Get all contacts
    Returns: Dictionary of all contacts
    """
    return load_contacts()
def get_contact(name):
    """
    Get specific contact
    Returns: Contact data if found, None otherwise
    """
    contacts = load_contacts()
    return contacts.get(name)

def update_contact(name, new_phone):
    """
    Update existing contact
    Returns: (success, message)
    """
    contacts = load_contacts()
    if name not in contacts:
        return False, 'Contact not found!'
    
    contacts[name] = new_phone
    save_contacts(contacts)
    return True, 'Contact updated successfully!'
