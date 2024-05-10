from django.test import TestCase
from restaurant.models import Menu, Booking
from decimal import Decimal
from datetime import datetime

# Create your tests here.
class MenuItemTest(TestCase): 
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), 'IceCream : 80')

    def test_default_inventory(self):
        item = Menu.objects.create(title="Strawberry Cheesecake", price=Decimal('50'))
        self.assertEqual(item.inventory, 5)

class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            name="Jakub Ritz",
            number_of_guests=8,
            booking_date=datetime(2024, 5, 10, 15, 36)
        )
        expected_str = "Jakub Ritz for 8 guests on 2024-05-10 15:36:00"
        self.assertEqual(str(booking), expected_str)

    def test_default_number_of_guests(self):
        booking = Booking.objects.create(
            name="Jakub Ritz",
            booking_date=datetime(2025, 5, 10, 15, 38)
        )
        self.assertEqual(booking.number_of_guests, 6)