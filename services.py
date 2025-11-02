from models import *

class ContactService:
    
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
        is_valid, error_msg = ContactService.validate_contact_data(name, phone)
        if not is_valid:
            return False, error_msg
        
        return add_contact(name.strip(), phone.strip())
    
    @staticmethod
    def get_all_contacts():
        return get_all_contacts()
    
    @staticmethod
    def get_contact(name):
        return get_contact(name)
    
    @staticmethod
    def update_contact(name, new_phone):
        if not new_phone or not new_phone.strip():
            return False, "Phone cannot be empty!"
        
        if not new_phone.strip().isdigit():
            return False, "Phone should contain only numbers!"
        
        return update_contact(name, new_phone.strip())
    
    @staticmethod
    def delete_contact(name):
        return delete_contact(name)