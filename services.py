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