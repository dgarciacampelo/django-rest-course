from .models import Contact
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


def create_contact_data(**kwargs):
    default_data = {
        "name": "Daniel Garcia",
        "message": "This is a test message",
        "email": "danielgarciah@test.com",
    }
    default_data.update(kwargs)
    return default_data


class ContactTestCase(APITestCase):
    """Test suite for Contact"""

    def setUp(self):
        self.client = APIClient()
        self.url = "/contact/"

    def test_create_contact(self):
        """Test ContactViewSet create method"""
        print("Testing for valid data (1 contact in db)...")
        data = create_contact_data()
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().title, "Daniel Garcia")

    def test_create_contact_with_blank_fields(self):
        """Test ContactViewSet create method with blank fields"""
        fields_to_test = ["name", "message", "email"]

        for field in fields_to_test:
            # Print a message to know what field is being tested
            print(f"Testing for blank {field}...")
            data = create_contact_data(**{field: ""})
            response = self.client.post(self.url, data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_with_missing_fields(self):
        """Test ContactViewSet create method with missing fields"""
        fields_to_test = ["name", "message", "email"]

        for field in fields_to_test:
            # Print a message to know what field is being tested
            print(f"Testing for missing {field}...")
            data = create_contact_data()
            data.pop(field)
            response = self.client.post(self.url, data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_when_email_equals_non_email(self):
        """test ContactViewSet create method when email is not email"""
        print("Testing for non-email email...")
        data = create_contact_data()
        data["email"] = "test"
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
