from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestToDoItemForm(TestCase):

    def test_can_create_item_with_just_name(self):
        form = ItemForm({'name': 'Create tests'})
        self.assertTrue(form.is_valid())

    def test_error_message_for_missing_name(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

# test needs to start with test_, only than will Django see it as a test