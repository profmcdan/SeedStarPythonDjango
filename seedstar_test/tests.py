from django.test import TestCase
from seedstar_test.models import Contact
# Create your tests here.

class ContactTests(TestCase):

    def test_str(self):
        contact = Contact(first_name='Dan', last_name='Tony')

        self.assertEquals(str(contact), 'DanTony',)
