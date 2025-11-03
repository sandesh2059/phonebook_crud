import unittest
import os
import json
import models

class TestPhoneBook(unittest.TestCase):
    
    def setUp(self):
        self.test_file = 'test_contacts.json'
        # Set the test file directly in the models module
        models.DATA_FILE = self.test_file
        # Clear test file before each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        # Reset to original data file
        models.DATA_FILE = 'contacts.json'
    
    def test_add_contact_success(self):
        success, message = models.add_contact("Abhi Sharma", "9841234567")
        self.assertTrue(success)
        self.assertEqual(message, "Contact added successfully!")
    
    def test_add_contact_duplicate(self):
        models.add_contact("Abhi Sharma", "9841234567")
        success, message = models.add_contact("Abhi Sharma", "9851122334")
        self.assertFalse(success)
        self.assertEqual(message, "Contact already exists!")
    
    def test_get_all_contacts(self):
        models.add_contact("Abhi", "9841111111")
        models.add_contact("Sita", "9852222222")
        contacts = models.get_all_contacts()
        self.assertEqual(len(contacts), 2)
        self.assertIn("Abhi", contacts)
        self.assertIn("Sita", contacts)
    
    def test_get_contact_found(self):
        models.add_contact("Abhi", "9841234567")
        phone = models.get_contact("Abhi")
        self.assertEqual(phone, "9841234567")
    
    def test_get_contact_not_found(self):
        phone = models.get_contact("Nonexistent")
        self.assertIsNone(phone)
    
    def test_update_contact_success(self):
        models.add_contact("Abhi", "9841111111")
        success, message = models.update_contact("Abhi", "9859999999")
        self.assertTrue(success)
        self.assertEqual(message, "Contact updated successfully!")
        phone = models.get_contact("Abhi")
        self.assertEqual(phone, "9859999999")
    
    def test_update_contact_not_found(self):
        success, message = models.update_contact("Nonexistent", "9841234567")
        self.assertFalse(success)
        self.assertEqual(message, "Contact not found!")
    
    def test_delete_contact_success(self):
        models.add_contact("Abhi", "9841234567")
        success, message = models.delete_contact("Abhi")
        self.assertTrue(success)
        self.assertEqual(message, "Contact deleted successfully!")
        phone = models.get_contact("Abhi")
        self.assertIsNone(phone)
    
    def test_delete_contact_not_found(self):
        success, message = models.delete_contact("Nonexistent")
        self.assertFalse(success)
        self.assertEqual(message, "Contact not found!")
    
    def test_data_persistence(self):
        models.add_contact("Abhi", "9841111111")
        contacts1 = models.get_all_contacts()
        contacts2 = models.get_all_contacts()
        self.assertEqual(contacts1, contacts2)
    
    def test_multiple_contacts(self):
        models.add_contact("Abhi Sharma", "9841234567")
        models.add_contact("Sita Koirala", "9851122334")
        models.add_contact("Ram Bahadur", "9864455667")
        contacts = models.get_all_contacts()
        self.assertEqual(len(contacts), 3)
        self.assertIn("Abhi Sharma", contacts)
        self.assertIn("Sita Koirala", contacts)
        self.assertIn("Ram Bahadur", contacts)

if __name__ == '__main__':
    unittest.main()