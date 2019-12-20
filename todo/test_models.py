from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):
    def test_done_default_is_False(self):

        item = Item(name='Test item')
        item.save()

        self.assertEqual(item.name, "Test item")
        self.assertFalse(item.done)

    def test_create_item_with_name_and_status_is_False(self):

        item = Item(name='Test item', done=False)
        item.save()

        self.assertEqual(item.name, "Test item")
        self.assertFalse(item.done)
    
    def test_create_item_with_name_and_status_is_True(self):

        item = Item(name='Test item', done=True)
        item.save()

        self.assertEqual(item.name, "Test item")
        self.assertTrue(item.done)