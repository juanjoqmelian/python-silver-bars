import unittest
from decimal import Decimal

from order import Order
from order_type import OrderType


class OrderTest(unittest.TestCase):
    def test_valid_order(self):
        order = Order('my-user-id', 10, Decimal(12.5), OrderType.BUY)
        self.assertTrue(order.is_valid())

    def test_invalid_order_when_user_id_is_not_provided(self):
        order = Order(None, 10, Decimal(12.5), OrderType.BUY)
        self.assertFalse(order.is_valid())

    def test_invalid_order_when_user_id_is_empty(self):
        order = Order('', 10, Decimal(12.5), OrderType.BUY)
        self.assertFalse(order.is_valid())

    def test_invalid_order_when_quantity_is_not_provided(self):
        order = Order('my-user-id', None, Decimal(12.5), OrderType.BUY)
        self.assertFalse(order.is_valid())

    def test_invalid_order_when_quantity_is_negative(self):
        order = Order('my-user-id', -1, Decimal(12.5), OrderType.BUY)
        self.assertFalse(order.is_valid())

    def test_invalid_order_when_quantity_is_zero(self):
        order = Order('my-user-id', 0, Decimal(12.5), OrderType.BUY)
        self.assertFalse(order.is_valid())

    def test_invalid_order_when_price_is_not_provided(self):
        order = Order('my-user-id', 10, None, OrderType.BUY)
        self.assertFalse(order.is_valid())

    def test_invalid_order_when_price_is_negative(self):
        order = Order('my-user-id', 10, Decimal(-12.5), OrderType.BUY)
        self.assertFalse(order.is_valid())

    def test_invalid_order_when_price_is_zero(self):
        order = Order('my-user-id', 10, Decimal(0), OrderType.BUY)
        self.assertFalse(order.is_valid())

    def test_invalid_order_when_type_is_not_provided(self):
        order = Order('my-user-id', 10, Decimal(12.5), None)
        self.assertFalse(order.is_valid())

    def test_order_summary_for_buy_order(self):
        order = Order('my-user-id', 10, Decimal(12.5), OrderType.BUY)
        self.assertEqual('BUY: 10 kg for £12.50', order.summary())

    def test_order_summary_for_sell_order(self):
        order = Order('my-user-id', 10, Decimal(12.5), OrderType.SELL)
        self.assertEqual('SELL: 10 kg for £12.50', order.summary())