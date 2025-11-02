from models import *

class ContactService:
    
    @staticmethod
    def validate_contact_data(name, phone):
        pass
        @staticmethod
    def validate_contact_data(name, phone):
        if not name or not name.strip():
            return False, "Name cannot be empty!"
        
        if not phone or not phone.strip():
            return False, "Phone cannot be empty!"
        
        if len(name.strip()) < 2:
            return False, "Name must be at least 2 characters long!"
        
        if not phone.strip().isdigit():
            return False, "Phone should contain only numbers!"
        
        return True, ""
        @staticmethod
    def create_contact(name, phone):
        """
        Create new contact with validation
        Returns: (success, message)
        """
        # Validate data
        is_valid, error_msg = ContactService.validate_contact_data(name, phone)
        if not is_valid:
            return False, error_msg
        
        # Add contact
        return add_contact(name.strip(), phone.strip())
    
    @staticmethod
    def get_all_contacts():
        """
        Get all contacts
        Returns: Dictionary of contacts
        """
        return get_all_contacts()
    
    @staticmethod
    def get_contact(name):
        """
        Get specific contact
        Returns: Contact data if found, None otherwise
        """
        return get_contact(name)