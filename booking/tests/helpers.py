from datetime import date, time, timedelta
from django.contrib.auth.models import User
from ..models import Booking, Customer, Table


def create_fake_registered_customer(username='testuser', **kwargs):
    user = User.objects.create_user(username=username, password='pass')
    defaults = {
        'username': user,
        'is_guest': False,
        'phone': '0123456789',
        'email': 'registered@example.com',
        'customer_fname': 'Reg',
        'customer_lname': 'User',
    }
    defaults.update(kwargs)
    return Customer.objects.create(**defaults)


def create_fake_guest_customer(**kwargs):
    defaults = {
        'username': None,
        'is_guest': True,
        'phone': '0987654321',
        'email': 'guest@example.com',
        'customer_fname': 'Guest',
        'customer_lname': 'User',
    }
    defaults.update(kwargs)
    return Customer.objects.create(**defaults)


def create_fake_table(**kwargs):
    """
    Create and return a test Table instance.
    """
    defaults = {
        'number': 1,
        'capacity': 4,
    }
    defaults.update(kwargs)
    return Table.objects.create(**defaults)


def create_fake_booking(customer=None, table=None, **kwargs):
    """
    Create a generic fake booking. By default creates a guest customer booking.
    """
    if customer is None:
        customer = create_fake_guest_customer()

    if table is None:
        table = create_fake_table()

    defaults = {
        'customer': customer,
        'date': date.today() + timedelta(days=1),
        'time': time(hour=18, minute=0),
        'party_size': 2,
        'status': 'pending',
        'table': table,
    }
    defaults.update(kwargs)
    return Booking.objects.create(**defaults)


def create_fake_registered_booking(username='testuser', **kwargs):
    """
    Create a booking for a registered customer.
    """
    customer = create_fake_registered_customer(username=username)
    table = create_fake_table()
    return create_fake_booking(customer=customer, table=table, **kwargs)


def create_fake_guest_booking(**kwargs):
    """
    Create a booking for a guest customer.
    """
    customer = create_fake_guest_customer()
    table = create_fake_table()
    return create_fake_booking(customer=customer, table=table, **kwargs)
