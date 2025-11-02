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