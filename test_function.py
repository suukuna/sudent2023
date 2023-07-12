import function
# from unittest import TestCase


# class TestC(TestCase):
#     def test_something(self):
#         products = [
#             {'product': 'bread', 'price': 25},
#             {'product': 'milk', 'price': 30},
#             {'product': 'eggs', 'price': 35}
#         ]
#         max_price = 10
#
#         self.assertEqual(function.get_allowed_products(products, max_price), [])

def test_none_matching_products():
    products = [
        {'product': 'bread', 'price': 25},
        {'product': 'milk', 'price': 30},
        {'product': 'eggs', 'price': 35}
    ]
    max_price = 10
    assert function.get_allowed_products(products, max_price) == []


def test_all_matching_products():
    products = [
        {'product': 'bread', 'price': 25},
        {'product': 'milk', 'price': 30},
        {'product': 'eggs', 'price': 35}
    ]
    max_price = 50
    assert function.get_allowed_products(products, max_price) == ['bread', 'milk', 'eggs']


def test_partial_matching_products():
    products = [
        {'product': 'bread', 'price': 25},
        {'product': 'milk', 'price': 30},
        {'product': 'eggs', 'price': 35}
    ]
    max_price = 30
    assert function.get_allowed_products(products, max_price) == ['bread', 'milk']
